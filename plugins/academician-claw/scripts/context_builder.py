#!/usr/bin/env python3
"""
openclaw-script: true
name: context_builder
description: Reads all memory and context files and outputs a formatted CONTEXT BLOCK
             ready to paste into Claude alongside ORCHESTRATOR.md.
             NO LLM API calls. Pure file reading and text formatting.
permissions: read-only
created: 2026-05-07
"""

import sys
import os
import datetime
import re
from pathlib import Path

BASE = Path(__file__).parent.parent  # plugin root

def read(rel, default="[not found]"):
    p = BASE / rel
    return p.read_text(encoding="utf-8").strip() if p.exists() else default

def section(title, content, max_lines=None):
    lines = content.split("\n")
    if max_lines and len(lines) > max_lines:
        content = "\n".join(lines[-max_lines:])
        content = f"[...trimmed to last {max_lines} lines...]\n" + content
    return f"\n### {title}\n{content}\n"

def extract_tasks(tasks_content):
    """Pull out only open tasks to keep context compact."""
    lines = tasks_content.split("\n")
    out = []
    in_completed = False
    for line in lines:
        if "## ✅" in line:
            in_completed = True
        if in_completed and not line.startswith("##"):
            continue
        if line.startswith("##"):
            in_completed = False
        out.append(line)
    return "\n".join(out)

def get_overdue_tasks(tasks_content):
    """Find tasks with due dates in the past."""
    today = datetime.date.today()
    overdue = []
    for line in tasks_content.split("\n"):
        m = re.search(r"Due:\s*(\d{4}-\d{2}-\d{2})", line)
        if m and "- [ ]" in line:
            try:
                due = datetime.date.fromisoformat(m.group(1))
                if due < today:
                    task_text = re.sub(r"\|.*", "", line.replace("- [ ]", "")).strip()
                    overdue.append(f"OVERDUE ({m.group(1)}): {task_text}")
            except ValueError:
                pass
    return overdue

def get_due_today(tasks_content):
    """Find tasks due today."""
    today = datetime.date.today().isoformat()
    due = []
    for line in tasks_content.split("\n"):
        if today in line and "- [ ]" in line:
            task_text = re.sub(r"\|.*", "", line.replace("- [ ]", "")).strip()
            due.append(task_text)
    return due

def extract_recent_episodic(episodic_content, n=8):
    """Extract the last N episodic entries."""
    entries = re.split(r"(?=^## \[)", episodic_content, flags=re.MULTILINE)
    entries = [e.strip() for e in entries if e.strip() and e.strip().startswith("##")]
    return "\n\n".join(entries[-n:]) if entries else "[no entries yet]"

def extract_active_habits(habits_content):
    """Pull just the active habits section."""
    m = re.search(r"## Active Habits(.+?)(?=^## |\Z)", habits_content,
                  re.DOTALL | re.MULTILINE)
    return m.group(1).strip() if m else "[no active habits]"

def build_context_block():
    today = datetime.date.today().isoformat()
    now   = datetime.datetime.now().strftime("%H:%M")

    # ── Read all memory files ────────────────────────────────────────────────
    soul          = read("memory/soul.md")
    work          = read("memory/semantic/work.md")
    prefs         = read("memory/semantic/preferences.md")
    vocab         = read("memory/semantic/vocabulary.md")
    relationships = read("memory/semantic/relationships.md")
    writing_style = read("memory/procedural/writing-style.md")
    code_style    = read("memory/procedural/code-style.md")
    dec_patterns  = read("memory/procedural/decision-patterns.md")
    relationship  = read("memory/procedural/relationship.md")
    tasks_raw     = read("context/tasks.md")
    project       = read("context/active-project.md")
    session       = read("context/current-session.md")
    episodic_raw  = read("memory/episodic/recent.md")
    habits_raw    = read("memory/habits/habits.md")
    ideas_idx     = read("memory/semantic/ideas.md")
    learning      = read("memory/semantic/learning.md")
    registry      = read("agents/registry.md")

    # ── Process ──────────────────────────────────────────────────────────────
    tasks_clean   = extract_tasks(tasks_raw)
    overdue       = get_overdue_tasks(tasks_raw)
    due_today     = get_due_today(tasks_raw)
    recent_ep     = extract_recent_episodic(episodic_raw)
    active_habits = extract_active_habits(habits_raw)

    # ── Alerts ───────────────────────────────────────────────────────────────
    alerts = []
    if overdue:
        alerts.append("⚠️  OVERDUE TASKS:\n" + "\n".join(f"  • {o}" for o in overdue))
    if due_today:
        alerts.append("📅 DUE TODAY:\n" + "\n".join(f"  • {d}" for d in due_today))

    alert_block = "\n".join(alerts) if alerts else "  No overdue or due-today items."

    # ── Estimate token size ──────────────────────────────────────────────────
    # rough: 4 chars ~ 1 token
    all_text = soul + work + prefs + writing_style + tasks_clean + \
               recent_ep + active_habits + project
    est_tokens = len(all_text) // 4

    # ── Assemble output ──────────────────────────────────────────────────────
    out = []
    out.append("=" * 70)
    out.append(f"OPENCLAW CONTEXT BLOCK — {today} {now}")
    out.append(f"Estimated tokens: ~{est_tokens:,}  |  Paste below ORCHESTRATOR.md")
    out.append("=" * 70)

    out.append("\n## 🚨 ALERTS")
    out.append(alert_block)

    out.append(section("SOUL PROFILE", soul, max_lines=60))
    out.append(section("WORK CONTEXT", work, max_lines=40))
    out.append(section("ACTIVE PROJECT", project, max_lines=30))
    out.append(section("WRITING & STYLE PREFERENCES", writing_style, max_lines=30))
    out.append(section("CODE STYLE", code_style, max_lines=20))
    out.append(section("DECISION PATTERNS", dec_patterns, max_lines=20))
    out.append(section("RELATIONSHIP ARC", relationship, max_lines=15))
    out.append(section("OPEN TASKS (active only)", tasks_clean, max_lines=50))
    out.append(section("CURRENT SESSION", session, max_lines=20))
    out.append(section("ACTIVE HABITS", active_habits, max_lines=30))
    out.append(section("RECENT EPISODIC MEMORY (last 8 entries)", recent_ep, max_lines=80))
    out.append(section("VOCABULARY & JARGON", vocab, max_lines=20))
    out.append(section("ACTIVE LEARNING GOALS", learning, max_lines=20))
    out.append(section("IDEAS — ACTIVE", ideas_idx, max_lines=20))
    out.append(section("AGENT REGISTRY", registry, max_lines=40))

    out.append("\n" + "=" * 70)
    out.append("END CONTEXT BLOCK")
    out.append("=" * 70)

    return "\n".join(out)

if __name__ == "__main__":
    # Optional: copy to clipboard if pyperclip is available
    context = build_context_block()
    print(context)

    if "--copy" in sys.argv:
        try:
            import pyperclip
            pyperclip.copy(context)
            print("\n[Copied to clipboard]", file=sys.stderr)
        except ImportError:
            print("\n[Install pyperclip for clipboard support: pip install pyperclip]",
                  file=sys.stderr)

    # Log the build
    log_path = BASE / "logs/sessions.log"
    log_path.parent.mkdir(exist_ok=True)
    today = datetime.date.today().isoformat()
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{today}] context_builder ran — ~{len(context)//4} tokens\n")
