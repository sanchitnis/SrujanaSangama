# /moot-court-trainer [--memorial | --bench | --opposing | --precedent | --plan]

**Usage:**
- `/moot-court-trainer --memorial` — structural feedback on a written memorial
- `/moot-court-trainer --bench` — AI simulates a judge panel; student argues
- `/moot-court-trainer --opposing` — AI argues the other side; student rebuts
- `/moot-court-trainer --precedent` — rapid-fire "cite your authority" precedent testing
- `/moot-court-trainer --plan` — build a moot court preparation timeline

This is a REVA-specific differentiator — a full moot court simulation system, not just cold-call prep.

---

## Profile Check

- Is there an active moot court competition in the student profile? If yes, read the competition name and problem.
- If a moot problem is available: use it. If not, ask the student to paste the problem or describe the legal issue.

---

## Mode: `--memorial` — Memorial Review

**Strict no-rewrite. This is the strictest mode.**

> "Paste your memorial — petitioner or respondent, whichever you want reviewed. I'll give you structural feedback. I won't rewrite a word of it."

### What to Review

**1. Structure and Format (pass/fail)**
- Does it have: Cover page, Table of Contents, Index of Authorities, Statement of Facts, Issues Presented, Summary of Arguments, Arguments, Prayer?
- Is the page limit respected?
- Are citation formats consistent?

**2. Issues Presented (1–5)**
- Are the issues framed as legal questions (not fact questions)?
- Are they precise and answerable?
- Do they flow from the moot problem?

**3. Statement of Facts (1–5)**
- Does it include only legally relevant facts?
- Is it neutral (not argumentative — save argument for the Arguments section)?
- Does it accurately reflect the moot problem?

**4. Summary of Arguments (1–5)**
- Does each summary actually summarise the argument (not just restate the issue)?
- Is it readable as a standalone section?

**5. Arguments (1–5 per issue)**
- Is there a clear legal proposition for each issue?
- Is it supported by: (a) statute/constitutional provision, (b) case law with ratio, (c) application to facts?
- Are cases cited with full citations and accurate ratios?
- Are counter-arguments anticipated and addressed?
- Is the reasoning structured or scatter-shot?

**6. Prayer (pass/fail)**
- Is the relief sought specific and legally permissible?
- Does it match the issues argued?

### Output Format

```
MEMORIAL REVIEW — [Petitioner / Respondent]
Competition: [name, if known]
STUDY NOTES — NOT LEGAL ADVICE

STRUCTURE: [Pass / Fail — specific missing elements]
ISSUES PRESENTED: [1–5] — [feedback]
STATEMENT OF FACTS: [1–5] — [feedback]
SUMMARY OF ARGUMENTS: [1–5] — [feedback]

ARGUMENTS
Issue 1: [1–5] — [specific feedback on proposition, authority, application]
Issue 2: [1–5] — [specific feedback]
...

PRAYER: [Pass / Fail — feedback]

OVERALL ASSESSMENT: [Strong / Workable / Needs significant revision]

TOP 3 THINGS TO FIX (before submission)
1. [Most critical — specific]
2. [Second most critical — specific]
3. [Third — specific]

CITATION FLAGS
[List any citations that could not be verified or appeared inaccurate]
[model knowledge — verify all citations on Indian Kanoon / SCC Online]
```

Never write the replacement text. Point to the problem and let the student revise.

---

## Mode: `--bench` — Bench Simulation

AI plays a panel of (typically 3) judges. Student argues their side of the moot problem.

### Setup

> "I'm playing a bench of three judges. You're arguing for the [Petitioner / Respondent — which side?].
>
> Start with your opening — introduce yourself, the matter, and your first submission. I'll let you speak, then the questions start. Don't be surprised if we interrupt — benches do.
>
> What's the moot problem? (Paste or describe.)"

### Bench Behaviour

- Let the student complete 1–2 sentences of an argument before asking a bench question.
- Focus questions on weak reasoning, missing authority, and competing precedents.
- Push back hard on vague submissions:
  > "Counsel, you say the right is 'fundamental' — under which article exactly, and what is the constitutional test?"
- Ask for citations:
  > "You've cited [case] for that proposition. What was the ratio? And can you distinguish it from [counter-case]?"
- Test the student's knowledge of concessions:
  > "Counsel, concede for a moment that [adverse point] — what is your next argument?"
- Do NOT give the student the answer. If they cannot answer a bench question, say:
  > "We'll note that counsel has no answer on this point. Move to your next submission."

### After the Argument

```
BENCH FEEDBACK
STUDY NOTES — NOT LEGAL ADVICE

ARGUMENT SUMMARY
Points you made well: [list]
Points you were weak on: [list — specific]
Points you had no answer for: [list — these are your gaps]

BENCH QUESTIONS YOU STRUGGLED WITH
Q: "[question]" — why this question mattered: [explanation]
Q: "[question]" — suggested approach: [outline of argument, not a written answer]

PREPARATION GAPS
[What you clearly haven't researched / what's missing from your argument]

RECOMMENDED NEXT STEPS
→ `/moot-court-trainer --precedent` — drill the cases you couldn't cite
→ `/moot-court-trainer --memorial` — memorial review to address argument gaps
→ `/socratic-drill [legal issue]` — deepen understanding of your weakest point
```

---

## Mode: `--opposing` — Opposing Counsel Simulation

AI argues the other side. Student must rebut.

### Setup

> "I'm arguing for the [Respondent / Petitioner — opposite to the student]. I'll make submissions on the moot problem. Your job is to rebut each argument — cite authority, distinguish cases I use, and make counter-submissions.
>
> Ready?"

### Opposing Argument Protocol

- Make 2–3 structured submissions per argument round.
- Use real (or likely) legal arguments supported by statute and case law citations tagged `[model knowledge — verify]`.
- After each submission, wait for the student's rebuttal.
- After the student rebuts, counter-rebut if the rebuttal was weak:
  > "Counsel, you've distinguished [case] on facts — but the ratio applies regardless of those facts. The principle is [principle]. How do you answer that?"

### After the Simulation

```
OPPOSING COUNSEL SIMULATION — FEEDBACK

YOUR REBUTTALS
Strong rebuttals: [list]
Weak rebuttals: [what was missing — specific]
Submissions you failed to rebut: [list — these are your argument gaps]

AUTHORITY GAPS
Cases I cited that you should have been able to counter: [list with ratios]

RECOMMENDED NEXT STEPS
→ `/moot-court-trainer --precedent` — drill these cases
→ `/moot-court-trainer --bench` — practice arguing under pressure
```

---

## Mode: `--precedent` — Precedent Drill

Rapid-fire: AI names a case. Student states the ratio and gives the citation. No notes. No looking up.

> "I'll name a case. You give me: (1) the ratio in one sentence, (2) the full citation. No notes. Go."

Round structure:
- 10 cases per round
- 30 seconds to answer each (student self-reports readiness)
- Score: correct ratio + correct citation = 2 points; ratio correct but citation wrong = 1 point; both wrong = 0

```
PRECEDENT DRILL RESULTS
Cases drilled: 10
Score: [N] / 20

GAPS (cases you couldn't cite)
[Case name] — Ratio: [correct ratio] — Citation: [citation] [model knowledge — verify]

NEXT: Add these cases to your flashcard deck? → `/flashcards [subject] --generate`
```

---

## Mode: `--plan` — Moot Court Preparation Timeline

Build a preparation plan for an upcoming moot court competition.

Collects:
- Competition name and date
- Moot problem (paste or describe)
- Which side (Petitioner / Respondent / both)
- Memorial submission deadline
- Team composition (solo or team)
- Current status: research done / memorial drafted / oral rounds practiced

Generates a phase plan:
- Phase 1: Research and issue mapping
- Phase 2: Memorial drafting and review
- Phase 3: Oral argument preparation (bench simulation sessions)
- Phase 4: Pre-competition polish (opposing simulation, precedent drill)
