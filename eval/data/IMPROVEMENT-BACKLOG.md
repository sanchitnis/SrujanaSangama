# Evaluation Improvement Backlog — F-9 Gap Topics

This file is read by `eval_bridge.py` to identify concept gaps per course.
Run `python eval_bridge.py --course-code [CODE]` to extract gap topics for `build.py --refresh`.

> **Format rule**: Each gap entry must have a `course_code` tag so `eval_bridge.py` can filter by course.
> Keep entries short — these become `--gap-topics` strings passed to the NotebookLM refresh query.

---

## How to add a gap

When a student cohort scores below threshold (F-9 = below 40% on a concept in CO attainment data),
add an entry here:

```
### [YYYY-MM-DD] [CourseCode] — [Concept name]
- **Evidence**: [source of gap — IA1 results / CO attainment report / faculty observation]
- **Priority**: High / Medium / Low
- **Gap topic string**: "[exact concept phrase to pass to --gap-topics]"
- **Status**: Open / In refresh / Resolved
```

---

## Active Gaps

*(No gaps logged yet — populate after first CO attainment cycle)*

---

## Resolved Gaps

*(Move entries here after a successful refresh has been verified by faculty)*

---

## Usage by eval_bridge.py

```powershell
# Extract gap topics for a course and pipe into refresh
$GAP_TOPICS = python skills\course-buddy-builder\tools\course-buddy-builder\eval_bridge.py --course-code B25CI0201

python skills\course-buddy-builder\tools\course-buddy-builder\build.py `
  --course-file skills\course-buddy-builder\tools\course-buddy-builder\templates\B25CI0201-descriptor.md `
  --output-dir knowledge\ `
  --refresh `
  --gap-topics $GAP_TOPICS
```
