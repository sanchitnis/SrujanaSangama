#!/usr/bin/env python3
"""
openclaw-script: true
name: cee_context_builder
description: Extends context_builder.py with --cee flag. Reads all CEE memory files
             (cee-identity.md, para-projects.md, para-areas.md, holding-inbox.md,
             termite-history.md) and appends a ### CEE CONTEXT section to the
             standard context block. Also detects Weekly Alignment Audit trigger
             (post-Friday 6PM IST or Saturday/Sunday) and prepends an alert.
             NO LLM API calls. Pure file reading, date math, and text formatting.
permissions: read-only
created: 2026-06-11
"""

import sys
import os
import datetime
import re
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────
import path_resolver
from path_resolver import BASE, WORKSPACE_ROOT, resolve_path, get_private_dir

CEE_CONTEXT = get_private_dir() / "context"
CEE_SEM     = get_private_dir() / "semantic"
CEE_ARCHIVE = get_private_dir() / "archive"
CEE_LOGS    = get_private_dir() / "logs"



def read(path, default="[not found]"):
    p = Path(path)
    return p.read_text(encoding="utf-8").strip() if p.exists() else default


def section(title, content, max_lines=None):
    lines = content.split("\n")
    if max_lines and len(lines) > max_lines:
        content = "\n".join(lines[-max_lines:])
        content = f"[...trimmed to last {max_lines} lines...]\n" + content
    return f"\n### {title}\n{content}\n"


# ── Weekly Audit Trigger Detection ───────────────────────────────────────────
def is_weekly_audit_due():
    """Returns True if current time is post-Friday 6PM IST or Sat/Sun."""
    # IST = UTC+5:30
    utc_now = datetime.datetime.utcnow()
    ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
    weekday = ist_now.weekday()  # 0=Mon, 4=Fri, 5=Sat, 6=Sun
    hour    = ist_now.hour

    if weekday == 4 and hour >= 18:   # Friday after 6 PM
        return True
    if weekday in (5, 6):             # Saturday or Sunday
        return True
    return False


def get_audit_trigger_message(ist_now):
    weekday = ist_now.weekday()
    day_name = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][weekday]
    friday = ist_now - datetime.timedelta(days=(weekday - 4) % 7)
    friday_str = friday.strftime("%Y-%m-%d")
    return (
        f"⚠️  WEEKLY AUDIT DUE\n"
        f"    It's {day_name}. Week ending {friday_str}.\n"
        f"    → Paste workflows/08_weekly-alignment-audit.md for your Weekly Alignment Audit."
    )


# ── CEE-specific parsers ─────────────────────────────────────────────────────
def count_active_projects(para_projects_content):
    """Count Active projects in para-projects.md."""
    count = 0
    for line in para_projects_content.split("\n"):
        if "| Active |" in line or "Active" in line and "|" in line:
            count += 1
    return count


def count_holding_items(holding_content):
    """Count non-header, non-empty table rows in holding-inbox.md."""
    count = 0
    in_table = False
    for line in holding_content.split("\n"):
        if line.startswith("| #") or line.startswith("|---|"):
            in_table = True
            continue
        if in_table and line.startswith("|") and "[not found]" not in line:
            # Skip placeholder rows
            if "[YYYY-MM-DD]" not in line and "[to fill]" not in line:
                count += 1
    return count


def get_last_termite(termite_content):
    """Extract the most recent termite action from the log."""
    lines = [l for l in termite_content.split("\n")
             if l.startswith("|") and "YYYY-MM-DD" not in l and "Date" not in l
             and "---|" not in l]
    if not lines:
        return "None yet."
    last = lines[-1]
    # Extract date and description from table row
    parts = [p.strip() for p in last.split("|") if p.strip()]
    if len(parts) >= 3:
        return f"{parts[1]} — {parts[2]}"
    return last.strip()


def get_area_health_alerts(areas_content):
    """Find areas with health 🟡 or 🔴."""
    alerts = []
    for line in areas_content.split("\n"):
        if "🟡" in line or "🔴" in line:
            alerts.append(line.strip().lstrip("|").split("|")[0].strip())
    return alerts


def count_tasks_by_tag(tasks_content):
    """Count cognitive tags in enriched task table."""
    tags = {"#deep-work": 0, "#quick-review": 0, "#dependency-block": 0, "#async-delegate": 0}
    for tag in tags:
        tags[tag] = tasks_content.count(tag)
    return tags


def get_overdue_task_rows(tasks_content):
    """Find task table rows where Scheduled Date < today and Status != done."""
    today = datetime.date.today()
    overdue = []
    for line in tasks_content.split("\n"):
        if "|" not in line:
            continue
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", line)
        if date_match and "done" not in line.lower():
            try:
                task_date = datetime.date.fromisoformat(date_match.group(1))
                if task_date < today:
                    cols = [c.strip() for c in line.split("|") if c.strip()]
                    if cols:
                        overdue.append(line.strip())
            except ValueError:
                pass
    return overdue


# ── CEE Context Builder ──────────────────────────────────────────────────────
def build_cee_section():
    """Read all CEE memory files and build the CEE CONTEXT section."""
    today = datetime.date.today()

    # IST now for audit trigger
    utc_now = datetime.datetime.utcnow()
    ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)

    # Read CEE files — each from its correct folder in the memory hierarchy
    cee_identity   = read(CEE_SEM     / "cee-identity.md")      # semantic/ — strategic knowledge
    para_projects  = read(CEE_CONTEXT / "para-projects.md")     # context/  — active work
    para_areas     = read(CEE_SEM     / "para-areas.md")        # semantic/ — ongoing domains
    holding_inbox  = read(CEE_CONTEXT / "holding-inbox.md")     # context/  — pending actionable
    termite_hist   = read(CEE_LOGS    / "termite-history.md")   # logs/     — execution history
    tasks_raw      = read(resolve_path("context/tasks.md"))

    # Derive metrics
    active_projects = count_active_projects(para_projects)
    cap_warning     = " ⚠️ CAP REACHED — hold new projects" if active_projects >= 3 else ""
    inbox_count     = count_holding_items(holding_inbox)
    last_termite    = get_last_termite(termite_hist)
    area_alerts     = get_area_health_alerts(para_areas)
    tag_counts      = count_tasks_by_tag(tasks_raw)
    overdue_rows    = get_overdue_task_rows(tasks_raw)

    total_tasks = sum(tag_counts.values())
    admin_ratio = 0
    if total_tasks > 0:
        admin_tasks = tag_counts["#quick-review"] + tag_counts["#async-delegate"]
        admin_ratio = round((admin_tasks / total_tasks) * 100)

    # Build section
    out = []
    out.append("\n" + "═" * 60)
    out.append("### CEE CONTEXT")
    out.append("═" * 60)

    # Active project cap
    out.append(f"\n📊 ACTIVE PROJECTS: {active_projects}/3{cap_warning}")

    # Tag distribution
    out.append(f"\n🎯 TASK FOCUS DISTRIBUTION (this week):")
    for tag, count in tag_counts.items():
        out.append(f"   {tag}: {count}")
    if admin_ratio > 40:
        out.append(f"   ⚠️ DRIFT ALERT: {admin_ratio}% admin tasks (threshold: 40%)")

    # Overdue tasks
    if overdue_rows:
        out.append(f"\n📋 OVERDUE TASKS ({len(overdue_rows)}):")
        for row in overdue_rows[:5]:
            out.append(f"   {row}")
    else:
        out.append("\n✅ No overdue tasks.")

    # Holding inbox
    out.append(f"\n📥 HOLDING INBOX: {inbox_count} item(s) pending")

    # Last termite
    out.append(f"\n🤖 LAST TERMITE: {last_termite}")

    # Area alerts
    if area_alerts:
        out.append(f"\n⚠️ AREA HEALTH ALERTS:")
        for a in area_alerts:
            out.append(f"   • {a}")

    # CEE identity extract (compact)
    out.append(section("CEE IDENTITY (compact)", cee_identity, max_lines=20))

    # Gemini /schedule reminder (if first-run signal)
    if "Gemini /schedule not configured" in cee_identity or "[not found]" in cee_identity:
        out.append("\n💡 SETUP REMINDER: Morning Briefing via Gemini /schedule not yet configured.")
        out.append("   → In Gemini: /schedule → Daily → 6:00 AM → paste workflows/07_morning-briefing.md")

    return "\n".join(out)


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    cee_mode = "--cee" in sys.argv

    # Import and run standard context builder
    sys.path.insert(0, str(BASE / "scripts"))
    try:
        import context_builder
        context = context_builder.build_context_block()
    except ImportError:
        context = "[Standard context block not available — run context_builder.py separately]"

    # Prepend weekly audit alert if due
    header_alerts = []
    if cee_mode and is_weekly_audit_due():
        utc_now = datetime.datetime.utcnow()
        ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
        header_alerts.append(get_audit_trigger_message(ist_now))

    # Append CEE section
    cee_section = build_cee_section() if cee_mode else ""

    # Assemble output
    output_parts = []
    if header_alerts:
        output_parts.append("\n" + "!" * 60)
        for alert in header_alerts:
            output_parts.append(alert)
        output_parts.append("!" * 60 + "\n")
    output_parts.append(context)
    if cee_section:
        output_parts.append(cee_section)

    final_output = "\n".join(output_parts)
    print(final_output)

    # Clipboard support
    if "--copy" in sys.argv:
        try:
            import pyperclip
            pyperclip.copy(final_output)
            print("\n[Copied to clipboard]", file=sys.stderr)
        except ImportError:
            print("\n[Install pyperclip for clipboard: pip install pyperclip]", file=sys.stderr)

    # Log
    log_path = BASE / "logs" / "sessions.log"
    log_path.parent.mkdir(exist_ok=True)
    today = datetime.date.today().isoformat()
    mode_label = "cee+standard" if cee_mode else "standard"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{today}] cee_context_builder ran [{mode_label}] — ~{len(final_output)//4} tokens\n")


if __name__ == "__main__":
    main()
