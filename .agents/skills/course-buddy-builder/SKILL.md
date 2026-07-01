---
name: course-buddy-builder
description: >
  Course Buddy Builder — faculty and admin tool for creating and maintaining per-course
  knowledge artefacts: Obsidian wiki, Jupyter practice workbook, and Course Buddy skill
  file. Covers three operating modes: Build (new course), Refresh (update existing
  artefacts), and Audit (staleness check). Free-tier compatible; NotebookLM optional.

  NOT student-facing. Use only in developer/admin context.

  Trigger on: "build course buddy", "create course wiki", "course descriptor",
  "refresh course artefacts", "audit knowledge", "knowledge wiki", "workbook generator",
  "skill_generator", "course-buddy-builder", "NotebookLM pipeline", or
  "add a new course to SrujanaBuddy".
---

# Course Buddy Builder Skill

> **Status**: Internal infrastructure — not student-facing. Never triggered during student coaching sessions.
> **Agent spec**: [`agents/course-buddy-builder.md`](../../../agents/course-buddy-builder.md)
> **Instance template**: [`agents/course-buddy-template.md`](../../../agents/course-buddy-template.md)
> **Tool**: [`tools/course-buddy-builder/`](../../../tools/course-buddy-builder/)
> **Tier**: T0/T2 (deterministic pipeline; NotebookLM integration is optional)

---

## When to use

- A new course needs a wiki, workbook, and Course Buddy skill created from scratch (**Build**)
- A course has updated syllabus, new sources, or open F-9 eval gaps (**Refresh**)
- Quarterly or pre-semester staleness check across all courses (**Audit**)

---

## Operating modes

### Build — new course

```bash
cd tools/course-buddy-builder
python3 build.py --course-file templates/[CourseCode]-descriptor.md --output-dir ../../knowledge/
```

Produces under `knowledge/[CourseCode]-[ShortName]/`:
- `wiki/` — Obsidian Markdown (index, concept pages, glossary, concept map)
- `workbook.ipynb` — Jupyter practice notebook
- `instances/[CourseCode]-[ShortName]/skill.md` — Course Buddy skill

After build: assign the generated skill to an available slot in `agents/course-buddyes/instances/`.

### Refresh — update existing artefacts

```bash
GAP_TOPICS=$(python3 tools/course-buddy-builder/eval_bridge.py --course-code CSE301)
python3 tools/course-buddy-builder/build.py \
  --course-file tools/course-buddy-builder/templates/CSE301-descriptor.md \
  --output-dir knowledge/ \
  --refresh \
  --gap-topics "$GAP_TOPICS"
```

### Audit — dry run staleness check

```bash
python3 tools/course-buddy-builder/build.py \
  --course-file tools/course-buddy-builder/templates/CSE301-descriptor.md \
  --output-dir knowledge/ \
  --dry-run
```

---

## Course Buddy instance structure

Every generated `skill.md` follows the template in [`agents/course-buddy-template.md`](../../../agents/course-buddy-template.md):

1. Syllabus and unit outcomes
2. Concept dependency map
3. Assessment blueprint
4. Question bank and past patterns
5. Practice checklist

**Mastery levels**: Not started → Basic recall → Conceptual understanding → Application → Analysis and integration → Exam-ready mastery

**Socratic flow**: Probe before answer → Diagnose misconception → Adapt explanation style → What / Why / How / What If → Student summary + one practice problem

---

## Input: course descriptor

Minimum required fields in YAML frontmatter:

| Field | Type | Description |
|-------|------|-------------|
| `course_code` | string | University course code (folder key) |
| `course_name` | string | Full course name |
| `short_name` | string | Short identifier used in file names |
| `stream` | string | CSE / ECE / MBA / BCA / MCA / MTECH / PHD / other |
| `semester` | int | 1–8 (UG) or 1–4 (PG) |

Required body sections: `# Unit Breakdown` with `## Unit N —` subsections, numbered outcomes, and `- [ ]` concept checkboxes.

Template: [`tools/course-buddy-builder/templates/course-descriptor.md`](../../../tools/course-buddy-builder/templates/course-descriptor.md)

---

## Key constraints

- **Free-tier compatible** — NotebookLM uses `notebooklm-py` (unofficial client, Google free tier). Auth via browser cookie (`notebooklm login`). Use `--skip-notebooklm` for fully offline output.
- **No paid API key required** at any tier.
- Workbook generation requires `pip install nbformat`; skipped gracefully if absent.

---

## Related files

| File | Role |
|------|------|
| [`agents/course-buddy-builder.md`](../../../agents/course-buddy-builder.md) | Full agent spec (modes, contracts, failure modes) |
| [`agents/course-buddy-template.md`](../../../agents/course-buddy-template.md) | Instance skill template |
| [`tools/course-buddy-builder/`](../../../tools/course-buddy-builder/) | Python pipeline scripts |
| [`knowledge/README.md`](../../../knowledge/README.md) | Output folder conventions |
| [`eval/data/IMPROVEMENT-BACKLOG.md`](../../../eval/data/IMPROVEMENT-BACKLOG.md) | F-9 gap source for refresh |
| [`agents/course-buddyes/instances/`](../../../agents/course-buddyes/instances/) | Active Course Buddy slots (01–10) |
