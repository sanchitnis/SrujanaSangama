#!/usr/bin/env python3
"""
Workbook Generator — produces a Jupyter notebook (.ipynb) from course units + NLM quiz data.
Constraint: C1 (stdlib + nbformat; no API calls)
Requirement: nbformat>=5.9.0  (pip install nbformat)

Output structure per notebook:
  - Cover cell (markdown): course title, manifesto link, how to use
  - Per unit:
      - Unit heading (markdown)
      - Learning outcomes (markdown)
      - Concept explanation stub (markdown)  ← filled from NLM study guide when available
      - Exercise cell (code or markdown)     ← populated from NLM quiz JSON when available
      - Student notes cell (markdown, editable)
      - Evidence prompt cell (markdown)      ← Srujana portfolio link
  - Contribution invitation (final markdown cell)
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path
from typing import Any

try:
    import nbformat
    from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook
    _HAS_NBFORMAT = True
except ImportError:
    _HAS_NBFORMAT = False


class WorkbookGenerator:
    def __init__(
        self,
        course_meta: dict,
        units: list[dict],
        evidence_map: list[dict],
        nlm_data: dict,
        output_path: Path,
        dry_run: bool = False,
    ) -> None:
        self.meta = course_meta
        self.units = units
        self.evidence_map = evidence_map
        self.nlm = nlm_data
        self.output_path = output_path
        self.dry_run = dry_run
        self.course_code: str = course_meta["course_code"]
        self.course_name: str = course_meta.get("course_name", self.course_code)
        self.stream: str = course_meta.get("stream", "")

    def generate(self) -> None:
        if self.dry_run:
            unit_count = len(self.units)
            concept_count = sum(len(u.get("concepts", [])) for u in self.units)
            # Each unit: heading + outcomes + explanation + exercise + notes + evidence = 6 cells
            # Plus cover + contribution = 2 cells
            cell_estimate = unit_count * 6 + 2
            print(
                f"[DRY RUN] Would write: {self.output_path} "
                f"({unit_count} units, ~{cell_estimate} cells, {concept_count} concepts)"
            )
            return

        if not _HAS_NBFORMAT:
            print(
                "[WARN] nbformat not installed — skipping workbook generation. "
                "Run: pip install nbformat",
            )
            return

        nb = new_notebook()
        nb.metadata["kernelspec"] = {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        }
        nb.metadata["language_info"] = {"name": "python", "version": "3.10"}
        nb.metadata["course"] = self.course_code
        nb.metadata["course_name"] = self.course_name

        cells = []
        cells.append(self._cover_cell())

        quiz_by_unit = self._distribute_quiz_items()

        for i, unit in enumerate(self.units):
            unit_quiz = quiz_by_unit.get(i, [])
            cells.extend(self._unit_cells(unit, unit_quiz, i))

        cells.append(self._contribution_cell())

        nb.cells = cells
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        nbformat.write(nb, str(self.output_path))
        print(f"[OK] Workbook: {self.output_path} ({len(cells)} cells)")

    # ── Cell builders ────────────────────────────────────────────────────────

    def _cover_cell(self) -> Any:
        instructor = self.meta.get("instructor", "")
        semester = self.meta.get("semester", "")
        textbooks = self.meta.get("textbooks") or []
        tb_lines = "\n".join(
            f"- *{t.get('title', '')}* — {t.get('authors', '')} ({t.get('edition', '')} ed.)"
            for t in textbooks
        )
        return new_markdown_cell(textwrap.dedent(f"""\
            # {self.course_code} — {self.course_name}
            **Stream**: {self.stream} | **Semester**: {semester} | **Instructor**: {instructor}

            This workbook is part of the SrujanaBuddy Knowledge System.
            It is designed to convert course knowledge into practice and portfolio evidence,
            following the [REVA AI Tutor Philosophy](../../../references/ai-tutor-philosophy.md).

            **How to use this workbook**:
            1. Work through each unit section in order.
            2. Read the concept explanation, then attempt the exercise *before* looking at answers.
            3. Fill in your "Student notes" cell after each exercise.
            4. Complete the "Evidence prompt" cell — link your output to your Srujana portfolio.
            5. If you find an error or want to improve an explanation, add it to `student-contributions/`.

            ---

            **Textbooks**:
            {tb_lines if tb_lines else "_No textbooks listed in course descriptor._"}

            ---
        """))

    def _unit_cells(self, unit: dict, quiz_items: list[dict], unit_index: int) -> list[Any]:
        cells = []
        title = unit.get("title", f"Unit {unit_index + 1}")
        outcomes = unit.get("outcomes", [])
        concepts = unit.get("concepts", [])
        assessment = unit.get("assessment", "")

        # ── 1. Unit heading ──────────────────────────────────────────────────
        outcome_lines = "\n".join(f"{i+1}. {o}" for i, o in enumerate(outcomes))
        concept_links = ", ".join(f"`{c}`" for c in concepts)
        cells.append(new_markdown_cell(textwrap.dedent(f"""\
            ---
            ## {title}

            **Learning outcomes**: After this unit you can:
            {outcome_lines if outcome_lines else "_(Outcomes not specified)_"}

            **Key concepts**: {concept_links if concept_links else "_None listed_"}

            **Assessment**: {assessment if assessment else "_Not specified_"}
        """)))

        # ── 2. Concept explanation stub (from NLM or placeholder) ────────────
        nlm_explanation = self._find_unit_explanation(title)
        cells.append(new_markdown_cell(textwrap.dedent(f"""\
            ### Concept Overview

            {nlm_explanation}

            > **Tip**: After reading, close this cell and explain the concept to yourself
            > in the Student Notes cell below. If you cannot, re-read.
        """)))

        # ── 3. Exercise cell ─────────────────────────────────────────────────
        if quiz_items:
            cells.append(self._exercise_cell_from_quiz(quiz_items, title))
        else:
            cells.append(self._exercise_stub_cell(title, concepts))

        # ── 4. Student notes ─────────────────────────────────────────────────
        cells.append(new_markdown_cell(textwrap.dedent(f"""\
            ### My Notes — {title}

            *Replace this text with your own summary of what you learned in this unit.*

            - Key insight:
            - What confused me:
            - How I resolved the confusion:
            - One question I still have:
        """)))

        # ── 5. Evidence prompt ───────────────────────────────────────────────
        evidence = next(
            (
                row["evidence"]
                for row in self.evidence_map
                if title.split("—")[0].strip() in row.get("unit", "")
            ),
            "See Srujana Evidence Mapping in the course descriptor.",
        )
        cells.append(new_markdown_cell(textwrap.dedent(f"""\
            ### Evidence Prompt — {title}

            **Srujana evidence from this unit**: {evidence}

            Complete the following:
            - [ ] I can explain the key concepts of this unit in my own words (Stage 1 evidence).
            - [ ] I have solved at least one practice problem and documented my approach (Stage 2).
            - [ ] I have identified a real application of these concepts in a project or competition (Stage 2-3).
            - [ ] I have helped a peer understand a concept from this unit (Stage 3 — teaching is evidence).

            **Where to record**: Add a line to your Srujana portfolio under Stage 2 — Application,
            linking to this notebook cell or your solved problem submission.
        """)))

        return cells

    def _exercise_cell_from_quiz(self, quiz_items: list[dict], unit_title: str) -> Any:
        """Generate a code or markdown exercise cell from NLM quiz JSON."""
        lines = [f"### Practice Problems — {unit_title}\n"]
        for i, item in enumerate(quiz_items[:3], 1):  # max 3 per unit
            question = item.get("question", f"Question {i}")
            options = item.get("options") or []
            answer = item.get("answer", "")
            explanation = item.get("explanation", "")

            lines.append(f"**Q{i}**: {question}\n")
            if options:
                for j, opt in enumerate(options):
                    lines.append(f"   {chr(65+j)}. {opt}")
                lines.append("")
            lines.append(f"<details><summary>Answer</summary>\n\n**{answer}**")
            if explanation:
                lines.append(f"\n{explanation}")
            lines.append("</details>\n")

        return new_markdown_cell("\n".join(lines))

    def _exercise_stub_cell(self, unit_title: str, concepts: list[str]) -> Any:
        """Fallback exercise cell when no NLM quiz data is available."""
        concept_list = "\n".join(f"- {c}" for c in concepts[:5]) or "- (no concepts listed)"
        if self.stream in ("CSE", "ECE", "BCA", "MCA", "MTECH"):
            # STEM: code stub
            return new_code_cell(textwrap.dedent(f"""\
                # Practice — {unit_title}
                # Concepts: {", ".join(concepts[:3])}
                #
                # TODO: Implement a solution demonstrating one or more of these concepts.
                # Replace this comment block with working code.
                #
                # Example starter:
                # def solve(input_data):
                #     # your implementation here
                #     pass
                #
                # Test your solution:
                # print(solve(...))
            """))
        else:
            # Non-STEM: structured text prompt
            return new_markdown_cell(textwrap.dedent(f"""\
                ### Practice — {unit_title}

                **Concepts covered**:
                {concept_list}

                **Exercise**: Choose one concept from the list above. Write:
                1. A one-paragraph explanation in plain language (no jargon).
                2. A real-world example (from your own experience or a case you know).
                3. One way this concept connects to the course assessment or a career scenario.

                *Write your answer here:*

            """))

    def _contribution_cell(self) -> Any:
        return new_markdown_cell(textwrap.dedent(f"""\
            ---
            ## Contribute to the Knowledge Wiki

            Found an error? Have a better explanation? Solved a harder problem?

            Add your contribution to `student-contributions/[concept-slug]-[your-reva-id].md`
            in the course wiki folder. Accepted contributions are:
            - Attributed to you in the wiki.
            - Valid Srujana portfolio evidence (Stage 2-3 — teaching and creation).

            See [CONTRIBUTING.md](CONTRIBUTING.md) for the format and review process.

            ---
            *This workbook was generated by the SrujanaBuddy Course Buddy Builder
            ([tools/course-buddy-builder/](../../../tools/course-buddy-builder/)).
            Governing philosophy: [references/ai-tutor-philosophy.md](../../../references/ai-tutor-philosophy.md).*
        """))

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _distribute_quiz_items(self) -> dict[int, list[dict]]:
        """
        Distribute NLM quiz items across units roughly evenly.
        Returns dict: unit_index → list of quiz item dicts.
        """
        items: list[dict] = self.nlm.get("quiz_items", []) or []
        if not items or not self.units:
            return {}
        result: dict[int, list[dict]] = {}
        per_unit = max(1, len(items) // len(self.units))
        for i, unit in enumerate(self.units):
            start = i * per_unit
            result[i] = items[start: start + per_unit]
        return result

    def _find_unit_explanation(self, unit_title: str) -> str:
        """
        Try to find NLM study guide content relevant to this unit.
        Returns a Markdown string (may be a placeholder).
        """
        study_guide: str = self.nlm.get("study_guide_md", "")
        if not study_guide:
            return (
                "_Concept explanation will be populated when the course is built with NotebookLM. "
                "Run `build.py` without `--skip-notebooklm` to generate AI-enriched content._"
            )

        # Search for a section heading that matches the unit title keywords
        unit_keywords = [w.lower() for w in unit_title.split() if len(w) > 3]
        lines = study_guide.splitlines()
        best_start = -1
        for i, line in enumerate(lines):
            if any(kw in line.lower() for kw in unit_keywords):
                best_start = i
                break

        if best_start == -1:
            return "_No matching section found in NotebookLM study guide for this unit._"

        # Return up to 30 lines from that point
        excerpt = "\n".join(lines[best_start: best_start + 30]).strip()
        return excerpt if excerpt else "_No content found._"
