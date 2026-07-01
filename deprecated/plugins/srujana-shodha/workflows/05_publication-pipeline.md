<!-- Paste this workflow into a PhD Scholar session when working on paper ideation, venue selection, paper drafting, or tracking §14.1 publication minimums. -->

# Session Type: Publication Pipeline — From Research to Published Paper

**Purpose:** Guide the scholar from research output to published paper — ideation, venue selection, drafting, submission, and reviewer response — while tracking §14.1 publication minimum compliance.

**Estimated total time:** 45–90 minutes depending on stage of paper

---

## Phase 1 — Publication Minimum Dashboard (5 min)

Always open with the §14.1 dashboard. Activate `publication-coach.md` → publication minimum tracker.

Display current status:
- Option A / B / C progress
- Engineering floor status (≥1 Q1/Q2/Q3)
- Active-publication-at-submission check

Ask: *"Which paper are we working on today — a new one, an existing draft, or a revision?"*

---

## Phase 2 — Session Type Selection (2 min)

| Option | Go to |
|---|---|
| A — New paper: ideation and venue selection | Phase 3a |
| B — Existing draft: review and improve | Phase 3b |
| C — Reviewer response: handle feedback | Phase 3c |
| D — Predatory check on a venue | Phase 3d |

---

## Phase 3a — Paper Ideation & Venue Selection (20–30 min)

Activate `publication-coach.md` → paper ideation + venue selection protocol.

1. *"What is the single most novel thing you found or built?"*
2. Identify primary audience (systems / ML / practitioners / educators)
3. Determine paper type (full 8–10 pp / short 4–6 pp / poster)
4. Map contribution to Section 6 in `references/schools/cse/publication-venues.md`
5. Generate a 3-venue shortlist with deadline, acceptance rate, and tier

**Predatory check** each venue against PUBLICATION_STANDARDS.md before recommending.

Output:
```
Venue shortlist for: [contribution area]
1. [Venue] — [type] — [tier] — [deadline] — [acceptance rate]
2. [Venue] — [type] — [tier] — [deadline] — [acceptance rate]
3. [Venue] — [type] — [tier] — [deadline] — [acceptance rate]
Recommended: [venue + reason]
```

---

## Phase 3b — Draft Review (30–45 min)

Activate `publication-coach.md` → drafting protocol.

Ask the scholar to share their draft section by section (or describe it). Review:

| Section | Check |
|---|---|
| Title | Precise, searchable, contains key technical term |
| Abstract | 150–200 words; problem + gap + method + result + significance |
| Introduction | Motivation → problem → gap → contribution list → paper structure |
| Related Work | Grouped by theme; ends with clear gap |
| Methodology | Reproducible; SIGSOFT standard cited |
| Results | Tables/figures first; no "significant" without p-value (CONSTITUTION §15) |
| Discussion | Limitations and threats to validity present |
| Conclusion | Contributions + findings + future work |

For each weak section: provide specific rewrite guidance.

---

## Phase 3c — Reviewer Response (20–30 min)

Activate `publication-coach.md` → reviewer response protocol.

1. Read all reviews in full before addressing any
2. Categorise comments (factual corrections / additional experiments / clarifications / disagreements)
3. For each comment: draft a response using the standard template
4. Assess feasibility of any additional experiments requested

Output: a response-to-reviewers draft with each comment addressed.

---

## Phase 3d — Predatory Venue Check (10 min)

Run the 7-point predatory check from PUBLICATION_STANDARDS.md.

Verdict: **Safe to submit / Hard stop — do not submit**

If hard stop: suggest an alternative venue in the same tier/domain.

---

## Phase 4 — Publication Tracker Update (3 min)

Update `memory/semantic/publication-log.md`:
- Add new paper entry or update status of existing entry
- Update §14.1 dashboard

---

## Output Template

```
## Publication Pipeline Session — [Name] — [Date]

**§14.1 Status:**
- Option [A/B/C]: [N/required]
- Engineering floor: [met / not yet]
- At least one active at submission: [yes / no / not yet applicable]

**Session focus:** [Ideation / Drafting / Reviewer Response / Predatory Check]
**Paper:** [title or working title]
**Venue selected / confirmed:** [venue — tier]
**Status:** [in-prep / submitted / under-review / revision / accepted]

**Work done this session:** [summary]

**Next action:**
1. [specific task]
2. [specific task]

---
*Publication log updated: `memory/semantic/publication-log.md`*
*§14.1 dashboard updated: `context/publication-pipeline.md`*
```
