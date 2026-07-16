---
name: reva-course-reviewer
description: >
  Review a REVA University BTech CS course design document for pedagogical quality,
  technical correctness, Bloom's taxonomy alignment, and learning effectiveness.
  Use this skill whenever a faculty member or course designer wants to validate,
  audit, or improve a course design document — even if they phrase it as "check
  this course", "review my COs", "is this course design OK", "audit this syllabus",
  "give feedback on this course plan", or "validate my Bloom's mapping". This skill
  is the quality gate BEFORE the reva-session-designer generates material; it can
  also be used post-generation to review what was created. Input is a course design
  document in Markdown format. Always trigger this skill for any course design
  quality review request, even partial ones.
compatibility: "Requires bash tool for checklist read/write. No external tools required."
---

# REVA Course Content Reviewer

Reviews a BTech CS course design document at REVA University for **pedagogical quality, technical correctness, Bloom's taxonomy alignment, CO-PO mapping integrity, and student learning effectiveness**. Produces a structured report with strengths and prioritised improvement recommendations.

This skill is **complementary to reva-session-designer** — it reviews the upstream course design document that the session designer consumes. Branding is out of scope; pedagogy and technical soundness are the focus.

---

## Step 0 — Load the Review Checklist

Before doing anything else, read the live checklist file:

```
/home/claude/reva-course-reviewer/references/review-checklist.md
```

If the file does not exist (first run), use the **Default Checklist** in Appendix A at the bottom of this file, and immediately write it to that path so future runs can evolve it.

The checklist is the single source of truth for what gets reviewed. It may have been updated by prior reviews — always load the latest version.

---

## Step 1 — Parse the Course Design Document

Extract and structure the following fields from the uploaded `.md` file:

| Field | What to look for |
|---|---|
| Course Name & Code | Header or metadata block |
| Semester / Year | Context section |
| Credits & contact hours | L-T-P structure or equivalent |
| Prerequisites | Stated or implied |
| Course Outcomes (COs) | Numbered list, usually CO1–CO6 |
| Bloom's taxonomy levels | Tagged on COs or implicit in verbs |
| Module structure | Module titles, topics, session counts |
| CO–Module mapping | Table or matrix |
| CO–PO mapping | Matrix if present |
| Assessment scheme | CIE, SEE, assignments, labs |
| Reference materials | Textbooks, online resources |
| Lab / practical component | If applicable |

If any field is missing, note it as a gap — do not ask the user to fill it in (this is a review, not an intake).

---

## Step 2 — Run the Review

Work through every checklist item. For each item, assign one of:

- ✅ **Pass** — requirement met well
- ⚠️ **Partial** — present but weak/incomplete
- ❌ **Fail** — missing or incorrect
- ➖ **N/A** — not applicable to this course type

Record evidence for each rating (quote or paraphrase from the document).

### Review Dimensions (mapped to checklist sections)

#### A. Course Outcome Quality
- Are COs written as observable, assessable student behaviours?
- Does each CO use an **action verb** from Bloom's taxonomy (not vague verbs like "understand" or "know")?
- Are CO Bloom's levels **appropriate for the semester level** (Year 1 ≠ Year 4)?
- Are there **5–6 COs** (not fewer than 4, not more than 6 for a 3-credit course)?
- Are COs **distinguishable** — do they cover different capabilities, not restate each other?
- Is there a **progression of Bloom's levels** across COs (not all at the same level)?

#### B. Bloom's Taxonomy Alignment
- For each CO, identify the **highest Bloom's verb** used.
- Check whether the **module content, topics, and assessments** actually engage students at that Bloom's level.
  - A CO at "Analyse" must have content that requires analysis — not just recall.
  - A CO at "Create" must include a design/build/compose task.
- Flag any **Bloom's level mismatch** (e.g., CO says "Evaluate" but only MCQ testing recall).
- Check whether the **assessment verbs match the CO verbs** (construct alignment).

#### C. Module & Content Coverage
- Does the content across modules **collectively address all COs**?
- Is the **CO–Module mapping matrix** complete and sensible (no orphan COs)?
- Are there topics with **no CO mapping** (wasted content) or **COs with no topic coverage**?
- Is the **topic sequencing** logical — prerequisites before dependent concepts?
- Is the **cognitive load per module** manageable (not too many new concepts at once)?
- Are **foundational concepts** introduced before applied/advanced ones?

#### D. Technical Correctness (CS-specific)
- Are all **technical terms used correctly** (terminology audit)?
- Are **algorithms, data structures, protocols, or system concepts** described accurately?
- Are **code examples or pseudocode** (if present) syntactically and semantically correct?
- Are **resource recommendations** (textbooks, links) appropriate and current?
- Is the **difficulty calibration** correct for the target audience (semester, branch)?

#### E. Assessment Design
- Does the assessment scheme **cover all COs** (CO attainment mapping)?
- Is there a **mix of formative and summative** assessment?
- Do assessments include **higher-order tasks** (projects, case studies, design problems) where COs demand Apply/Analyse/Create?
- Are **rubrics or marking criteria** present or referenced?
- Is the **CIE/SEE split** compliant with REVA norms (typically 50:50)?
- Are **lab assessments** aligned with practical COs?

#### F. Learning Effectiveness Design
- Is there evidence of **active learning strategies** (not purely lecture-based)?
- Are there **retrieval practice** opportunities (not just end-of-module tests)?
- Is **spaced practice** designed in (topics revisited across modules)?
- Does the course include **real-world application** contexts to motivate learning?
- Is **scaffolding** present — does the course build skills progressively?
- Are **prerequisite links** made explicit so students know what they need to know?

#### G. CO–PO Mapping Integrity
- Is the **CO–PO matrix present**?
- Are mappings **justified** (not all COs mapped at Level 3 to all POs — that's a red flag)?
- Do the mapped POs **logically relate** to the CO content?
- Is there coverage of **PO1 (Engineering Knowledge), PO2 (Problem Analysis), PO5 (Modern Tools)** for CS courses?
- Are **PSOs** (Programme Specific Outcomes) mapped if applicable?

#### H. Document Completeness & Usability
- Is the document **self-contained** — can a new faculty member teach from it?
- Are **session-level details** available or is it only module-level?
- Is the **lab component** described with enough detail?
- Are **pre-requisite courses** stated?
- Is the **course rationale** (why this course, what it prepares students for) present?

---

## Step 3 — Synthesise Findings

After running all checklist items, produce a structured report.

### Report Format

```
═══════════════════════════════════════════════════════════
REVA UNIVERSITY — COURSE DESIGN REVIEW REPORT
═══════════════════════════════════════════════════════════
Course: [Name] ([Code])
Reviewed: [Date]
Reviewer: REVA Course Reviewer (AI-assisted)
Document version: [if present]

OVERALL RATING: [Excellent / Good / Needs Work / Major Revision Required]
Checklist score: [X / Y items passed] ([Z]%)

───────────────────────────────────────────────────────────
SECTION 1 — STRENGTHS
───────────────────────────────────────────────────────────
[List positive findings with specific evidence. Include at minimum 3 strengths even for weak documents — acknowledge what was done well.]

● [Strength 1] — [brief evidence]
● [Strength 2] — [brief evidence]
...

───────────────────────────────────────────────────────────
SECTION 2 — RECOMMENDATIONS (sorted by importance)
───────────────────────────────────────────────────────────
[P1 = Critical — affects accreditation or student learning outcomes significantly]
[P2 = Important — should be fixed before course delivery]
[P3 = Suggested — would improve quality but not blocking]

🔴 P1 — CRITICAL
  [Item #] [Title]
  Issue: [what's wrong, with evidence]
  Why it matters: [impact on student learning / CO attainment / accreditation]
  Recommendation: [specific, actionable fix]

🟠 P2 — IMPORTANT
  [Item #] [Title]
  Issue: ...
  Recommendation: ...

🟡 P3 — SUGGESTED
  [Item #] [Title]
  Issue: ...
  Recommendation: ...

───────────────────────────────────────────────────────────
SECTION 3 — BLOOM'S LEVEL ANALYSIS
───────────────────────────────────────────────────────────
[Table showing each CO, its stated Bloom's level, the highest verb used, whether assessments align, and a verdict]

| CO | Stated Level | Key Verbs | Assessment Alignment | Verdict |
|----|-------------|-----------|---------------------|---------|
| CO1 | Apply | implement, develop | Lab + project ✅ | Aligned |
| CO2 | Analyse | examine, identify | MCQ only ⚠️ | Mismatch — needs case analysis |
...

───────────────────────────────────────────────────────────
SECTION 4 — CO COVERAGE HEATMAP (text)
───────────────────────────────────────────────────────────
[For each module, which COs does it address? Flag any CO with <2 modules addressing it.]

───────────────────────────────────────────────────────────
SECTION 5 — CHECKLIST SUMMARY TABLE
───────────────────────────────────────────────────────────
| Section | Items | Pass | Partial | Fail | N/A |
|---------|-------|------|---------|------|-----|
| A. CO Quality | n | n | n | n | n |
...

───────────────────────────────────────────────────────────
SECTION 6 — MEMORY NOTE (internal)
───────────────────────────────────────────────────────────
[After producing the report, write a 2–3 sentence memory note capturing any new pattern observed in this review that should inform future reviews. This will be saved to memory.]
═══════════════════════════════════════════════════════════
```

---

## Step 4 — Update Checklist (if warranted)

After completing the review, reflect: did this document reveal a **gap in the checklist** — something important that wasn't covered? If yes:

1. Propose the new checklist item to the user (briefly describe it and why it was triggered).
2. If the user agrees (or if running autonomously, if the gap is clear), add it to `references/review-checklist.md`.
3. Log the update with a date stamp.

This keeps the checklist **improving with each review**.

---

## Step 5 — Save Memory

After every completed review, call the `memory_user_edits` tool to add a concise note such as:

> "Course reviewer pattern [date]: [course name] — [1–2 sentences on a notable finding or recurring gap that should inform future reviews]"

Limit to one memory note per review. If the pattern is the same as a prior note (already in memory), skip.

---

## Appendix A — Default Checklist

This is the starting checklist. It is written to `/home/claude/reva-course-reviewer/references/review-checklist.md` on first run. It evolves as reviews are completed.

See `references/review-checklist.md` (created on first run from this appendix).

### DEFAULT CHECKLIST CONTENT (copy to file on first run):

```markdown
# REVA Course Design Review Checklist
Version: 1.0
Last updated: [auto-updated by reviewer]

## A. Course Outcome Quality
- [ ] A1. Each CO uses a specific Bloom's action verb (not "understand", "know", "learn")
- [ ] A2. COs are observable and assessable behaviours
- [ ] A3. Number of COs is 4–6 for a 3-credit course
- [ ] A4. COs are distinct — no two COs restate the same capability
- [ ] A5. Bloom's levels across COs show appropriate progression
- [ ] A6. CO Bloom's levels are appropriate for the semester/year level

## B. Bloom's Taxonomy Alignment
- [ ] B1. Each CO's Bloom's level is explicitly stated or clearly inferable
- [ ] B2. Module topics engage students at the stated Bloom's level (not just lower)
- [ ] B3. Assessments require performance at the stated Bloom's level
- [ ] B4. No CO-assessment Bloom's mismatch (e.g., "Evaluate" CO with only MCQ)
- [ ] B5. Higher-order COs (Apply and above) have project/design/analysis tasks

## C. Module & Content Coverage
- [ ] C1. CO–Module mapping matrix is present and complete
- [ ] C2. All COs are addressed by at least 2 modules
- [ ] C3. No module content exists without a CO mapping
- [ ] C4. Topic sequencing is logically ordered (prerequisites first)
- [ ] C5. Cognitive load per session is reasonable (≤3 new concepts)
- [ ] C6. Foundational topics precede applied/advanced topics

## D. Technical Correctness
- [ ] D1. All technical terms are used correctly
- [ ] D2. Algorithms/data structures/protocols are described accurately
- [ ] D3. Code examples or pseudocode (if present) are correct
- [ ] D4. Recommended textbooks/resources are appropriate and reasonably current
- [ ] D5. Difficulty level is appropriate for target semester and branch

## E. Assessment Design
- [ ] E1. All COs have at least one assessment mapped to them
- [ ] E2. Mix of formative and summative assessments present
- [ ] E3. Higher-order COs (Apply+) include project, case study, or design tasks
- [ ] E4. Rubrics or marking criteria are referenced
- [ ] E5. CIE/SEE split follows REVA norms
- [ ] E6. Lab assessments (if applicable) are aligned with practical COs

## F. Learning Effectiveness
- [ ] F1. Active learning strategies are embedded (not purely passive lecture)
- [ ] F2. Retrieval practice opportunities exist beyond end-of-module tests
- [ ] F3. Real-world application context is present to motivate learning
- [ ] F4. Scaffolding is evident — skills build progressively across modules
- [ ] F5. Prerequisite links are made explicit in the document

## G. CO–PO Mapping Integrity
- [ ] G1. CO–PO mapping matrix is present
- [ ] G2. Mappings use a 1–3 scale (or equivalent) with justification
- [ ] G3. Not all COs mapped at Level 3 to all POs (uniform mapping = red flag)
- [ ] G4. PO1, PO2, PO5 are meaningfully covered for CS courses
- [ ] G5. PSO mapping is present if programme has defined PSOs

## H. Document Completeness
- [ ] H1. Document is self-contained — new faculty can understand and teach from it
- [ ] H2. Lab/practical component described with sufficient detail
- [ ] H3. Prerequisite courses are stated
- [ ] H4. Course rationale is present (what does this course prepare students for?)
- [ ] H5. Session-level or week-level breakdown is available
```
