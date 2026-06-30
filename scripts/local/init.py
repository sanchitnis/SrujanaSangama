#!/usr/bin/env python3
"""
SrujanaSangama: Setup & Workspace Initialisation Script
Description: Scaffolds the full srujana-memory/ folder structure and populates
             soul.md and default templates based on an interactive interview.
Permissions: write
"""

import os
import sys
import datetime
import json
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

import path_resolver
from path_resolver import get_srujana_memory_dir, resolve_path

class C:
    ORANGE = "\033[38;5;208m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    DIM = "\033[2m"
    BOLD = "\033[1m"
    END = "\033[0m"
    YELLOW = "\033[93m"
    RED = "\033[91m"

def ask(prompt, default=None):
    d = f" {C.DIM}(default: {default}){C.END}" if default else ""
    answer = input(f"  {C.CYAN}{prompt}{C.END}{d}\n  → ").strip()
    return answer if answer else (default or "")

def ask_list(prompt):
    print(f"  {C.CYAN}{prompt}{C.END} {C.DIM}(comma-separated){C.END}")
    answer = input("  → ").strip()
    return [x.strip() for x in answer.split(",") if x.strip()]

def ask_multi_select(prompt, options):
    print(f"  {C.CYAN}{prompt}{C.END} {C.DIM}(comma-separated numbers){C.END}")
    for idx, opt in enumerate(options, 1):
        print(f"    {idx}. {opt}")
    answer = input("  → ").strip()
    selected = []
    for x in answer.split(","):
        try:
            val = int(x.strip())
            if 1 <= val <= len(options):
                selected.append(options[val - 1])
        except ValueError:
            pass
    return selected

def section(title):
    print(f"\n  {C.ORANGE}{C.BOLD}{title}{C.END}")
    print(f"  {C.DIM}{'─'*50}{C.END}\n")

def write_memory_file(rel, content):
    p = resolve_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def main():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"\n  {C.ORANGE}{C.BOLD}🦅 SrujanaSangama — Onboarding Setup{C.END}")
    print(f"  {C.DIM}No LLM API calls. Scaffolding your local srujana-memory/ workspace.{C.END}\n")

    # Ensure srujana-memory parent exists
    try:
        mem_dir = get_srujana_memory_dir()
        print(f"  Target memory directory: {C.GREEN}{mem_dir}{C.END}\n")
    except SystemExit:
        # If folder doesn't exist, create it relative to sibling dir
        sibling_dir = path_resolver.WORKSPACE_ROOT.parent / "srujana-memory"
        print(f"  {C.YELLOW}Srujana memory folder not found. Creating sibling directory at:{C.END}")
        print(f"  {C.GREEN}{sibling_dir}{C.END}\n")
        sibling_dir.mkdir(parents=True, exist_ok=True)
        mem_dir = sibling_dir

    section("1 / 5 — Role Definition")
    print("  Select your primary role:")
    print("    1. Faculty Member")
    print("    2. Research Scholar (PhD)")
    print("    3. Student Researcher (UG/PG)")
    
    role_choice = ask("Enter choice (1-3)", "1")
    role_mapping = {
        "1": "Faculty Member",
        "2": "Research Scholar",
        "3": "Student Researcher"
    }
    primary_role = role_mapping.get(role_choice, "Faculty Member")
    
    additional_roles = []
    if primary_role == "Faculty Member":
        additional_roles = ask_multi_select(
            "Select any additional roles you fulfill this academic year:",
            ["PhD Supervisor", "HOD", "Dean / Centre Director", "IQAC Coordinator", "TPC Coordinator", "Admissions Team", "PI / CoPI on active grants"]
        )

    section("2 / 5 — Profile Details")
    name = ask("Your full name (with titles, e.g. Dr. Rajesh Kumar)")
    school = ask("Your School / Department (e.g. School of CSE)")
    email = ask("Your REVA email address")
    
    role_specific_data = {}
    if primary_role == "Faculty Member":
        role_specific_data["research_focus"] = ask_list("Primary research interest domains")
        role_specific_data["courses_taught"] = ask_list("Courses teaching this semester (name or course code)")
    elif primary_role == "Research Scholar":
        role_specific_data["reg_date"] = ask("Provisional Registration Date (e.g., 2025-06-01)")
        role_specific_data["reg_type"] = ask("Registration type (Full-time / Part-time)", "Full-time")
        role_specific_data["guide"] = ask("PhD Guide name")
        role_specific_data["co_guide"] = ask("PhD Co-guide name (if any)")
        role_specific_data["topic"] = ask("Proposed thesis topic")
    else:
        role_specific_data["program"] = ask("Degree program & year (e.g., B.Tech CSE 3rd Year)")
        role_specific_data["focus"] = ask("Active project or research focus")

    section("3 / 5 — Goals & Values")
    sankalpas = ask_list("Your key Sankalpas (Resolutions/committed intents) for this academic year")
    goals = ask_list("Current goals derived from your Sankalpas")
    ikigai = ask("Ikigai alignment (what you love/are good at/REVA needs)", "Learner-centric excellence and impactful research")

    section("4 / 5 — Expertise & Preferences")
    skills_list = ask_list("Key technical/academic skills")
    tools_list = ask_list("Regular tools & platforms (e.g., Python, MATLAB, LaTeX)")
    tone = ask("Preferred AI communication tone (e.g., professional, direct, coaching)", "professional")
    working_pref = ask("AI response formatting preference (e.g., structured, markdown-heavy, concise)", "structured")

    section("5 / 5 — Initializing Memory Workspace")
    print("  Creating srujana-memory folders and templates...")

    today = datetime.date.today().isoformat()

    # ── Folder Scaffolding ───────────────────────────────────────────────────
    folders = [
        "my-memory",
        "my-memory/inbox",
        "my-memory/wiki",
        "my-memory/wiki/people",
        "my-memory/wiki/concepts",
        "my-memory/wiki/courses",
        "my-memory/wiki/projects",
        "my-memory/wiki/sources",
        "my-memory/wiki/_notes",
        "my-memory/semantic",
        "my-memory/episodic",
        "my-memory/episodic/weekly-reviews",
        "my-memory/episodic/meeting-notes",
        "my-memory/episodic/decisions",
        "my-memory/context",
        "my-memory/gps",
        "my-memory/gps/gps-archive",
        "my-memory/performance",
        "my-memory/performance/monthly",
        "my-memory/performance/appraisal-evidence",
        "my-memory/wellbeing",
        "my-memory/wellbeing/reflections",
        "public-memory",
        "public-memory/publications",
        "public-memory/patents",
        "public-memory/projects",
        "public-memory/reports",
        "collaborations"
    ]

    for f in folders:
        p = mem_dir / f
        p.mkdir(parents=True, exist_ok=True)

    # Scaffolding role-specific collaborations
    if "PhD Supervisor" in additional_roles:
        (mem_dir / "collaborations/scholar-guide").mkdir(parents=True, exist_ok=True)
    if "HOD" in additional_roles:
        (mem_dir / f"collaborations/reva-hod").mkdir(parents=True, exist_ok=True)
    if "Dean / Centre Director" in additional_roles:
        (mem_dir / f"collaborations/reva-dean").mkdir(parents=True, exist_ok=True)
    if "IQAC Coordinator" in additional_roles:
        (mem_dir / "collaborations/reva-iqac").mkdir(parents=True, exist_ok=True)
    if "TPC Coordinator" in additional_roles:
        (mem_dir / "collaborations/reva-tpc").mkdir(parents=True, exist_ok=True)
    if "Admissions Team" in additional_roles:
        (mem_dir / "collaborations/reva-admissions").mkdir(parents=True, exist_ok=True)

    # ── Write my-memory/soul.md ──────────────────────────────────────────────
    sankalpas_md = "\n- ".join(sankalpas) if sankalpas else "[To be filled]"
    goals_md = "\n- ".join(goals) if goals else "[To be filled]"
    roles_list_str = ", ".join([primary_role] + additional_roles)
    
    soul_content = f"""# soul.md — {name}
_Created: {today} | Last updated: {today}_

## Who I am
* **Name**: {name}
* **Designation**: {primary_role} ({school})
* **Email**: {email}
* **Created**: {today}

## My Roles (this academic year)
* **Primary**: {primary_role}
* **Additional**: {", ".join(additional_roles) if additional_roles else "None"}

## What I teach / study (this semester)
{chr(10).join([f"* {course}" for course in role_specific_data.get("courses_taught", ["[To be filled]"])]) if primary_role == "Faculty Member" else f"* Program focus: {role_specific_data.get('program', '[To be filled]')}"}

## Research Identity
* **Domain/Focus**: {", ".join(role_specific_data.get("research_focus", ["[To be filled]"])) if primary_role == "Faculty Member" else role_specific_data.get("topic", "[To be filled]")}
* **Active projects**: {role_specific_data.get("focus", "[None set]") if primary_role == "Student Researcher" else "[None set]"}

## My Sankalpa this year
- {sankalpas_md}

## My current Goals
- {goals_md}

## Ikigai alignment
- {ikigai}

## Working preferences
* **Tone**: {tone}
* **Format**: {working_pref}
"""
    write_memory_file("my-memory/soul.md", soul_content)

    # ── Write my-memory/semantic files ───────────────────────────────────────
    write_memory_file("my-memory/semantic/profile.md", f"""# Profile Context — {name}
_Last updated: {today}_

## Base Profile
* **Title**: {name}
* **Primary Role**: {primary_role}
* **School / Department**: {school}
* **Academic Roles**: {roles_list_str}

## Qualifications
* [Enter degrees, institutions, and years]

## Professional Experience
* [Enter past academic/industry tenure details]
""")

    if primary_role == "Faculty Member":
        write_memory_file("my-memory/semantic/teaching.md", f"""# Teaching & Learning Context — {name}
_Last updated: {today}_

## Pedagogical Philosophy
* Aligned to Outcome-Based Education (OBE) and NBA compliance.
* Focus on portfolio-first active learning.

## Courses Taught
{chr(10).join([f"### {course}{chr(10)}* Module structures, Course Outcomes (COs) to be updated." for course in role_specific_data.get("courses_taught", [])])}
""")
        write_memory_file("my-memory/semantic/research.md", f"""# Research Context — {name}
_Last updated: {today}_

## Primary Domains
{chr(10).join([f"* {focus}" for focus in role_specific_data.get("research_focus", [])])}

## Active Grants & Funding Proposals
* [None set]

## Target Publications
* [Identify target Tier-1/Quartile-1 journals]
""")
    elif primary_role == "Research Scholar":
        write_memory_file("my-memory/semantic/research.md", f"""# PhD Scholar Context — {name}
_Last updated: {today}_

## Registration Details
* **Provisional Date**: {role_specific_data.get("reg_date")}
* **Type**: {role_specific_data.get("reg_type")}
* **Guide**: {role_specific_data.get("guide")}
* **Co-guide**: {role_specific_data.get("co_guide")}

## Thesis Topic
* **Topic**: {role_specific_data.get("topic")}

## Work Plan & Coursework
* [List registered coursework courses]
* [List synopsis milestones and dates]
""")

    write_memory_file("my-memory/semantic/professional.md", f"""# Professional & Admin Context — {name}
_Last updated: {today}_

## Administrative Responsibilities
{chr(10).join([f"* {role}" for role in additional_roles]) if additional_roles else "* None"}

## Committees & Board Memberships
* [List BOS, Senate, or School committees]
""")

    # ── Write public-memory/profile.md ───────────────────────────────────────
    write_memory_file("public-memory/profile.md", f"""# Public Profile (CV) — {name}
_Last updated: {today}_

## Academic Standing
* **Name**: {name}
* **Role**: {primary_role}
* **School**: {school}
* **Affiliation**: REVA University

## Publications (Q1/Q2/National)
* [List top publications]

## Patents Filed/Granted
* [List patent reference numbers]

## Active Consulting Projects
* [List active consulting agreements]
""")

    # ── Write my-memory/context files ────────────────────────────────────────
    write_memory_file("my-memory/context/this-semester.md", f"""# Semester Focus — {today}
_Academic Year: 2026-27_

## Current Teaching / Research Load
* Teaching: {", ".join(role_specific_data.get("courses_taught", ["N/A"])) if primary_role == "Faculty Member" else "N/A"}
* Research: {", ".join(role_specific_data.get("research_focus", ["N/A"])) if primary_role == "Faculty Member" else role_specific_data.get("topic", "N/A")}

## Key Deliverables (This Month)
* Complete onboarding and workspace validation
* Set goals and milestones in gps/goals-current.md
""")

    write_memory_file("my-memory/context/tasks.md", f"""# Task List
_Last updated: {today}_

## 🔴 P1 — Critical / Due Soon
- [ ] Complete onboarding verification run

## 🟡 P2 — Important
- [ ] Structure initial Obsidian Vault view from srujana-memory/my-memory

## 🟢 P3 — Nice to Have
- [ ] Connect custom skills and commands in workspace
""")

    write_memory_file("my-memory/context/active-projects.md", f"""# Active Projects
_Last updated: {today}_

## Onboarding Setup Project
* **Goal**: Establish a healthy local SrujanaSangama agentic workspace.
* **Milestone**: All templates populated and path checks passing.
""")

    # ── Write my-memory/gps files ────────────────────────────────────────────
    write_memory_file("my-memory/gps/sankalpa-current.md", f"""# Sankalpas — Committed Intents ({today})

{chr(10).join([f"- **Sankalpa**: {s}{chr(10)}  - Commited on: {today}{chr(10)}  - Status: Committed" for s in sankalpas]) if sankalpas else "- **Sankalpa**: [resolution]{chr(10)}  - Status: Draft"}
""")

    write_memory_file("my-memory/gps/goals-current.md", f"""# Goals & Action Plans ({today})

{chr(10).join([f"## Goal: {g}{chr(10)}* **Plan**: [Outline milestone steps]{chr(10)}* **Sankalpa Link**: {sankalpas[0] if sankalpas else '[None]'}{chr(10)}* **Status**: In-Progress" for g in goals]) if goals else "## Goal: [Goal]{chr(10)}* **Plan**: [Outline steps]{chr(10)}* **Status**: Draft"}
""")

    write_memory_file("my-memory/gps/habit-log.md", f"""# Daily & Weekly Habit Tracker
_Last updated: {today}_

## Habits Aligned to Goals
1. [Habit name] — [Frequency] — [Goal Link]

## Weekly Streak Log
| Week Start | Habit 1 | Energy level | Notes |
|------------|---------|--------------|-------|
""")

    # ── Write my-memory/performance and wellbeing templates ──────────────────
    write_memory_file("my-memory/performance/fdp-log.md", f"""# Faculty Development Programmes (FDP) Log
_Last updated: {today}_

| FDP Title | Date | Organised by | Skills Acquired | Practice Integration Plan |
|-----------|------|--------------|-----------------|---------------------------|
""")

    write_memory_file("my-memory/wellbeing/balance-wheel.md", f"""# Life Balance Wheel Check
_Last updated: {today}_

## Dimension Scores (1-10)
* Career / Contribution: 5
* Research Momentum: 5
* Physical Health: 5
* Family / Relationships: 5
* Inner Growth / Wellbeing: 5

## Action Plan for Alignment
* [Enter specific adjustments for work-life integration]
""")

    write_memory_file("my-memory/episodic/recent.md", f"""# Episodic Memory Log — Recent Sessions
_Last updated: {today}_

## [{today} 12:00] — Setup Onboarding Complete
Onboarding completed. Initialized role profile templates for '{primary_role}'. Directory structures created inside srujana-memory/.
""")

    # ── Write srujana.code-workspace in srujana-memory/ ──────────────────────
    workspace_data = {
        "folders": [
            { "path": "../SrujanaSangama" },
            { "path": "." },
            { "path": "../reva-information" }
        ],
        "settings": {}
    }
    
    workspace_file = mem_dir / "srujana.code-workspace"
    workspace_file.write_text(json.dumps(workspace_data, indent=2), encoding="utf-8")

    # ── Write Logs ───────────────────────────────────────────────────────────
    write_memory_file("my-memory/logs/sessions.log", f"[{today}] Workspace setup and onboarding completed.\n")
    write_memory_file("my-memory/logs/memory-changes.log", f"[{today}] Initialised all my-memory/ folders, soul.md, and code-workspace.\n")

    print(f"\n  {C.GREEN}{C.BOLD}✅ Workspace successfully scaffolded for {name}!{C.END}")
    print(f"  Srujana-memory workspace created at: {C.CYAN}{mem_dir}{C.END}")
    print(f"  Generated workspace file: {C.CYAN}{workspace_file}{C.END}\n")
    print(f"  {C.BOLD}Next Steps:{C.END}")
    print("    1. Close this folder in your IDE.")
    print(f"    2. Open the workspace file: {C.ORANGE}srujana-memory/srujana.code-workspace{C.END}")
    print("    3. Begin using domain slash commands (e.g. \"Use teaching-learning, run /design-course\").\n")

if __name__ == "__main__":
    main()
