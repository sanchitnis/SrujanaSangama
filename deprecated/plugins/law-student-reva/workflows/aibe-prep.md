# /aibe-prep [subject] [--mcq | --timed | --analysis | --syllabus]

**Usage:**
- `/aibe-prep Constitutional Law --mcq` — generate AIBE-pattern MCQs on a subject
- `/aibe-prep --timed` — simulate a full 100-question AIBE session (3.5 hours)
- `/aibe-prep --analysis` — review a past attempt and give subject-wise breakdown
- `/aibe-prep --syllabus` — show the 45-subject BCI AIBE syllabus with coverage status

AIBE is a **first-class feature** of this plugin, on par with bar exam prep in other jurisdictions.

---

## Profile Check

- Is AIBE in the student profile? If yes, read target date.
- If AIBE is not in profile: ask once, then proceed.
- If student is LL.M. or Ph.D. and AIBE was marked N/A: note this and offer to continue anyway if they want to attempt.

---

## Legislative Transition Reminder

> [!WARNING]
> AIBE question banks may still reference IPC, CrPC, and the Indian Evidence Act.
> As of 1 July 2024, these have been replaced by BNS, BNSS, and BSA.
> This workflow flags questions where the applicable code has changed.
> Always verify the BCI's current AIBE syllabus at barcouncilofindia.org for which version of the law is being tested in your attempt.

---

## Mode: `--mcq` — Generate AIBE-Pattern Questions

### When Invoked

Generate 10 MCQs on the specified subject (or mixed subjects if no subject given).

**Question format:**
```
Q[N]. [Question stem]

(A) [Option A]
(B) [Option B]
(C) [Option C]
(D) [Option D]

[Legislative transition flag if applicable, e.g.: Note — this tests IPC S.302 / BNS S.101. Verify which applies to your AIBE attempt.]
```

Wait for the student's answers before revealing correct answers or explanations.

### After Student Answers

For each question:
- **Correct:** Confirm and give a one-line reinforcement of the rule.
- **Wrong:** Reveal the correct answer + the statutory basis + one-sentence ratio if a case is involved. Then ask: "Can you tell me why option [student's choice] is wrong?"
- **Legislative transition:** If the question involved an IPC/CrPC/IEA provision, note the BNS/BNSS/BSA equivalent.

### Subjects Covered

All 45 BCI AIBE subjects, including:
Constitutional Law and Human Rights, Contract Law, Law of Torts, Family Law (Hindu, Muslim, Christian, Parsi), Transfer of Property, Criminal Law (BNS/IPC), Criminal Procedure (BNSS/CrPC), Civil Procedure, Evidence (BSA/IEA), Company Law, Arbitration, Environmental Law, Labour Laws, Administrative Law, Intellectual Property Law, Tax Law (Direct and Indirect), Jurisprudence, International Law, Consumer Protection Law, Banking Law, Cyber Law, Professional Ethics and Bar Council Norms.

```
[AIBE syllabus — verify subject list is current at barcouncilofindia.org]
```

---

## Mode: `--timed` — Full AIBE Simulation

### Setup

> "Starting a timed AIBE simulation. 100 questions across mixed subjects. You have 3 hours 30 minutes (210 minutes). I'll track your time.
>
> Rules of this simulation:
> - Answer all 100 questions before I reveal results.
> - No explanations during the session — only after.
> - You may flag questions as 'unsure' — I'll track those separately.
> - Say 'done' when finished or time runs out.
>
> Ready? Starting now."

Deliver questions in batches of 10. Track:
- Questions answered
- Questions flagged as unsure
- Time elapsed (based on student self-reporting or timestamps)

### After Simulation

Generate a full analysis (same as `--analysis` mode below).

---

## Mode: `--analysis` — Post-Attempt Breakdown

After a timed session or after the student uploads/pastes past AIBE attempt results:

### Output Format

```
AIBE ATTEMPT ANALYSIS
STUDY NOTES — NOT LEGAL ADVICE

Date: [date]
Questions attempted: [N] / 100
Estimated score: [N]% (AIBE pass mark: 45% for general / 40% for SC/ST/OBC — verify current BCI rule)

SUBJECT-WISE BREAKDOWN
| Subject | Qs Attempted | Correct | Accuracy | Verdict |
|---|---|---|---|---|
| Constitutional Law | 8 | 6 | 75% | Strong |
| Criminal Law (BNS) | 6 | 2 | 33% | Weak — prioritise |
| Evidence (BSA) | 5 | 1 | 20% | Critical gap |
...

TOP PRIORITY SUBJECTS FOR NEXT SESSION
1. [Weakest subject] — [specific gaps identified]
2. [Second weakest] — [specific gaps identified]
3. [Third weakest] — [specific gaps identified]

UNSURE QUESTIONS REVIEW
[List of flagged questions with correct answers and explanations]

RECOMMENDED NEXT STEPS
- `/socratic-drill [weakest subject]`
- `/flashcards [weakest subject]`
- `/aibe-prep [weakest subject] --mcq` (10 more questions)
- `/study-plan` to update your AIBE prep timeline
```

---

## Mode: `--syllabus` — Coverage Map

Show the 45 AIBE subjects with the student's self-assessed coverage status:

```
AIBE SUBJECT COVERAGE MAP
[model knowledge — verify against current BCI syllabus at barcouncilofindia.org]

| # | Subject | Status |
|---|---|---|
| 1 | Constitutional Law and Human Rights | [strong / okay / shaky / not started] |
| 2 | Law of Contract | ... |
| 3 | Law of Torts | ... |
...
| 45 | Professional Ethics and Bar Council Norms | ... |

COVERAGE SUMMARY
- Strong (ready): [N] subjects
- Okay (needs review): [N] subjects
- Shaky / Not started (priority): [N] subjects
```

Ask the student to fill in the status column. Do not assume any subject is "done" without the student confirming.

---

## BNS / BNSS / BSA Transition Flag Trigger Words

Whenever any question or discussion involves: murder, culpable homicide, theft, cheating, hurt, sedition, dacoity, arrest, bail, remand, confession, FIR, investigation, dying declaration, hearsay, documentary evidence, electronic records — flag:

```
[Legislative update — IPC/CrPC/IEA provisions replaced by BNS/BNSS/BSA w.e.f. 1 July 2024. Verify which code your AIBE attempt tests.]
```
