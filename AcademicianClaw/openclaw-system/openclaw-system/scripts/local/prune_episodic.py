#!/usr/bin/env python3
"""prune_episodic.py — Archives old entries in memory/episodic/recent.md. Zero LLM calls."""
import re, datetime, sys
from pathlib import Path

BASE = Path(__file__).parent.parent.parent

PRUNE_THRESHOLD = 500   # lines
ARCHIVE_LINES   = 200   # lines to move to archive
KEEP_LINES      = 300   # lines to keep in recent.md

class C:
    G="\033[92m"; Y="\033[93m"; O="\033[38;5;208m"; D="\033[2m"; B="\033[1m"; END="\033[0m"

def read(rel, default=""):
    p = BASE / rel
    return p.read_text(encoding="utf-8") if p.exists() else default

def write(rel, content):
    p = BASE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def append_to(rel, text):
    p = BASE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(text)

def main():
    recent_path = BASE / "memory/episodic/recent.md"
    if not recent_path.exists():
        print("  No episodic/recent.md found.")
        return

    content = recent_path.read_text(encoding="utf-8")
    lines   = content.split("\n")
    total   = len(lines)

    print(f"\n  {C.O}{C.B}🗂  Episodic Memory Manager{C.END}")
    print(f"  {C.D}recent.md: {total} lines (threshold: {PRUNE_THRESHOLD}){C.END}\n")

    if total < PRUNE_THRESHOLD:
        print(f"  {C.G}✓ No pruning needed.{C.END} ({PRUNE_THRESHOLD - total} lines before threshold)\n")
        return

    # Split entries by heading
    header_lines = []
    entries = []
    in_header = True
    current_entry = []

    for line in lines:
        if re.match(r"^## \[", line):
            in_header = False
            if current_entry:
                entries.append("\n".join(current_entry))
            current_entry = [line]
        elif in_header:
            header_lines.append(line)
        else:
            current_entry.append(line)

    if current_entry:
        entries.append("\n".join(current_entry))

    total_entries = len(entries)
    archive_count = max(1, total_entries // 3)  # archive oldest third
    to_archive = entries[:archive_count]
    to_keep    = entries[archive_count:]

    # Determine archive file name
    archive_month = datetime.date.today().strftime("%Y-%m")
    archive_path  = f"memory/episodic/{archive_month}.md"

    # Check if archive already exists (append) or create new
    existing_archive = read(archive_path, "")
    if not existing_archive:
        archive_header = f"# Episodic Archive — {archive_month}\n_Archived from recent.md_\n\n"
    else:
        archive_header = existing_archive

    archive_content = archive_header + "\n\n".join(to_archive) + "\n"
    write(archive_path, archive_content)

    # Rebuild recent.md
    header_text  = "\n".join(header_lines)
    recent_new   = header_text + "\n\n" + "\n\n".join(to_keep) + "\n"
    write("memory/episodic/recent.md", recent_new)

    new_line_count = len(recent_new.split("\n"))

    # Log
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    append_to("logs/memory-changes.log",
              f"[{ts}] PRUNE: moved {archive_count} entries to {archive_path} | recent.md now {new_line_count} lines\n")

    print(f"  {C.G}✓ Archived{C.END} {archive_count} entries → {archive_path}")
    print(f"  {C.G}✓ recent.md{C.END} reduced to {new_line_count} lines")
    print(f"  {C.D}Log updated: logs/memory-changes.log{C.END}\n")

if __name__ == "__main__":
    main()
