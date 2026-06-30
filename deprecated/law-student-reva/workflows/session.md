# /session [subject] [n]

**Usage:** `/session Contract Law 10` — focused 10-question session on Contract Law

Run a focused, N-question session on a specific subject. Questions escalate in difficulty. Results feed back into the student's study plan.

---

## Profile Check

- Confidence level for this subject (strong / okay / shaky / avoid)
- Learning style (drill-me vs. explain-to-me)
- Any recent sessions on this subject — if yes, pick up from where gaps were identified

---

## Session Setup

> "Starting a [N]-question session on [Subject].
>
> Rules:
> - I ask, you answer.
> - No hints unless you're genuinely stuck.
> - Flag any question you're unsure about — I'll track it.
> - At the end, I'll give you a score and update your study plan.
>
> Ready?"

---

## Question Progression

Questions escalate across three tiers:

**Tier 1 (Questions 1–3) — Recall**
Definition-level. What does the section say? What is the rule? What is the test?

**Tier 2 (Questions 4–7) — Application**
Give a short fact pattern. Ask the student to identify the issue, apply the rule, and reach a conclusion.

**Tier 3 (Questions 8–N) — Analysis / Edge**
Harder fact patterns. Competing precedents. Exceptions and qualifications. "What if [twist]?"

---

## During the Session

After each answer:
- **Correct and complete:** "Correct. Next." (keep pace — don't slow down for praise)
- **Partially correct:** "[What was right]. But you missed [what]. Partial credit. Note this gap."
- **Wrong:** "That's not right. The correct answer is [answer] — [one-line reason]. Flag this for review."
- **Genuinely stuck (after 30 seconds):** "Flag it. Move on. I'll come back to it."

Do not explain at length after each answer unless it was wrong — maintain session pace.

---

## Session Close

After N questions are complete:

```
SESSION RESULTS — [Subject]
STUDY NOTES — NOT LEGAL ADVICE

Date: [date]
Questions: [N]
Score: [correct] / [N] = [%]

BREAKDOWN
Tier 1 (Recall): [correct] / [tier 1 count]
Tier 2 (Application): [correct] / [tier 2 count]
Tier 3 (Analysis): [correct] / [tier 3 count]

FLAGGED QUESTIONS (review these)
Q[n]: [question text] — correct answer: [answer]
Q[n]: [question text] — correct answer: [answer]

STUDY PLAN UPDATE
[Subject] session score: [%]
→ [if < 60%]: Moving [subject] to HIGH priority. Adding flashcard review and Socratic drill to next 3 days.
→ [if 60–79%]: [Subject] staying at MEDIUM priority. Review flagged questions before next session.
→ [if ≥ 80%]: [Subject] performance is strong. Scheduled for maintenance review in [N] days.

NEXT RECOMMENDED ACTION
→ `/socratic-drill [Subject]` — to drill your weakest area from this session
→ `/flashcards [Subject] --drill` — review flagged concepts
→ `/session [Subject] [N]` — run another session to confirm improvement
```

---

## Citation Rule

All cases used in session questions must be tagged:
```
[model knowledge — verify on Indian Kanoon / SCC Online]
```

All questions involving IPC/CrPC/IEA must flag the BNS/BNSS/BSA equivalent where applicable.

---

## Mixed-Subject Session

If no subject is specified (`/session 20`), run a mixed session across the student's flagged weak subjects — prioritise "shaky" and "avoid" subjects from profile.

Tell the student upfront:
> "No subject specified — I'm pulling from your weakest areas: [list]. Mixed sessions are good for simulating AIBE. Let's go."
