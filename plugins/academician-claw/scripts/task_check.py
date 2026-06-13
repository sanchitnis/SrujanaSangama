#!/usr/bin/env python3
"""task_check.py — Print overdue and due-today tasks from context/tasks.md. Zero LLM calls."""
import re, datetime, sys
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import BASE, WORKSPACE_ROOT, resolve_path


class C:
    R="\033[91m"; Y="\033[93m"; G="\033[92m"; O="\033[38;5;208m"
    D="\033[2m"; B="\033[1m"; END="\033[0m"

def main():
    tasks_path = resolve_path("context/tasks.md")
    if not tasks_path.exists():
        print("  No tasks.md found. Run init.py first.")
        return

    content = tasks_path.read_text(encoding="utf-8")
    today = datetime.date.today()
    today_str = today.isoformat()

    overdue, due_today, due_week, all_open = [], [], [], []

    for line in content.split("\n"):
        if not line.strip().startswith("- [ ]"):
            continue
        all_open.append(line)
        m = re.search(r"Due:\s*(\d{4}-\d{2}-\d{2})", line)
        task_text = re.sub(r"\|.*", "", line.replace("- [ ]", "")).strip()
        if m:
            try:
                due = datetime.date.fromisoformat(m.group(1))
                delta = (due - today).days
                if delta < 0:
                    overdue.append((task_text, m.group(1), delta))
                elif delta == 0:
                    due_today.append((task_text, m.group(1)))
                elif delta <= 7:
                    due_week.append((task_text, m.group(1), delta))
            except ValueError:
                pass

    print(f"\n  {C.O}{C.B}📋 Task Check — {today_str}{C.END}\n")

    if overdue:
        print(f"  {C.R}{C.B}⚠ OVERDUE ({len(overdue)}){C.END}")
        for text, date, delta in sorted(overdue, key=lambda x: x[2]):
            print(f"    {C.R}• {text}{C.END}  {C.D}(due {date}, {abs(delta)}d ago){C.END}")
        print()

    if due_today:
        print(f"  {C.Y}{C.B}📅 DUE TODAY ({len(due_today)}){C.END}")
        for text, date in due_today:
            print(f"    {C.Y}• {text}{C.END}")
        print()

    if due_week:
        print(f"  {C.G}📆 THIS WEEK ({len(due_week)}){C.END}")
        for text, date, delta in sorted(due_week, key=lambda x: x[2]):
            print(f"    • {text}  {C.D}(due {date}, in {delta}d){C.END}")
        print()

    if not overdue and not due_today and not due_week:
        print(f"  {C.G}✓ No overdue or upcoming tasks in the next 7 days.{C.END}")

    print(f"  {C.D}Total open tasks: {len(all_open)}{C.END}\n")

if __name__ == "__main__":
    main()
