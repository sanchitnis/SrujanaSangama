#!/usr/bin/env python3
"""
openclaw-script: true
name: init
description: First-run interactive interview. Writes soul.md and all memory
             template files. NO LLM API calls — pure input() and file writes.
permissions: write
created: 2026-05-07
"""

import os, sys, datetime
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import BASE, WORKSPACE_ROOT, resolve_path


class C:
    ORANGE="\033[38;5;208m"; GREEN="\033[92m"; CYAN="\033[96m"
    DIM="\033[2m"; BOLD="\033[1m"; END="\033[0m"; YELLOW="\033[93m"

def ask(prompt, default=None):
    d = f" {C.DIM}(default: {default}){C.END}" if default else ""
    answer = input(f"  {C.CYAN}{prompt}{C.END}{d}\n  → ").strip()
    return answer if answer else (default or "")

def ask_list(prompt):
    print(f"  {C.CYAN}{prompt}{C.END} {C.DIM}(comma-separated){C.END}")
    answer = input("  → ").strip()
    return [x.strip() for x in answer.split(",") if x.strip()]

def section(title):
    print(f"\n  {C.ORANGE}{C.BOLD}{title}{C.END}")
    print(f"  {C.DIM}{'─'*50}{C.END}\n")

def write(rel, content):
    p = resolve_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def main():
    os.system("clear" if os.name=="posix" else "cls")
    print(f"\n  {C.ORANGE}{C.BOLD}🦅 OpenClaw — First Run Setup{C.END}")
    print(f"  {C.DIM}No LLM API calls. Pure file setup.{C.END}\n")

    section("1 / 5 — Identity")
    name     = ask("Your name", "User")
    role     = ask("Your role / title")
    org      = ask("Organisation")
    location = ask("Location (city, country)", "Bengaluru, India")
    timezone = ask("Timezone", "Asia/Kolkata")
    language = ask("Primary language", "English")

    section("2 / 5 — Goals & Values")
    values   = ask_list("Core values (2–3)")
    goal_1y  = ask("Most important goal this year")
    goal_5y  = ask("Where do you want to be in 3–5 years?")

    section("3 / 5 — Expertise")
    deep     = ask_list("Areas of deep expertise")
    working  = ask_list("Working knowledge areas")
    learning = ask_list("Currently learning")
    langs    = ask_list("Programming languages you use")
    tools    = ask_list("Tools & platforms you use regularly")
    project  = ask("Current main project or focus")

    section("4 / 5 — Style")
    tone     = ask("Preferred tone", "warm-professional")
    length   = ask("Response length preference (concise/moderate/detailed)", "moderate")
    fmt      = ask("Format preference (prose/structured/bullets)", "structured")

    section("5 / 5 — AI Preferences")
    trust    = ask("Trust level for autonomous actions (low/medium/high)", "medium")
    proact   = ask("Proactivity level (reactive/occasional/proactive)", "occasional")

    today = datetime.date.today().isoformat()

    # ── Write soul.md ─────────────────────────────────────────────────────────
    values_md   = "\n- ".join(values) if values else "[to be filled]"
    deep_md     = "\n  - ".join(deep) if deep else "[to be filled]"
    working_md  = "\n  - ".join(working) if working else "[to be filled]"
    learning_md = "\n  - ".join(learning) if learning else "[to be filled]"

    soul = f"""# Soul Profile
_Created: {today} | Last updated: {today}_

---

## Identity
- **Name**: {name}
- **Role / Title**: {role}
- **Organisation**: {org}
- **Location**: {location}
- **Timezone**: {timezone}
- **Primary Language**: {language}

---

## Core Values
- {values_md}

---

## Long-Term Goals
- **This year (12 months)**: {goal_1y}
- **Medium term (3–5 years)**: {goal_5y}

---

## Personality & Communication Style
- **Tone**: {tone}
- **Response length**: {length}
- **Format preference**: {fmt}

---

## Expertise Map
- **Deep expertise**:
  - {deep_md}
- **Working knowledge**:
  - {working_md}
- **Currently learning**:
  - {learning_md}

---

## AI Interaction Preferences
- **Trust level**: {trust}
- **Proactivity**: {proact}

---

## Inferred Preferences
_[Auto-populated by Memory Steward over time]_
-

## Deprecated Facts
_[Soft-deleted facts — never hard-deleted]_
-
"""
    write("memory/soul.md", soul)

    # ── Write semantic/work.md ────────────────────────────────────────────────
    tools_md = ", ".join(tools) if tools else "[to be filled]"
    langs_md = ", ".join(langs) if langs else "[to be filled]"
    write("memory/semantic/work.md", f"""# Work Context
_Created: {today} | Last updated: {today}_

---

## Current Role
- {role} at {org}

## Organisation
- Name: {org}
- Location: {location}

## Active Projects
- {project or '[to be filled]'}

## Key Colleagues
- [to be populated from conversations]

## Tools & Platforms
- {tools_md}

## Programming Languages
- {langs_md}

## Ongoing Challenges
- [to be populated from conversations]
""")

    # ── Write procedural/writing-style.md ────────────────────────────────────
    write("memory/procedural/writing-style.md", f"""# Writing Style Preferences
_Created: {today} | Last updated: {today}_

---

## Tone
- General: {tone}

## Format
- Preferred structure: {fmt}
- Response length: {length}
- Use bullet points: sparingly, prefer prose
- Use headings: yes, for documents >400 words
- Code blocks: always for any code or commands

## Special Rules
- [populated from explicit user instructions over time]

## Patterns from Edits
_[Auto-populated when 3+ consistent edits detected]_
-
""")

    # ── Write procedural/code-style.md ───────────────────────────────────────
    write("memory/procedural/code-style.md", f"""# Code Style Preferences
_Created: {today} | Last updated: {today}_

---

## Primary Languages
- {langs_md}

## Conventions
- Indentation: 4 spaces (Python) / 2 spaces (JS)
- Naming: snake_case (Python) / camelCase (JS)
- Type hints: always in Python 3.10+
- Docstrings: Google style
- Error handling: exceptions with descriptive messages

## Anti-Patterns to Avoid
- Hardcoded secrets or credentials
- Bare except clauses
- SQL string concatenation

## Patterns from Interactions
-
""")

    # ── Write procedural/decision-patterns.md ────────────────────────────────
    write("memory/procedural/decision-patterns.md", f"""# Decision Patterns
_Created: {today} | Last updated: {today}_

---

## Decision Style
- Primary: [to be populated]
- Risk tolerance: [to be populated]

## What Convinces This User
- [to be populated from observations]

## Patterns Observed
-

## Significant Decisions Log
| Decision | Date | Chosen | Rationale |
|----------|------|--------|-----------|
""")

    # ── Write procedural/relationship.md ─────────────────────────────────────
    write("memory/procedural/relationship.md", f"""# Relationship Arc
_Created: {today} | Last updated: {today}_

---

## History
- Started: {today}
- Total sessions: 0
- Total turns: 0

## Current Rapport Level
new

## Evolution Log
| Date | Change | Trigger |
|------|--------|---------|

## Observed Style Drift
-
""")

    # ── Context files ─────────────────────────────────────────────────────────
    write("context/tasks.md", f"""# Task List
_Last updated: {today}_

## 🔴 P1 — Critical / Due Soon
[none]

## 🟡 P2 — Important
[none]

## 🟢 P3 — Nice to Have
[none]

## ✅ Completed (last 7 days)
[none]

## 🚫 Blocked
[none]
""")

    write("context/active-project.md", f"""# Active Project
_Last updated: {today}_

## Project Name
{project or '[none set]'}

## Goal
[to be filled]

## Constraints
[to be filled]

## Key Decisions Made
[none yet]

## Open Questions
[none yet]
""")

    write("context/current-session.md", f"""# Current Session
_Started: {today}_

## Focus
[OpenClaw initialisation — ready for first real session]

## In Progress
[none]

## Parked
[none]
""")

    write("context/scratchpad.md", "# Scratchpad\n_Cleared each session_\n\n")

    # ── Memory stubs (written to WORKSPACE_ROOT/memory/ — never inside the plugin) ──
    for rel, content in [
        ("memory/episodic/recent.md",
         f"# Episodic Memory — Recent\n_Managed by update_memory.py_\n\n## [{today}] — Initialisation\nSystem initialised for {name} at {org}.\n"),
        ("memory/semantic/work.md",
         f"# Work Context\n_Created: {today} | Last updated: {today}_\n\n---\n\n## Current Role\n- {role} at {org}\n\n## Organisation\n- Name: {org}\n- Location: {location}\n\n## Active Projects\n- [to be filled from conversations]\n\n## Key Colleagues\n- [to be populated from conversations]\n\n## Tools & Platforms\n- [to be filled]\n\n## Ongoing Challenges\n- [to be filled]\n"),
        ("memory/semantic/preferences.md",
         "# Preferences\n_Last updated: [YYYY-MM-DD]_\n\n## Tools\n-\n\n## Work Preferences\n-\n\n## Personal\n-\n"),
        ("memory/semantic/vocabulary.md",
         "# Vocabulary\n_Last updated: [YYYY-MM-DD]_\n\n## Domain Terms\n| Term | Meaning | Context |\n|------|---------|---------|\n\n## Acronyms\n| Acronym | Expansion |\n|---------|-----------|\n"),
        ("memory/semantic/relationships.md",
         "# Relationships\n_Last updated: [YYYY-MM-DD]_\n\n## Direct Reports\n| Name | Role | Notes |\n|------|------|-------|\n\n## Peers\n| Name | Org | Notes |\n|------|-----|-------|\n"),
        ("memory/semantic/ideas.md",
         "# Ideas Archive\n_Last updated: [YYYY-MM-DD]_\n\n## Active\n\n## Parked\n\n## Discarded\n"),
        ("memory/semantic/learning.md",
         "# Learning Journal\n_Last updated: [YYYY-MM-DD]_\n\n## Active Goals\n\n## Spaced Repetition\n| Concept | Learned | Next Review |\n|---------|---------|-------------|\n\n## Session Log\n"),
        ("memory/habits/habits.md",
         "# Habit Tracker\n_Last updated: [YYYY-MM-DD]_\n\n## Active Habits\n\n## Weekly Log\n\n## Retired\n"),
    ]:
        write(rel, content)

    # ── Log files ─────────────────────────────────────────────────────────────
    write("logs/sessions.log",   f"[{today}] OpenClaw initialised for {name}\n")
    write("logs/memory-changes.log", f"[{today}] System initialised — soul.md and all templates written\n")

    # ── CEE memory files ──────────────────────────────────────────────────────
    # Copy .example files to live CEE memory files (gitignored).
    # Destination paths mirror the cognitive memory hierarchy:
    #   context/  — active working state (projects, holding inbox)
    #   semantic/ — domain knowledge (areas, resources, identity)
    #   archive/  — closed work
    #   logs/     — execution history
    cee_examples = [
        # context/ — active, time-bound, actionable
        ("context/para-projects.md",          BASE / "context/para-projects.md.example"),
        ("context/holding-inbox.md",          BASE / "context/holding-inbox.md.example"),
        # semantic/ — ongoing knowledge and domain accountability
        ("memory/semantic/cee-identity.md",   BASE / "memory/semantic/cee-identity.md.example"),
        ("memory/semantic/para-areas.md",     BASE / "memory/semantic/para-areas.md.example"),
        ("memory/semantic/para-resources.md", BASE / "memory/semantic/para-resources.md.example"),
        # archive/ — closed projects and records
        ("memory/archive/para-archive.md",    BASE / "memory/archive/para-archive.md.example"),
    ]
    for rel, example_path in cee_examples:
        target = resolve_path(rel)
        if not target.exists() and example_path.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(example_path.read_text(encoding="utf-8"), encoding="utf-8")

    # logs/ — mechanical execution history
    termite_example = BASE / "memory" / "logs" / "termite-history.md.example"
    termite_live    = resolve_path("memory/logs/termite-history.md")
    if not termite_live.exists() and termite_example.exists():
        termite_live.parent.mkdir(parents=True, exist_ok=True)
        termite_live.write_text(termite_example.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"\n  {C.GREEN}{C.BOLD}✅ OpenClaw initialised for {name}{C.END}")
    print(f"\n  {C.DIM}Next steps:{C.END}")
    print(f"  1. Run:  {C.CYAN}python3 scripts/health.py{C.END}")
    print(f"  2. Run:  {C.CYAN}python3 scripts/context_builder.py{C.END}")
    print(f"  3. Paste {C.CYAN}rules/ORCHESTRATOR.md{C.END} + context into Claude\n")
    print(f"  {C.ORANGE}{C.BOLD}📋 CEE Engine — Morning Briefing Setup:{C.END}")
    print(f"  {C.DIM}Set up your daily 6 AM briefing via Gemini /schedule:{C.END}")
    print(f"  1. Open Gemini")
    print(f"  2. Type {C.CYAN}/schedule{C.END}")
    print(f"  3. Set frequency: {C.CYAN}Daily{C.END} | Time: {C.CYAN}6:00 AM IST{C.END}")
    print(f"  4. Paste contents of {C.CYAN}workflows/07_morning-briefing.md{C.END} as the prompt body")
    print(f"  5. Gemini will fire your Morning Briefing every day automatically.\n")
    print(f"  {C.DIM}To migrate your existing tasks to the enriched CEE format:{C.END}")
    print(f"  Run: {C.CYAN}python3 scripts/cee_task_migrate.py{C.END}\n")

if __name__ == "__main__":
    main()
