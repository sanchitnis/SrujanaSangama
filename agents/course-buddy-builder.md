# Agent Spec — course-buddy-builder

> **Status**: Internal infrastructure — not student-facing.
> **Skill**: [`skills/course-buddy-builder/SKILL.md`](../skills/course-buddy-builder/SKILL.md)
> **Tool**: [`skills/course-buddy-builder/tools/course-buddy-builder/`](../skills/course-buddy-builder/tools/course-buddy-builder/)
> **Output slots**: [`agents/course-buddies/instances/`](course-buddies/instances/)

---

## Purpose

The `course-buddy-builder` agent runs the pipeline that converts a filled course descriptor into three student-ready artefacts per course: an Obsidian wiki, a Jupyter workbook, and a Course Buddy `skill.md`. It is invoked by faculty or admins only — never surfaced to students.

---

## Operating Modes

| Mode | Trigger | Description |
|------|---------|-------------|
| **Build** | `build course buddy`, `create course wiki` | New course — full pipeline from descriptor |
| **Refresh** | `refresh course artefacts`, `update course buddy` | Re-run with updated descriptor or gap topics |
| **Audit** | `audit knowledge`, `staleness check` | Dry-run only — no files written |

---

## Input Contract

A valid course descriptor Markdown file with:

**Required frontmatter fields:**
- `course_code` — string, university course code (used as folder key)
- `course_name` — string, full course name
- `short_name` — string, short identifier used in file/folder names
- `stream` — one of: CSE / ECE / MBA / BCA / MCA / MTECH / PHD / other
- `semester` — integer 1–8 (UG) or 1–4 (PG)

**Required body sections:**
- `# Unit Breakdown` with `## Unit N —` subsections
- Numbered learning outcomes (`1.`, `2.`…)
- Concept checkboxes (`- [ ] concept name`)
- Assessment alignment lines (`**Assessment alignment**: …`)

**Template**: [`skills/course-buddy-builder/tools/course-buddy-builder/templates/course-descriptor.md`](../skills/course-buddy-builder/tools/course-buddy-builder/templates/course-descriptor.md)

---

## Output Contract

All output lands under `knowledge/[CourseCode]-[ShortName]/`:

```
knowledge/
  [CourseCode]-[ShortName]/
    wiki/
      index.md
      [concept-slug].md          (one per key concept, 3 levels: beginner/intermediate/advanced)
      glossary.md
      concept-map.md
      .obsidian/app.json
    workbook.ipynb
    flashcards.md                (if NotebookLM enabled)
    audio-overview.mp3           (if NotebookLM enabled)
    faculty-notes/README.md
    student-contributions/README.md
    CONTRIBUTING.md
  instances/
    [CourseCode]-[ShortName]/
      skill.md                   → copy to agents/course-buddies/instances/
```

---

## Pipeline Steps

1. **Load & validate** course descriptor frontmatter and unit body
2. **NotebookLM enrichment** (optional — skipped with `--skip-notebooklm` or `--dry-run`)
   - Study guide → concept pages
   - Mind map → concept dependency map
   - Quiz → workbook exercises
   - Flashcards → `flashcards.md`
   - Audio overview → `audio-overview.mp3`
3. **Wiki generation** — `wiki_generator.py`
4. **Workbook generation** — `workbook_generator.py`
5. **Skill generation** — `skill_generator.py`
6. **Contribution scaffold** — `CONTRIBUTING.md`, `faculty-notes/`, `student-contributions/`

---

## Human Approval Gates

| Step | Human action required |
|------|-----------------------|
| After Build | Faculty reviews generated `skill.md` before copying to `instances/` slot |
| After Refresh | Faculty checks updated wiki pages for accuracy |
| Slot assignment | Faculty updates `agents/course-buddies/instances/_SLOTS.md` manually |

AI generates — humans validate before deployment. No skill goes live without faculty sign-off.

---

## Failure Modes

| Failure | Behaviour |
|---------|-----------|
| Missing `course_code` in frontmatter | Hard exit with `[ERROR]` message; no files written |
| NotebookLM auth expired | Prints warning; falls back to `--skip-notebooklm` template-only output |
| `nbformat` not installed | Workbook step skipped gracefully; wiki and skill still generated |
| Output directory not writable | Hard exit with `[ERROR]` message |
| Descriptor has no units | Skill and workbook generated with empty tracker; wiki index only |

---

## Related Files

| File | Role |
|------|------|
| [`skills/course-buddy-builder/SKILL.md`](../skills/course-buddy-builder/SKILL.md) | Skill entry point and usage guide |
| [`agents/course-buddy-template.md`](course-buddy-template.md) | Instance skill template |
| [`agents/course-buddies/instances/_SLOTS.md`](course-buddies/instances/_SLOTS.md) | Active slot registry |
| [`knowledge/README.md`](../knowledge/README.md) | Output folder conventions |
| [`eval/data/IMPROVEMENT-BACKLOG.md`](../eval/data/IMPROVEMENT-BACKLOG.md) | F-9 gap source for `--refresh` |
