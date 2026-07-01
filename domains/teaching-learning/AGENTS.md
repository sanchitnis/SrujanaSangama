# Teaching Learning Domain Router

Use this router only after the root `AGENTS.md` Usage Mode router selects
`teaching-learning`.

## Load Order

1. Identify whether the request concerns curriculum design, course design,
   session planning, assessment, active learning, concept mapping, or question
   paper review.
2. If a slash command is named, read only the matching file in `commands/`.
3. Read rules only when the command or request names them directly.
4. Read shared skills only when the command or request names them directly.
5. Use `reva-information/` only for the specific syllabus, regulation,
   programme, or accreditation reference needed by the task.

## Local Commands

- `10_curriculum-strategy-check`
- `11_activity-design-ai-ready`
- `12_concept-map-network`
- `assessment-check`
- `course-check`
- `curriculum-design-lifecycle`
- `lesson-plan`
- `question-paper-reviewer`
- `session-check`

## Local Rules

- `ACADEMIC_INTEGRITY.md`
- `ASSESSMENT_QUALITY_STANDARD.md`
- `COURSE_DESIGN_STANDARD.md`
- `CURRICULUM_DESIGN_FRAMEWORK_v2.md`

## Output Boundary

Draft outputs for faculty and committee review. Write persistent task outputs to
the user's `srujana-memory/` or collaboration space, not to this shared domain
folder.
