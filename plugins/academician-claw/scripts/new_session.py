#!/usr/bin/env python3
"""new_session.py — Resets current-session.md and prints a session start summary. Zero LLM calls."""
import re, datetime, sys
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import BASE, WORKSPACE_ROOT, resolve_path


class C:
    O="\033[38;5;208m"; G="\033[92m"; Y="\033[93m"; C="\033[96m"
    D="\033[2m"; B="\033[1m"; END="\033[0m"

def read(rel, default=""):
    p = resolve_path(rel)
    return p.read_text(encoding="utf-8") if p.exists() else default

def write(rel, content):
    p = resolve_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def append_to(rel, text):
    p = resolve_path(rel)
    with open(p, "a", encoding="utf-8") as f:
        f.write(text)

def get_overdue_tasks(tasks_content):
    today = datetime.date.today()
    overdue, due_today = [], []
    for line in tasks_content.split("\n"):
        if "- [ ]" not in line:
            continue
        m = re.search(r"Due:\s*(\d{4}-\d{2}-\d{2})", line)
        text = re.sub(r"\|.*", "", line.replace("- [ ]", "")).strip()
        if m:
            try:
                due = datetime.date.fromisoformat(m.group(1))
                delta = (due - today).days
                if delta < 0:
                    overdue.append((text, m.group(1), abs(delta)))
                elif delta == 0:
                    due_today.append((text,))
            except ValueError:
                pass
    return overdue, due_today

def get_habit_nudges(habits_content):
    """Find habits not yet logged today."""
    today = datetime.date.today().isoformat()
    nudges = []
    for line in habits_content.split("\n"):
        lm = re.match(r"-\s+\*\*Last completed\*\*:\s*(\S+)", line)
        if lm and lm.group(1) != today and lm.group(1) != "never":
            # find the habit name (it's in a ### heading above)
            pass  # simplified — just count active habits not done today
    return nudges

def main():
    today     = datetime.date.today().isoformat()
    now       = datetime.datetime.now().strftime("%H:%M")
    tasks     = read("context/tasks.md")
    habits    = read("memory/habits/habits.md")
    soul      = read("memory/soul.md")
    prev_sess = read("context/current-session.md")

    # Extract name
    name_m = re.search(r"\*\*Name\*\*:\s*(.+)", soul)
    name = name_m.group(1).strip() if name_m else "User"

    # Extract carried-over threads from previous session
    carry_m = re.search(r"## Carried Over.*?\n([\s\S]+?)(?=\n##|\Z)", prev_sess)
    carried = carry_m.group(1).strip() if carry_m else ""

    # Task alerts
    overdue, due_today = get_overdue_tasks(tasks)

    # ── Print session summary ─────────────────────────────────────────────────
    print(f"\n  {C.O}{C.B}🦅 OpenClaw — New Session{C.END}")
    print(f"  {C.D}{today}  {now}  ·  Hello, {name}{C.END}\n")

    if overdue:
        print(f"  {C.Y}⚠ OVERDUE:{C.END}")
        for text, date, days in overdue[:3]:
            print(f"    • {text}  {C.D}({days}d overdue){C.END}")

    if due_today:
        print(f"  {C.G}📅 DUE TODAY:{C.END}")
        for (text,) in due_today[:3]:
            print(f"    • {text}")

    if carried and "[none]" not in carried:
        print(f"\n  {C.C}Carried over from last session:{C.END}")
        for line in carried.split("\n")[:3]:
            if line.strip().startswith("- "):
                print(f"    {line.strip()}")

    print(f"\n  {C.D}Steps:{C.END}")
    print(f"  1. python3 scripts/local/context_builder.py  (--copy to clipboard)")
    print(f"  2. Open Claude → paste prompts/session/ORCHESTRATOR.md + context block")
    print(f"  3. Work. End with prompts/session/SESSION_CLOSER.md")
    print(f"  4. python3 scripts/local/update_memory.py\n")

    # ── Reset current-session.md ──────────────────────────────────────────────
    new_session = f"""# Current Session
_Started: {today} {now}_

## Focus
[Set when conversation begins]

## In Progress
[none]

## Parked
[none]

## Notes
[none]
"""
    write("context/current-session.md", new_session)
    write("context/scratchpad.md", f"# Scratchpad\n_{today}_\n\n")

    # Log session start
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    append_to("logs/sessions.log", f"[{ts}] SESSION START — {name}\n")

    print(f"  {C.D}current-session.md and scratchpad.md reset.{C.END}\n")

if __name__ == "__main__":
    main()
