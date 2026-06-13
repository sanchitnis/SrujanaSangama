#!/usr/bin/env python3
"""
openclaw-script: true
name: update_memory
description: Parses a SESSION_SUMMARY block produced by Claude (via SESSION_CLOSER.md)
             and updates memory files accordingly.
             NO LLM API calls. Pure text parsing and file writes.
permissions: write
created: 2026-05-07
"""

import re
import sys
import datetime
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import BASE, WORKSPACE_ROOT, resolve_path


def read(rel, default=""):
    p = resolve_path(rel)
    return p.read_text(encoding="utf-8") if p.exists() else default

def write(rel, content):
    p = resolve_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def append_to(rel, content):
    p = resolve_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(content)

def log_change(msg):
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    append_to("logs/memory-changes.log", f"[{ts}] {msg}\n")

# ─── Parsers ──────────────────────────────────────────────────────────────────

def extract_block(text, field):
    """Extract multi-line list under a SESSION_SUMMARY field."""
    pattern = rf"^{re.escape(field)}:\s*\n((?:- .+\n?)+)"
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return []
    items = re.findall(r"^- (.+)$", m.group(1), re.MULTILINE)
    return [i.strip() for i in items if i.strip() and i.strip() != "[none]"]

def extract_single(text, field):
    """Extract a single-line field value."""
    m = re.search(rf"^{re.escape(field)}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""

def extract_multiline(text, field):
    """Extract a multi-sentence field (like EPISODIC_ENTRY)."""
    pattern = rf"^{re.escape(field)}:\s*\n([\s\S]+?)(?=\n[A-Z_]+:|\n===|$)"
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(1).strip() if m else ""

# ─── Updaters ─────────────────────────────────────────────────────────────────

def update_episodic(entry_text, date_str):
    """Append a new episodic entry to memory/episodic/recent.md."""
    content = read("memory/episodic/recent.md")
    new_entry = f"\n## [{date_str}] — Session\n{entry_text}\n"
    content += new_entry
    write("memory/episodic/recent.md", content)
    log_change(f"episodic/recent.md: added entry for {date_str}")

    # Prune if over 500 lines
    lines = content.split("\n")
    if len(lines) > 500:
        archive_date = datetime.date.today().strftime("%Y-%m")
        archive_path = f"memory/episodic/{archive_date}.md"
        archive_content = read(archive_path, f"# Episodic Archive — {archive_date}\n\n")
        archive_content += "\n".join(lines[:200]) + "\n"
        write(archive_path, archive_content)
        write("memory/episodic/recent.md", "\n".join(lines[200:]))
        log_change(f"episodic/recent.md: pruned — archived 200 lines to {archive_path}")

def update_tasks(captured, completed):
    """Add captured tasks and mark completed tasks in context/tasks.md."""
    content = read("context/tasks.md", "# Task List\n\n## 🔴 P1\n[none]\n\n## 🟡 P2\n[none]\n\n## 🟢 P3\n[none]\n\n## ✅ Completed (last 7 days)\n[none]\n\n## 🚫 Blocked\n[none]\n")
    today = datetime.date.today().isoformat()

    # Update timestamp
    content = re.sub(r"_Last updated:.*?_", f"_Last updated: {today}_", content)

    # Add captured tasks
    section_map = {"p1": "## 🔴 P1", "p2": "## 🟡 P2", "p3": "## 🟢 P3"}
    for task_line in captured:
        # Format: priority: p1/p2/p3 | text: description | due: date
        m = re.match(r"priority:\s*(p\d)\s*\|\s*text:\s*(.+?)\s*\|\s*due:\s*(.+)", task_line, re.IGNORECASE)
        if not m:
            # Fallback: treat whole line as P2 task
            new_line = f"- [ ] {task_line} | Due: none\n"
            content = _insert_task(content, "## 🟡 P2", new_line)
            continue
        priority, text, due = m.group(1).lower(), m.group(2).strip(), m.group(3).strip()
        new_line = f"- [ ] {text} | Due: {due}\n"
        header = section_map.get(priority, "## 🟡 P2")
        content = _insert_task(content, header, new_line)
        log_change(f"tasks.md: added [{priority}] {text}")

    # Mark completed tasks
    for done_text in completed:
        pattern = rf"- \[ \] {re.escape(done_text.strip())}.*"
        replacement = f"- [x] {done_text.strip()} | Completed: {today}"
        content, n = re.subn(pattern, replacement, content)
        if n:
            log_change(f"tasks.md: marked done — {done_text[:60]}")

    write("context/tasks.md", content)

def _insert_task(content, header, new_line):
    """Insert a task line under the appropriate header."""
    if header + "\n[none]\n" in content:
        content = content.replace(header + "\n[none]\n", header + "\n" + new_line)
    elif header in content:
        idx = content.index(header) + len(header) + 1
        content = content[:idx] + new_line + content[idx:]
    return content

def update_habits(logged):
    """Update habit streaks in memory/habits/habits.md."""
    content = read("memory/habits/habits.md")
    today = datetime.date.today().isoformat()

    for entry in logged:
        # Format: habit name | status: done/missed | date: YYYY-MM-DD
        m = re.match(r"(.+?)\s*\|\s*status:\s*(done|missed)\s*\|\s*date:\s*(\S+)", entry, re.IGNORECASE)
        if not m:
            continue
        name, status, date = m.group(1).strip(), m.group(2).lower(), m.group(3).strip()
        symbol = "✅" if status == "done" else "❌"

        # Update weekly log
        log_line = f"| {date} | {name} | {symbol} |"
        append_to("memory/habits/habits.md", f"\n{log_line}")
        log_change(f"habits.md: {name} — {status} on {date}")

        # Update Last completed and streak for done habits
        if status == "done":
            content = _update_habit_streak(content, name, date)

    write("memory/habits/habits.md", content)

def _update_habit_streak(content, habit_name, date):
    """Find the habit section and increment streak."""
    pattern = rf"(### {re.escape(habit_name)}\n[\s\S]+?)(- \*\*Streak\*\*: )(\d+)( days)"
    def increment(m):
        new_streak = int(m.group(3)) + 1
        return m.group(1) + m.group(2) + str(new_streak) + m.group(4)
    content, _ = re.subn(pattern, increment, content)

    # Update last completed
    pattern2 = rf"(### {re.escape(habit_name)}\n[\s\S]+?)(- \*\*Last completed\*\*: )(\S+)"
    content, _ = re.subn(pattern2, rf"\g<1>\g<2>{date}", content)
    return content

def update_memory_facts(updates):
    """Write new memory facts to the appropriate files."""
    today = datetime.date.today().isoformat()

    for update_line in updates:
        # Format: fact | tier: X | file: filename.md
        m = re.match(r"(.+?)\s*\|\s*tier:\s*(\S+)\s*\|\s*file:\s*(\S+)", update_line, re.IGNORECASE)
        if not m:
            # No file specified — append to episodic
            append_to("memory/episodic/recent.md",
                      f"\n_[MEMORY {today}]: {update_line.strip()}_\n")
            log_change(f"episodic: added unstructured memory: {update_line[:60]}")
            continue

        fact, tier, filename = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()

        # Build file path from tier and filename
        tier_dirs = {
            "soul": "memory",
            "semantic": "memory/semantic",
            "procedural": "memory/procedural",
            "episodic": "memory/episodic",
        }
        dir_ = tier_dirs.get(tier.lower(), "memory/semantic")
        filepath = f"{dir_}/{filename}"

        current = read(filepath, "")
        new_entry = f"\n- [NEW {today}] {fact}\n"

        if "## Inferred from Interactions" in current:
            current = current.replace(
                "## Inferred from Interactions\n_[Auto-populated by Memory Steward]_\n- ",
                f"## Inferred from Interactions\n_[Auto-populated by Memory Steward]_\n{new_entry}- "
            )
        else:
            current += new_entry

        write(filepath, current)
        log_change(f"{filepath}: added fact — {fact[:60]}")

def mark_deprecated(deprecated):
    """Mark deprecated facts across memory files."""
    today = datetime.date.today().isoformat()
    for fact in deprecated:
        append_to("memory/episodic/recent.md",
                  f"\n_[DEPRECATED {today}]: {fact.strip()}_\n")
        log_change(f"deprecated: {fact[:60]}")

def update_session_log(summary_data, date_str):
    """Write one-line entry to logs/sessions.log."""
    agents = summary_data.get("agents", "[not recorded]")
    topics = summary_data.get("accomplished", ["[not recorded]"])[:2]
    topics_str = "; ".join(topics)
    append_to("logs/sessions.log",
              f"[{date_str}] agents={agents} | topics={topics_str}\n")

# ─── Main ─────────────────────────────────────────────────────────────────────

BANNER = """
╔══════════════════════════════════════════╗
║   OpenClaw — Memory Update              ║
║   Paste Claude's SESSION_SUMMARY block  ║
╚══════════════════════════════════════════╝

Paste the SESSION_SUMMARY block from Claude.
Type END on a new line when done, or press Ctrl+D.
"""

def get_summary_input():
    """Accept multi-line paste from stdin."""
    if not sys.stdin.isatty():
        # Piped input
        return sys.stdin.read()

    print(BANNER)
    lines = []
    try:
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
    except EOFError:
        pass
    return "\n".join(lines)

def main():
    raw = get_summary_input()

    # Extract the block between delimiters
    m = re.search(r"===SESSION_SUMMARY_START===([\s\S]+?)===SESSION_SUMMARY_END===", raw)
    if not m:
        print("⚠  No valid SESSION_SUMMARY block found.")
        print("   Make sure you pasted the full block including the === delimiters.")
        sys.exit(1)

    summary = m.group(1).strip()

    # Parse all fields
    date_str    = extract_single(summary, "DATE") or datetime.date.today().isoformat()
    episodic    = extract_multiline(summary, "EPISODIC_ENTRY")
    accomplished= extract_block(summary, "ACCOMPLISHED")
    mem_updates = extract_block(summary, "MEMORY_UPDATES")
    tasks_cap   = extract_block(summary, "TASKS_CAPTURED")
    tasks_done  = extract_block(summary, "TASKS_COMPLETED")
    habits_log  = extract_block(summary, "HABITS_LOGGED")
    deprecated  = extract_block(summary, "DEPRECATED_FACTS")
    skill_gaps  = extract_block(summary, "SKILL_GAPS")
    agents_used = extract_single(summary, "AGENTS_USED")
    open_threads= extract_block(summary, "OPEN_THREADS")

    print(f"\nParsed summary for {date_str}")
    print(f"  Memory updates:   {len(mem_updates)}")
    print(f"  Tasks captured:   {len(tasks_cap)}")
    print(f"  Tasks completed:  {len(tasks_done)}")
    print(f"  Habits logged:    {len(habits_log)}")
    print(f"  Deprecated facts: {len(deprecated)}")

    # Apply updates
    if episodic:
        update_episodic(episodic, date_str)
        print("  ✅ Episodic memory updated")

    if mem_updates:
        update_memory_facts(mem_updates)
        print("  ✅ Semantic/procedural memory updated")

    if tasks_cap or tasks_done:
        update_tasks(tasks_cap, tasks_done)
        print("  ✅ Tasks updated")

    if habits_log:
        update_habits(habits_log)
        print("  ✅ Habits updated")

    if deprecated:
        mark_deprecated(deprecated)
        print("  ✅ Deprecated facts marked")

    # Update session log
    update_session_log({"accomplished": accomplished, "agents": agents_used}, date_str)

    # Update current-session.md with open threads
    if open_threads:
        threads_text = "\n".join(f"- {t}" for t in open_threads)
        session_content = f"# Current Session\n_Updated: {date_str}_\n\n## Focus\n[Start of new session]\n\n## Carried Over from Last Session\n{threads_text}\n"
        write("context/current-session.md", session_content)
        print("  ✅ current-session.md updated with open threads")

    # Report skill gaps
    if skill_gaps:
        print(f"\n  ✨ Skill gaps detected ({len(skill_gaps)}):")
        for sg in skill_gaps:
            print(f"     • {sg}")
        print("     → Paste prompts/workflows/SKILL_GENERATOR.md into Claude to generate them")

    print(f"\n  Done. All changes logged to logs/memory-changes.log\n")

if __name__ == "__main__":
    main()
