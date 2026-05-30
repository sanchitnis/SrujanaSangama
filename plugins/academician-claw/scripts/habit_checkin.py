#!/usr/bin/env python3
"""habit_checkin.py — CLI habit check-in. Updates streaks in memory/habits/habits.md. Zero LLM calls."""
import re, datetime, sys
from pathlib import Path

BASE = Path(__file__).parent.parent  # plugin root

class C:
    G="\033[92m"; R="\033[91m"; Y="\033[93m"; O="\033[38;5;208m"
    C="\033[96m"; D="\033[2m"; B="\033[1m"; END="\033[0m"

def read(rel):
    p = BASE / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""

def write(rel, content):
    p = BASE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def append_to(rel, text):
    p = BASE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(text)

def parse_habits(content):
    """Return list of (name, frequency, streak, last_completed) tuples."""
    habits = []
    current = None
    for line in content.split("\n"):
        m = re.match(r"^### (.+)$", line)
        if m:
            current = {"name": m.group(1).strip(), "frequency": "daily",
                       "streak": 0, "last_completed": "never", "total": 0}
        if current:
            fm = re.match(r"-\s+\*\*Frequency\*\*:\s*(.+)", line)
            if fm: current["frequency"] = fm.group(1).strip()
            sm = re.match(r"-\s+\*\*Streak\*\*:\s*(\d+)", line)
            if sm: current["streak"] = int(sm.group(1))
            lm = re.match(r"-\s+\*\*Last completed\*\*:\s*(.+)", line)
            if lm: current["last_completed"] = lm.group(1).strip()
            tm = re.match(r"-\s+\*\*Total completions\*\*:\s*(\d+)", line)
            if tm: current["total"] = int(tm.group(1))
            # Detect end of habit block
            if line.strip() == "" and current.get("name"):
                habits.append(current)
                current = None
    if current and current.get("name"):
        habits.append(current)
    return habits

def update_habit_in_content(content, name, done, today):
    """Update streak and last_completed for a habit in the file content."""
    # Update streak
    def update_streak(m):
        current_streak = int(m.group(2))
        new_streak = current_streak + 1 if done else 0
        return m.group(1) + str(new_streak) + " days"

    pattern = rf"(### {re.escape(name)}\n[\s\S]*?- \*\*Streak\*\*: )(\d+)( days)"
    content = re.sub(pattern, update_streak, content)

    # Update last completed
    if done:
        pattern2 = rf"(### {re.escape(name)}\n[\s\S]*?- \*\*Last completed\*\*: )(\S+)"
        content = re.sub(pattern2, rf"\g<1>{today}", content)

    # Update total completions
    if done:
        def inc_total(m):
            return m.group(1) + str(int(m.group(2)) + 1)
        pattern3 = rf"(### {re.escape(name)}\n[\s\S]*?- \*\*Total completions\*\*: )(\d+)"
        content = re.sub(pattern3, inc_total, content)

    return content

def is_milestone(streak):
    return streak in (7, 14, 30, 60, 100, 200, 365)

def main():
    today = datetime.date.today().isoformat()
    content = read("memory/habits/habits.md")

    if not content or "## Active Habits" not in content:
        print(f"\n  {C.Y}No habits tracked yet.{C.END}")
        print(f"  Start tracking a habit by telling Claude (Habit Tracker agent):")
        print(f"  {C.D}\"Add habit: [name], daily\"{C.END}\n")
        return

    habits = parse_habits(content.split("## Active Habits")[1].split("## ")[0] if "## Active Habits" in content else "")

    if not habits:
        print(f"\n  {C.D}No active habits found in habits.md.{C.END}\n")
        return

    print(f"\n  {C.O}{C.B}✅ Habit Check-In — {today}{C.END}\n")
    print(f"  {C.D}Current streaks:{C.END}")
    for i, h in enumerate(habits):
        streak_info = f"{h['streak']}d streak"
        last = f"last: {h['last_completed']}" if h['last_completed'] != "never" else "not started"
        print(f"  {C.C}{i+1}.{C.END} {h['name']}  {C.D}({streak_info} · {last}){C.END}")

    print(f"\n  {C.D}Enter habit number(s) completed today, comma-separated.")
    print(f"  Press Enter with no input to skip. Type 'miss N' to log a miss.{C.END}")
    raw = input("  → ").strip()

    if not raw:
        print(f"  {C.D}No check-ins recorded.{C.END}\n")
        return

    # Parse input: "1, 3, miss 2"
    done_indices = []
    missed_indices = []
    for part in raw.split(","):
        part = part.strip()
        if part.lower().startswith("miss"):
            nums = re.findall(r"\d+", part)
            missed_indices.extend(int(n) - 1 for n in nums if 0 < int(n) <= len(habits))
        else:
            nums = re.findall(r"\d+", part)
            done_indices.extend(int(n) - 1 for n in nums if 0 < int(n) <= len(habits))

    updated_content = content
    log_lines = []

    for idx in done_indices:
        h = habits[idx]
        updated_content = update_habit_in_content(updated_content, h["name"], True, today)
        new_streak = h["streak"] + 1
        milestone = f"  🔥 {new_streak}-day milestone!" if is_milestone(new_streak) else ""
        print(f"  {C.G}✅ {h['name']}{C.END} — {new_streak}-day streak{milestone}")
        log_lines.append(f"| {today} | {h['name']} | ✅ |")

    for idx in missed_indices:
        h = habits[idx]
        updated_content = update_habit_in_content(updated_content, h["name"], False, today)
        print(f"  {C.R}❌ {h['name']}{C.END} — streak reset. Back at it tomorrow.")
        log_lines.append(f"| {today} | {h['name']} | ❌ |")

    write("memory/habits/habits.md", updated_content)

    # Append to weekly log section
    if log_lines:
        log_block = "\n" + "\n".join(log_lines) + "\n"
        if "## Weekly Log" in updated_content:
            final = updated_content.replace("## Weekly Log\n", "## Weekly Log\n" + log_block)
            write("memory/habits/habits.md", final)

    # Append to memory changes log
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    for line in log_lines:
        append_to("logs/memory-changes.log", f"[{ts}] HABIT: {line}\n")

    print(f"\n  {C.D}habits.md updated. Changes logged.{C.END}\n")

if __name__ == "__main__":
    main()
