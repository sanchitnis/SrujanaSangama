# /study-plan [--build | --update | --view]

**Usage:**
- `/study-plan --build` — build a new study plan from scratch
- `/study-plan --update` — update the plan based on recent session results
- `/study-plan` — view current plan and today's tasks

---

## Profile Check

Read from student profile:
- Programme and semester
- Subjects with confidence levels (strong / okay / shaky / avoid)
- Upcoming exam dates and deadlines
- AIBE target date (if applicable)
- Learning style

---

## Mode: `--build` — Build a New Study Plan

### Step 1 — Gather Planning Inputs

Ask (2 questions max per turn):

> 1. How many hours per day can you realistically study law? (Be honest — not aspirational.)
> 2. Are there any days in this period that are completely unavailable? (festivals, family, travel, placements)

Then ask:
> 3. Which subjects are you most worried about? (These get more time regardless of what the schedule says.)
> 4. Is AIBE prep part of this plan, or is this purely for semester exams?

### Step 2 — Generate the Plan

**Structure:**

```
STUDY PLAN — [Student name / "You"] 
Period: [start date] to [exam date or AIBE date]
Total available study days: [N]
Hours per day committed: [H]
Total study hours: [N × H]

SUBJECT ALLOCATION
| Subject | Priority | Hours Allocated | % of total |
|---|---|---|---|
| [Subject — shaky] | HIGH | [H] | [%] |
| [Subject — okay] | MEDIUM | [H] | [%] |
| [Subject — strong] | LOW (maintenance) | [H] | [%] |
| AIBE Mixed Subjects | HIGH (if applicable) | [H] | [%] |

PHASE PLAN
Phase 1 (Week 1–2): Foundation — shaky subjects, core doctrines, S.1–S.30 etc.
Phase 2 (Week 3–4): Application — IRAC practice, case brief sessions, problem questions
Phase 3 (Week 5+): Consolidation — flashcard drill, past papers, exam-forecast sessions
Final Week: Revision only — no new material

DAILY SCHEDULE TEMPLATE (adapt as needed)
[Day 1]: [Subject] — [skill] (e.g., "Constitutional Law — Socratic drill, 45 min; Case briefs — 2 cases, 30 min")
[Day 2]: [Subject] — [skill]
...
```

**Priority rules:**
- "Avoid" subjects get **40% more time** than "strong" subjects — discomfort is the point.
- AIBE subjects get their own dedicated slots if AIBE is a goal.
- No subject disappears from the plan even if the student is "strong" in it — maintenance review is scheduled.

### Step 3 — Confirm and Save

> "Here's your plan. Two things to check:
> 1. Does the daily workload feel realistic, or should I compress / stretch it?
> 2. Any subjects you want to swap more or less time into?"

After confirmation, save the plan to the session context as `study-plan.md`.

---

## Mode: `--update` — Adaptive Update

After sessions, IRAC practice, or AIBE prep runs, update the plan:

1. Identify subjects where recent session results were weak (below 60% accuracy or flagged in session summary).
2. Increase time allocation for those subjects by 20%.
3. Identify subjects where the student has consistently scored well — reduce to maintenance mode.
4. Adjust exam proximity: if an exam is within 7 days, shift to consolidation phase for that subject.

Show the diff:
```
PLAN UPDATE — [date]

Changes made:
+ Criminal Law: +2 hours this week (session score 35% — flagged weak)
- Contract Law: moved to maintenance (3 consecutive sessions above 80%)
+ AIBE Evidence (BSA): added 3-day intensive block (aibe-prep analysis flagged critical gap)
```

---

## Mode: `--view` (default) — View Plan and Today's Tasks

Show:
```
TODAY — [date]

YOUR TASKS
1. [Subject] — [workflow] — [estimated time]
2. [Subject] — [workflow] — [estimated time]

THIS WEEK'S FOCUS
[Phase and goal for this week]

UPCOMING DEADLINES
[exam date] — [subject] — [X days away]
[moot court submission] — [X days away]
[AIBE date] — [X days away]

PLAN HEALTH
Subjects on track: [N]
Subjects behind: [N — names]
Days remaining to exam: [N]
```

---

## Hard Rules

- Never schedule more than 4 hours of law study in a day without at least a 30-minute break built in.
- Always flag if the plan is mathematically impossible (too many subjects, too little time) — give the student honest numbers and ask what to drop or compress.
- If the student has fewer than 5 study days before an exam, shift entirely to consolidation mode: past papers, flashcard drills, IRAC practice — no new material.
