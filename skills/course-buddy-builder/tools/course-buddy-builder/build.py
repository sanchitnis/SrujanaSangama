#!/usr/bin/env python3
"""
Course Buddy Builder — CLI entry point
Constraint: C2 (Google NotebookLM free tier via notebooklm-py)
Requirements: notebooklm-py[browser]>=0.4.0, nbformat>=5.9.0, PyYAML>=6.0
How to run:
    python3 build.py --course-file templates/course-descriptor.md --output-dir ../../knowledge/
    python3 build.py --course-file templates/course-descriptor.md --dry-run
    python3 build.py --course-file templates/course-descriptor.md --skip-notebooklm
    python3 build.py --course-file templates/course-descriptor.md --refresh --gap-topics "topic A, topic B"
Example output: knowledge/CSE301-DSA/ with wiki/, workbook.ipynb, flashcards.md, skill.md
"""
from __future__ import annotations

import argparse
import asyncio
import re
import sys
import textwrap
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Frontmatter parser (stdlib-only fallback if PyYAML unavailable)
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text) from a Markdown file with YAML frontmatter."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        print(f"[ERROR] Could not parse course descriptor frontmatter: {exc}", file=sys.stderr)
        sys.exit(1)
    return fm, parts[2].strip()


def _load_course(course_file: Path) -> tuple[dict, str]:
    text = course_file.read_text(encoding="utf-8")
    fm, body = _parse_frontmatter(text)
    if not fm.get("course_code"):
        print(
            f"[ERROR] course_code is required in frontmatter of {course_file}",
            file=sys.stderr,
        )
        sys.exit(1)
    return fm, body


# ---------------------------------------------------------------------------
# Unit parser — extract units from Markdown body
# ---------------------------------------------------------------------------

def _parse_units(body: str) -> list[dict]:
    """
    Parse the '# Unit Breakdown' section from the course descriptor body.
    Returns a list of dicts with keys: title, outcomes, concepts, assessment.
    """
    units: list[dict] = []
    in_breakdown = False
    current: dict | None = None

    for line in body.splitlines():
        if re.match(r"^# Unit Breakdown", line):
            in_breakdown = True
            continue
        if in_breakdown and re.match(r"^# ", line):
            # Hit the next top-level section
            break
        if not in_breakdown:
            continue

        # New unit heading
        if re.match(r"^## Unit \d+", line):
            if current:
                units.append(current)
            current = {
                "title": line.lstrip("# ").strip(),
                "outcomes": [],
                "concepts": [],
                "assessment": "",
            }
            continue

        if current is None:
            continue

        # Outcomes: numbered list lines
        if re.match(r"^\d+\.", line):
            current["outcomes"].append(line.lstrip("0123456789. ").strip())

        # Concepts: checkbox list items
        elif re.match(r"^- \[[ x]\]", line):
            concept = re.sub(r"^- \[[ x]\] ", "", line).strip()
            current["concepts"].append(concept)

        # Assessment alignment
        elif line.startswith("**Assessment alignment**:"):
            current["assessment"] = line.replace("**Assessment alignment**:", "").strip()

    if current:
        units.append(current)

    return units


# ---------------------------------------------------------------------------
# Srujana evidence map parser
# ---------------------------------------------------------------------------

def _parse_evidence_map(body: str) -> list[dict]:
    """Return rows from the Srujana Evidence Mapping table."""
    rows: list[dict] = []
    in_table = False
    header_passed = False
    for line in body.splitlines():
        if "Srujana Evidence Mapping" in line:
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            header_passed = True
            continue
        if not header_passed or not line.startswith("|"):
            if in_table and line.startswith("#"):
                break
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) >= 3:
            rows.append({"unit": parts[0], "stage": parts[1], "evidence": parts[2]})
    return rows


# ---------------------------------------------------------------------------
# Output directory helpers
# ---------------------------------------------------------------------------

def _output_dirs(output_dir: Path, course_code: str, short_name: str) -> dict[str, Path]:
    base = output_dir / f"{course_code}-{short_name}"
    wiki = base / "wiki"
    obsidian = wiki / ".obsidian"
    faculty_notes = base / "faculty-notes"
    student_contrib = base / "student-contributions"
    skill_dir = output_dir / "instances" / f"{course_code}-{short_name}"
    return {
        "base": base,
        "wiki": wiki,
        "obsidian": obsidian,
        "faculty_notes": faculty_notes,
        "student_contrib": student_contrib,
        "skill": skill_dir,
    }


def _ensure_dirs(dirs: dict[str, Path], dry_run: bool) -> None:
    for path in dirs.values():
        if dry_run:
            print(f"[DRY RUN] Would create directory: {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

async def _run(args: argparse.Namespace) -> None:
    course_file = Path(args.course_file).resolve()
    output_dir = Path(args.output_dir).resolve()
    dry_run: bool = args.dry_run
    skip_nlm: bool = args.skip_notebooklm or dry_run
    refresh: bool = args.refresh
    gap_topics: list[str] = (
        [t.strip() for t in args.gap_topics.split(",") if t.strip()]
        if args.gap_topics
        else []
    )

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Course Buddy Builder")
    print(f"  Course file : {course_file}")
    print(f"  Output dir  : {output_dir}")
    print(f"  NLM access  : {'SKIP' if skip_nlm else 'ENABLED'}")
    print(f"  Mode        : {'REFRESH' if refresh else 'BUILD'}")
    if gap_topics:
        print(f"  Gap topics  : {gap_topics}")
    print()

    if not course_file.exists():
        print(f"[ERROR] Course file not found: {course_file}", file=sys.stderr)
        sys.exit(1)

    fm, body = _load_course(course_file)
    course_code: str = fm["course_code"]
    short_name: str = fm.get("short_name", course_code)
    course_name: str = fm.get("course_name", course_code)

    print(f"[INFO] Course: {course_code} — {course_name}")

    units = _parse_units(body)
    evidence_map = _parse_evidence_map(body)
    dirs = _output_dirs(output_dir, course_code, short_name)

    print(f"[INFO] Parsed {len(units)} units, {sum(len(u['concepts']) for u in units)} concepts")

    _ensure_dirs(dirs, dry_run)

    # ── Step 1: NotebookLM enrichment ──────────────────────────────────────
    nlm_data: dict = {}
    if not skip_nlm:
        from notebooklm_connector import NotebookLMConnector  # type: ignore
        connector = NotebookLMConnector(course_code=course_code, course_name=course_name)
        nlm_data = await connector.run(
            sources=fm.get("notebooklm_sources", {}),
            units=units,
            gap_topics=gap_topics,
            refresh=refresh,
        )
        print(f"[INFO] NotebookLM: {len(nlm_data)} artefact types received")
    else:
        reason = "dry-run" if dry_run else "--skip-notebooklm"
        print(f"[INFO] NotebookLM skipped ({reason}) — using template-only output")

    # ── Step 2: Wiki generation ─────────────────────────────────────────────
    from wiki_generator import WikiGenerator  # type: ignore
    wiki_gen = WikiGenerator(
        course_meta=fm,
        units=units,
        evidence_map=evidence_map,
        nlm_data=nlm_data,
        output_dir=dirs["wiki"],
        dry_run=dry_run,
    )
    wiki_gen.generate()

    # ── Step 3: Workbook generation ─────────────────────────────────────────
    from workbook_generator import WorkbookGenerator  # type: ignore
    wb_gen = WorkbookGenerator(
        course_meta=fm,
        units=units,
        evidence_map=evidence_map,
        nlm_data=nlm_data,
        output_path=dirs["base"] / "workbook.ipynb",
        dry_run=dry_run,
    )
    wb_gen.generate()

    # ── Step 4: Course Buddy skill generation ──────────────────────────────
    from skill_generator import SkillGenerator  # type: ignore
    skill_gen = SkillGenerator(
        course_meta=fm,
        units=units,
        nlm_data=nlm_data,
        output_path=dirs["skill"] / "skill.md",
        dry_run=dry_run,
    )
    skill_gen.generate()

    # ── Step 5: Contribution scaffolding ────────────────────────────────────
    _write_contribution_scaffold(dirs, fm, course_code, short_name, dry_run)

    # ── Step 6: Flashcards (pass-through from NLM) ──────────────────────────
    if nlm_data.get("flashcards_md"):
        flashcard_path = dirs["base"] / "flashcards.md"
        if dry_run:
            print(f"[DRY RUN] Would write: {flashcard_path}")
        else:
            flashcard_path.write_text(nlm_data["flashcards_md"], encoding="utf-8")
            print(f"[OK] Flashcards: {flashcard_path}")

    # ── Step 7: Audio overview (download from NLM) ──────────────────────────
    if nlm_data.get("audio_path"):
        audio_dest = dirs["base"] / "audio-overview.mp3"
        if dry_run:
            print(f"[DRY RUN] Would copy audio to: {audio_dest}")
        else:
            import shutil
            shutil.copy2(nlm_data["audio_path"], audio_dest)
            print(f"[OK] Audio overview: {audio_dest}")

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Build complete — {course_code}-{short_name}")
    if not dry_run:
        print(f"  Wiki     : {dirs['wiki']}/index.md")
        print(f"  Workbook : {dirs['base']}/workbook.ipynb")
        print(f"  Skill    : {dirs['skill']}/skill.md")
        print(f"\nNext step: add skill.md to agents/course-buddyes/instances/ and assign a slot (01-10).")


def _write_contribution_scaffold(
    dirs: dict[str, Path], fm: dict, course_code: str, short_name: str, dry_run: bool
) -> None:
    """Write CONTRIBUTING.md, faculty-notes/README.md, student-contributions/README.md."""
    contributing = textwrap.dedent(f"""\
        # Contribution Guide — {course_code} {fm.get('course_name', '')}

        ## For students
        Add your annotations, worked examples, or corrections to `student-contributions/`.
        Name your file `[concept-slug]-[your-reva-id].md`.
        A faculty reviewer will evaluate and promote accepted contributions to the main wiki.
        An accepted wiki contribution is a Srujana portfolio evidence item.

        ## For faculty
        Add teaching notes, common misconceptions, or resource links to `faculty-notes/`.
        Faculty annotations appear in the wiki sidebar without modifying generated pages.
        To update a generated wiki page, edit it directly and commit (you are the course owner).

        ## To trigger a refresh (faculty)
        ```bash
        cd tools/course-buddy-builder
        python3 build.py --course-file templates/{course_code}-descriptor.md \\
                         --output-dir ../../knowledge/ \\
                         --refresh --gap-topics "concept A, concept B"
        ```

        ## Philosophy
        See [references/ai-tutor-philosophy.md](../../../references/ai-tutor-philosophy.md).
    """)

    faculty_readme = textwrap.dedent(f"""\
        # Faculty Notes — {course_code} {fm.get('course_name', '')}

        Add notes here as separate Markdown files named `[topic].md`.
        These appear in the wiki as supplemental context but do not override generated pages.
        No PR needed — direct commit by course faculty is sufficient.
    """)

    student_readme = textwrap.dedent(f"""\
        # Student Contributions — {course_code} {fm.get('course_name', '')}

        Add your contributions here as Markdown files named `[concept-slug]-[reva-id].md`.
        Include: your explanation, a worked example, and a note on what you found confusing.
        A faculty reviewer will promote accepted contributions to the main wiki.
        An accepted contribution is a Srujana Stage 2-3 evidence item (teaching a concept).
    """)

    files = {
        dirs["base"] / "CONTRIBUTING.md": contributing,
        dirs["faculty_notes"] / "README.md": faculty_readme,
        dirs["student_contrib"] / "README.md": student_readme,
    }

    for path, content in files.items():
        if dry_run:
            print(f"[DRY RUN] Would write: {path}")
        else:
            if not path.exists():
                path.write_text(content, encoding="utf-8")
                print(f"[OK] Scaffold: {path.name}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Course Buddy Builder — generate wiki, workbook, and skill from a course descriptor.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python3 build.py --course-file templates/course-descriptor.md --dry-run
              python3 build.py --course-file templates/course-descriptor.md --skip-notebooklm
              python3 build.py --course-file templates/course-descriptor.md --output-dir ../../knowledge/
              python3 build.py --course-file templates/course-descriptor.md --refresh --gap-topics "heaps, BFS"
        """),
    )
    parser.add_argument(
        "--course-file",
        required=True,
        help="Path to the course descriptor Markdown file (YAML frontmatter + body).",
    )
    parser.add_argument(
        "--output-dir",
        default="../../knowledge",
        help="Root output directory for generated knowledge artefacts (default: ../../knowledge).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without writing files or calling APIs.",
    )
    parser.add_argument(
        "--skip-notebooklm",
        action="store_true",
        help="Generate template-only output without calling NotebookLM (C1-compatible).",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Re-query NotebookLM with the existing notebook (updates AI-derived sections).",
    )
    parser.add_argument(
        "--gap-topics",
        default="",
        help="Comma-separated list of concept gaps to add as extra queries in refresh mode.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    asyncio.run(_run(args))
