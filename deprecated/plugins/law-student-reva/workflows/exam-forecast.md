# /exam-forecast [subject] [--upload | --patterns | --priority]

**Usage:**
- `/exam-forecast Constitutional Law --upload` — analyse uploaded past papers and forecast
- `/exam-forecast Constitutional Law --patterns` — show patterns identified from past papers
- `/exam-forecast --priority` — show top-priority topics across all subjects before exam

Analyse past REVA exam papers for a subject and forecast what is likely to appear in the upcoming exam.

---

## Profile Check

- Upcoming exam date for this subject (from student profile)
- Professor name for this subject (from student profile) — professor-specific patterns are more valuable
- Materials: has the student uploaded past papers for this subject?

---

## Data Warning

If fewer than 3 past papers are available for this subject:
```
[LIMITED DATA — fewer than 3 past papers provided for [Subject]. Forecast confidence is LOW.
Patterns identified may not reflect the professor's actual examination style.
Upload more past papers with /exam-forecast [subject] --upload to improve forecast quality.]
```

If no past papers are available:
> "I don't have any past papers for [Subject] in your profile. Without them, I can only give you a generic topic-frequency analysis based on standard law school syllabi — not your professor's actual exam pattern. That's much less useful.
>
> Do you have past papers? Paste them or share a file path. Even 1-2 papers help."

---

## Mode: `--upload` — Analyse Past Papers

Student pastes or uploads past question papers.

**What to extract from each paper:**
1. Date and semester
2. Number of questions in each section (long answer / short answer / MCQ)
3. Topics covered — map each question to a topic on the subject syllabus
4. Which topics appear in EVERY paper (consistently tested)
5. Which topics appear in MOST papers (likely this year)
6. Which topics have NEVER appeared (potentially due, or permanently out of favour)
7. Question framing patterns: case-study based / statute-based / theoretical / problem questions

---

## Mode: `--patterns` — Show Analysis

After papers are analysed (or if student wants to see stored patterns), show:

```
EXAM FORECAST — [Subject]
Professor: [name, if known]
Papers analysed: [N] (Semesters: [list])
STUDY NOTES — NOT LEGAL ADVICE
[LIMITED DATA tag if < 3 papers]

TOPIC FREQUENCY MAP
| Topic | Appearances | Last Appeared | Forecast Likelihood |
|---|---|---|---|
| [Topic] | [N/N papers] | [semester] | HIGH — appears in every paper |
| [Topic] | [N/N papers] | [semester] | MEDIUM — appears in most papers |
| [Topic] | [0/N papers] | Never | LOW or UNKNOWN — never appeared |

QUESTION FORMAT PATTERNS
- Long answer questions: [typical topics, typical word count]
- Short answer questions: [typical topics]
- Case-study questions: [frequency, typical style]
- Any recurring specific case or statute always cited in questions: [list]

HIGH-PROBABILITY TOPICS FOR THIS EXAM
These are the topics that the pattern analysis suggests are most likely to appear:
1. [Topic] — appeared in [N/N] papers; last asked [semester]; likely angle: [angle]
2. [Topic] — [reasoning]
3. [Topic] — [reasoning]
4. [Topic] — [reasoning]
5. [Topic] — [reasoning]

DUE TOPICS (never or rarely appeared — watch for)
[Topics that haven't come up in a while and may be "due"]

TOPICS TO NOT NEGLECT
[Topics that students often skip assuming they won't appear, but which the pattern shows DO appear]

PREPARATION RECOMMENDATIONS
For each HIGH-probability topic:
→ `/socratic-drill [topic]`
→ `/session [subject] [n]` focused on this topic
→ `/flashcards [subject] --generate` for key cases in these topics
→ `/irac-practice` for problem questions likely to test these topics
```

---

## Mode: `--priority` — Pre-Exam Priority View

Called within 14 days of any scheduled exam. Shows a ranked topic priority list for the exam:

```
PRE-EXAM PRIORITY LIST — [Subject]
Exam in: [N] days
STUDY NOTES — NOT LEGAL ADVICE

MUST COVER (high probability + student marked weak/shaky)
1. [Topic]
2. [Topic]
3. [Topic]

COVER IF TIME ALLOWS (medium probability)
4. [Topic]
5. [Topic]

MAINTENANCE ONLY (student marked strong + moderate probability)
6. [Topic]

DO NOT SPEND ADDITIONAL TIME ON (low probability + student already strong)
[Topic list]

STUDY RECOMMENDATION FOR [N] DAYS REMAINING
Day 1–[X]: [Topic] via `/socratic-drill` and `/irac-practice`
Day [X+1]–[Y]: [Topic] via `/session` and `/flashcards --drill`
Day [Y+1]–Exam: Consolidation — `/flashcards --session 20` mixed + `/aibe-prep --mcq` if AIBE is also upcoming
```

---

## Honesty Rules

1. If patterns from past papers are clear, state them directly.
2. If patterns are ambiguous (the paper set is small or inconsistent), say so and flag confidence level.
3. Never guarantee a question will appear — state probability and reasoning.
4. Never suggest skipping topics entirely — every topic on the syllabus is fair game.
5. Always note: "Exam forecasting predicts probability, not certainty. Study the fundamentals regardless."
