---
name: PhD Milestone Calculator
description: Input rules and derivation logic used by agents/core/stage-tracker.md to auto-compute milestones for each candidate type.
version: "1.0"
tags: [milestone, stage-tracker, regulations, timeline, phd]
source: REVA PhD Regulations 2025 — §4, §6, §7, §9
---

# PhD Milestone Calculator
## Spec for `agents/core/stage-tracker.md` Auto-Compute Logic

This file defines the precise derivation rules that `stage-tracker.md` must apply when computing milestone dates for a scholar. All date arithmetic is calendar-month-based.

---

## 1. Inputs (Read from `context/scholar-profile.md`)

| Field | Key | Required? |
|---|---|---|
| Registration date | `registration_date` | Yes |
| Candidate type | `candidate_type` | Yes |
| School / Department | `school` | Yes |
| Qualification | `highest_qualification` | Yes |
| Employment status | `employment` | Optional (for industrial candidacy) |

Candidate type options: `FT-standard` | `PT-working` | `industrial` | `foreign` | `other-domain`

---

## 2. Duration Rules (REVA PhD Regulations §4)

| Candidate Type | Minimum Duration | Maximum Duration | Source |
|---|---|---|---|
| FT-standard | 3 years | 6 years | §4.1, §4.2 |
| PT-working | 4 years | 7 years (with extension) | §4.1, §4.2 |
| industrial | 3 years | 6 years | §4.1, §4.2 |
| foreign | 3 years | 6 years | §4.1 |
| other-domain | 3 years | 6 years | §4.1 |

**Annulment rule (§4.5):** If no submission is made within 10 years of registration, registration is annulled. Flag when remaining time ≤ 6 months.

---

## 3. Credit Floor Rules (REVA PhD Regulations §9.7)

| Candidate Type | Minimum Credits | Note |
|---|---|---|
| FT-standard | 18 | Standard floor |
| industrial | 30 | Higher floor |
| 4-year UG degree | 46 | Applies regardless of FT/PT |
| foreign or other-domain | 50 | Highest floor |

Derivation: Read `candidate_type` and `highest_qualification`. If `highest_qualification` is "4-year B.Tech / BE", floor = max(type_floor, 46). If `candidate_type` is `foreign` or `other-domain`, floor = 50.

---

## 4. Stage Milestones — Derivation Rules

### Stage 0 — Pre-Registration (before `registration_date`)
Not computable. Display: *"Registration not yet complete — milestones will auto-compute on registration."*

### Stage 1 — Coursework Phase

**Coursework deadline:** `registration_date` + 12 months (FT) or + 18 months (PT)

Coursework complete when `credits_earned >= credit_floor`.

**IA sessions:** Scheduled by institution — no auto-compute. Display: *"Check with School for IA schedule."*

**RPE (Research Proposal Evaluation):** After coursework complete, before end of Year 1 (FT) or Year 1.5 (PT).

### Stage 2 — Synopsis and Colloquium

**Earliest synopsis submission:** `registration_date` + 18 months (FT) or + 24 months (PT)

**Pre-submission colloquium (§14.2):** Must occur before thesis submission. Earliest: 6 months before planned thesis submission.

**Colloquium re-appearance:** If failed, earliest re-appearance = colloquium_date + 1 month.

### Stage 3 — Active Research

No fixed deadline. Tracks:
- Biannual DRPC reviews (every 6 months from `registration_date`)
- Publication milestone progress (§14.1 option)

### Stage 4 — Writing Up

No fixed rule. Recommended: begin when ≥ 2 chapters drafted and 1 paper accepted.

### Stage 5 — Pre-Submission Colloquium

(See §14.2 above — belongs to this stage in the workflow.)

### Stage 6 — Thesis Submission

**Submission deadline rule (§14.4):**
- Batch 2014–2019: submit by **30 November** of the eligible year
- Batch 2020+: submit by **30 April** of the eligible year

**"Eligible year"** = first year when minimum duration has elapsed and all publication requirements are met.

**Plagiarism ceiling (§14.4):** ≤ 10% overall; must be checked before submission.

**6-month fee exemption window:** If scholar submits within 6 months of guide certification, no additional fee is charged. Flag when this window approaches.

### Stage 7 — Examination

**Examiner panel (§14.3):**
- 12 examiners: 6 from Karnataka, 6 from outside Karnataka (≥1 from abroad)
- Each examiner: PhD holder, ≥5 years post-PhD experience, h-index ≥5
- BoS Chair must appoint panel within 4 weeks of thesis submission

**Viva voce (§15.4):** Open viva; at least 1 external examiner must be present (video conferencing permitted).

### Stage 8 — Award

**INFLIBNET (§16):** Thesis must be submitted to INFLIBNET/Shodhganga before the award is announced. Flag if not done.

---

## 5. DRPC Review Schedule

DRPC (Doctoral Research Progress Committee) reviews occur every 6 months from `registration_date`.

Compute as: `registration_date` + (N × 6) months for N = 1, 2, 3, …

Display: next upcoming DRPC date, days remaining, and what must be ready for that review.

---

## 6. Output Format for stage-tracker.md

When called, `stage-tracker.md` must output:

```
## PhD Progress Snapshot — [Scholar Name]

Registration date: YYYY-MM-DD
Candidate type: [type]
Time elapsed: N years, N months
Current stage: Stage N — [Stage Name]

--- Milestone Timeline ---
Stage 1 — Coursework deadline:          YYYY-MM-DD  [complete / on-track / overdue]
RPE:                                    YYYY-MM-DD  [complete / on-track / overdue]
Stage 2 — Earliest synopsis:            YYYY-MM-DD  [complete / on-track / not yet]
Next DRPC review:                       YYYY-MM-DD  (N days from today)
Stage 5 — Colloquium (if applicable):   YYYY-MM-DD  [scheduled / not yet]
Stage 6 — Thesis submission deadline:   YYYY-MM-DD  [N months remaining]
Stage 7 — Examiner panel due:           YYYY-MM-DD  [after submission]

--- Publication Status (§14.1 Option [A/B/C]) ---
Required: [N] / Completed: [N] / Active: [N]
Engineering floor (≥1 Q1/Q2/Q3): [met / not yet]

--- Flags ---
[Any flags: annulment risk / submission window / fee exemption / plagiarism check due / INFLIBNET pending]
```

---

## 7. Re-Computation Triggers

stage-tracker.md should re-compute when any of the following change in `context/scholar-profile.md`:
- `registration_date`
- `candidate_type`
- `highest_qualification`
- `credits_earned`
- `publication_status` (any entry)
- `colloquium_date`
- `thesis_submission_date`
