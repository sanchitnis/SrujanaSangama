<!-- Paste this workflow into a Guide (/guide) session to review the guide's scholar roster, track milestones, and prepare for DRPC reviews or colloquia. -->

# Session Type: Guide Dashboard — Scholar Roster & Supervision Review

**Purpose:** Give the PhD guide a full view of their supervised scholars' progress, upcoming milestones, regulatory obligations, and colloquium preparation status.

**Activation:** `/guide` command only. This workflow is suppressed in Scholar mode.

**Estimated total time:** 30–60 minutes depending on number of scholars

---

## Phase 1 — Guide Identification (2 min)

Ask: *"Welcome to Guide mode. Which scholar would you like to review today, or shall I show all scholars in your roster?"*

---

## Phase 2 — Scholar Roster (5–10 min per scholar)

For each scholar in the roster, activate `guide-advisor.md` → guide dashboard output.

Display:
```
## Scholar Roster — [Guide Name] — [Date]

| Scholar | Stage | Registration | Candidate Type | Next Milestone | Days Remaining | Publication Status |
|---|---|---|---|---|---|---|
| [name] | Stage N | [date] | [type] | [milestone] | [N] | Option [A/B/C]: [N/req] |
| ... | | | | | | |

Scholars at or near cap: [N out of 8 max — §7.2]
```

Flag any scholar with:
- A milestone within 14 days (⚠️)
- An overdue milestone (🔴)
- A DRPC review due within 30 days

---

## Phase 3 — Deep Review for Selected Scholar (20 min)

For the selected scholar, produce a full review using `stage-tracker.md` output:

1. Milestone timeline table (all milestones with status and days remaining)
2. Publication minimum status (§14.1 Option A/B/C)
3. Thesis chapter progress (from `context/research-tracker.md`)
4. Pending guide actions:
   - Papers awaiting guide co-author review
   - Colloquium sign-off needed
   - DRPC report signature pending
   - Corrections list from previous review — implemented?

---

## Phase 4 — Pre-Submission Colloquium Guide Checklist (10 min)

When a scholar is within 8 weeks of their pre-submission colloquium:

Internal review checklist (per §14.2):
- [ ] All research objectives from synopsis addressed?
- [ ] Methodology chapter reproducible?
- [ ] Literature review gap clearly stated?
- [ ] Publication minimums on track (§14.1)?
- [ ] Plagiarism check run (ceiling 10% — §14.4b-ii)?

Colloquium day checklist:
- [ ] Examiner panel submitted (§14.3 — panel of 12, BoS Chair within 4 weeks)?
- [ ] Open seminar invitations sent to Doctoral Committee and school faculty?
- [ ] Scholar has done a mock presentation run?
- [ ] Guide and co-guide (if any) available on colloquium day?

---

## Phase 5 — Guide Obligation Reminders (5 min)

Summarise the guide's key upcoming obligations:

| Obligation | Regulation | Scholar | Due By |
|---|---|---|---|
| DRPC review attendance | §7.2 | [name] | [date] |
| Colloquium participation | §14.2 | [name] | [date] |
| Thesis certificate sign-off | Appendix 4 | [name] | [before submission] |
| Examiner panel submission | §14.3 | [name] | Within 4 weeks of synopsis submission |
| Co-authorship on conference paper | §14.1 | [name] | Before submission |

---

## Phase 6 — Feedback Template (optional) (10 min)

If the guide wants to record progress review feedback for a scholar, generate a structured feedback note:

```
## Progress Review Feedback — [Scholar Name] — [Date]

**Reviewed by:** [Guide name]
**Period covered:** [date range]

**Work completed (confirmed):**
- [bullet points]

**Areas requiring improvement:**
- [bullet points]

**Corrective actions required:**
1. [action] — due by [date]
2. [action] — due by [date]

**Milestone confirmations this review:**
- [milestone] — confirmed complete: [yes/no]

**Guide sign-off:** [pending — guide to sign the report]
```

---

## Output Template

```
## Guide Dashboard Session — [Guide Name] — [Date]

**Scholars reviewed:** [N]
**Scholars flagged (milestone within 14 days or overdue):** [list]

**Key actions needed from guide:**
1. [action] — for scholar [name] — by [date]
2. [action] — for scholar [name] — by [date]

**Colloquium preparation status:**
[scholar name] — §14.2 step reached: [N]
Checklist: [N/10 items checked]

**Next guide session needed:** [date estimate]
```
