#!/usr/bin/env python3
"""
openclaw-script: true
name: cee_task_migrate
description: One-time migration utility. Reads context/tasks.md in flat P1/P2/P3
             format and converts it to the enriched CEE table format. Pre-fills:
             priority (from heading), status (todo), description (from task text).
             All other columns are set to [to fill]. Creates a backup at
             context/tasks.md.bak before writing. Safe to re-run (idempotent).
permissions: write
created: 2026-06-11
"""

import datetime
import re
import shutil
from pathlib import Path

# Ensure UTF-8 output on Windows
import sys
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import BASE, WORKSPACE_ROOT, resolve_path
TASKS_PATH = resolve_path("context/tasks.md")



TABLE_HEADER = """\
# Task List — CEE Enriched Format
_Last updated: {date}_

> **Format:** Each row is one task. Fill all columns. Use `[to fill]` as placeholder.
> **Alignment column:** Reference CO-1 (Core Objective 1) and R1/R2/R3 (Leadership Roles) from cee-identity.md.
> **Tags:** #deep-work | #quick-review | #dependency-block | #async-delegate

| Task | Category / Project | Priority | Est. Time | Scheduled Date | Status | Description | Alignment | Tags |
|------|--------------------|----------|-----------|----------------|--------|-------------|-----------|------|
"""

COMPLETED_HEADER = """
---

## ✅ Completed (last 14 days)

| Task | Category / Project | Completed Date | Alignment |
|------|--------------------|----------------|-----------|
"""

PRIORITY_MAP = {
    "P1": "🔴 P1",
    "P2": "🟡 P2",
    "P3": "🟢 P3",
}


def is_already_table_format(content):
    """Check if tasks.md already has the enriched table format."""
    return "Category / Project" in content and "Est. Time" in content


def parse_flat_tasks(content):
    """Parse flat P1/P2/P3 task list and return list of (priority, text, status, due) tuples."""
    tasks = []
    completed = []
    current_priority = "P2"
    in_completed = False
    in_blocked = False

    for line in content.split("\n"):
        line = line.strip()

        # Detect section headings
        if "P1" in line and line.startswith("#"):
            current_priority = "P1"
            in_completed = False
            in_blocked = False
            continue
        elif "P2" in line and line.startswith("#"):
            current_priority = "P2"
            in_completed = False
            in_blocked = False
            continue
        elif "P3" in line and line.startswith("#"):
            current_priority = "P3"
            in_completed = False
            in_blocked = False
            continue
        elif "✅" in line and line.startswith("#"):
            in_completed = True
            in_blocked = False
            continue
        elif "🚫" in line and line.startswith("#"):
            in_blocked = True
            in_completed = False
            continue

        # Parse task lines
        if in_completed and line.startswith("- [x]"):
            text = line[5:].strip()
            # Extract completion date if present
            date_match = re.search(r"Completed:\s*(\d{4}-\d{2}-\d{2})", text)
            comp_date = date_match.group(1) if date_match else datetime.date.today().isoformat()
            text = re.sub(r"\|.*", "", text).strip()
            completed.append((text, comp_date))

        elif not in_completed and (line.startswith("- [ ]") or line.startswith("- [/]")):
            status = "in-progress" if "[/]" in line else ("blocked" if in_blocked else "todo")
            text_raw = re.sub(r"^- \[.\]\s*", "", line).strip()

            # Extract due date
            due_match = re.search(r"Due:\s*(\d{4}-\d{2}-\d{2})", text_raw)
            due_date  = due_match.group(1) if due_match else "[to fill]"

            # Extract project tag
            proj_match = re.search(r"Project:\s*([^\|]+)", text_raw)
            project = proj_match.group(1).strip() if proj_match else "[to fill]"

            # Clean title
            title = re.sub(r"\|.*", "", text_raw).strip()

            tasks.append({
                "title": title,
                "priority": PRIORITY_MAP.get(current_priority, "🟡 P2"),
                "status": status,
                "due": due_date,
                "project": project,
            })

    return tasks, completed


def format_task_row(t):
    return (
        f"| {t['title']} "
        f"| {t['project']} "
        f"| {t['priority']} "
        f"| [to fill] "
        f"| {t['due']} "
        f"| {t['status']} "
        f"| [to fill] "
        f"| [to fill] "
        f"| [to fill] |"
    )


def format_completed_row(text, comp_date):
    return f"| {text} | [to fill] | {comp_date} | [to fill] |"


def migrate():
    print("\n🔄 CEE Task Format Migration\n")

    if not TASKS_PATH.exists():
        print(f"❌ tasks.md not found at: {TASKS_PATH}")
        print("   Run init.py first to create it.")
        return

    content = TASKS_PATH.read_text(encoding="utf-8")

    if is_already_table_format(content):
        print("✅ tasks.md is already in enriched table format. Nothing to migrate.")
        return

    print(f"📄 Found flat-format tasks.md")

    # Create backup
    bak_path = TASKS_PATH.with_suffix(".md.bak")
    shutil.copy2(TASKS_PATH, bak_path)
    print(f"💾 Backup saved: {bak_path}")

    # Parse
    tasks, completed = parse_flat_tasks(content)
    print(f"   → Found {len(tasks)} active task(s), {len(completed)} completed task(s)")

    # Build new content
    today = datetime.date.today().isoformat()
    new_content = TABLE_HEADER.format(date=today)

    if tasks:
        for t in tasks:
            new_content += format_task_row(t) + "\n"
    else:
        new_content += "| [No active tasks] | — | — | — | — | — | — | — | — |\n"

    new_content += COMPLETED_HEADER

    if completed:
        for text, comp_date in completed:
            new_content += format_completed_row(text, comp_date) + "\n"
    else:
        new_content += "| [No completed tasks this period] | — | — | — |\n"

    # Write
    TASKS_PATH.write_text(new_content, encoding="utf-8")
    print(f"\n✅ Migration complete!")
    print(f"   tasks.md updated with enriched table format.")
    print(f"   Backup preserved at: {bak_path}")
    print(f"\n📝 Next step: Open tasks.md and fill in [to fill] columns:")
    print(f"   → Category / Project: which PARA project or area?")
    print(f"   → Est. Time: 30m, 2h, half-day?")
    print(f"   → Description: what does 'done' look like?")
    print(f"   → Alignment: which Core Objective + which Role? (from cee-identity.md)")
    print(f"   → Tags: #deep-work / #quick-review / #dependency-block / #async-delegate")


if __name__ == "__main__":
    migrate()
