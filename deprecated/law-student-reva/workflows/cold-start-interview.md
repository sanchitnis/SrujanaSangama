# /cold-start-interview

Set up the student's law profile. Every other workflow in this plugin reads from what this interview writes. Generic configuration gives generic output. Specific answers give specific, calibrated output.

**Run this first.** If the student's profile already exists and has no `[PLACEHOLDER]` markers, confirm before overwriting — unless `--redo` is passed.

---

## Before the Interview Starts

Show this preamble (3–4 lines, nothing more):

> **`reva-law-student` is for REVA University Law School students — BA LLB, BBA LLB, LLM, and PhD in Legal Studies.**
>
> **2 minutes** gets you your programme, current semester, subjects, and AIBE date.
> **15 minutes** adds your learning style, weak areas, moot court schedule, and uploaded materials (past papers, notes, question banks).
>
> Quick or full? (You can upgrade any time with `/cold-start-interview --full`.)

---

## Part 0 — Who Is Using This

Ask these questions first — they determine how every other workflow branches.

**Q0.1 — Programme:**
> Which programme are you in?
> 1. B.A. LL.B. (Hons.) — 5-year integrated
> 2. BBA LL.B. (Hons.) — 5-year integrated
> 3. LL.M.
> 4. Ph.D. in Legal Studies

**Q0.2 — Year / Semester:**
> What year and semester are you in? (e.g., 2nd Year, Semester 4)

**Q0.3 — AIBE:**
> Are you preparing for AIBE? If yes, what is your target attempt date?
> (AIBE is only for students who have already graduated or are in their final semester. Skip if not applicable.)

**Q0.4 — Moot Court:**
> Are you currently preparing for any moot court competition?
> If yes: name of the competition and the problem (paste or upload if available).

---

## Part 1 — Your Subjects This Semester

> List your subjects this semester. For each subject, tell me:
> - Subject name
> - Professor's name (optional but helps exam-forecast)
> - How confident you feel: **strong / okay / shaky / avoid if possible**

Capture this as a structured list. Flag any subject marked "shaky" or "avoid" for the study plan.

---

## Part 2 — How You Learn

> When you're studying law, what works better for you:
>
> **Drill-me** — Ask me questions, push back on my answers, don't explain unless I get it badly wrong. I learn by struggling.
>
> **Explain-to-me** — Walk me through the concept first, then quiz me once I've understood it.
>
> (You can change this per-session or per-subject later.)

---

## Part 3 — Case Briefing Preference

> When briefing a case, which format do you prefer?
> 1. **IRAC** — Issue → Rule → Application → Conclusion
> 2. **FILAC** — Facts → Issue → Law → Application → Conclusion
> 3. **Indian Narrative** — Facts → Issues → Arguments (Petitioner/Respondent) → Judgment → Ratio → Obiter
> 4. **My professor's format** (paste or describe it)

---

## Part 4 — Upcoming Exams and Deadlines

> List your upcoming exam dates, moot court submission deadlines, or AIBE date.
> I'll use this to sequence your study plan.

---

## Part 5 — Materials Intake

> Upload or paste any of the following — these make every workflow sharper:
> - Past REVA exam papers (same subject or professor)
> - Past AIBE papers or question banks
> - Your existing notes or outlines
> - Moot court problem and memorial drafts
> - Syllabus for any subject
>
> Paste the contents, share a file path, or say "skip for now."
> Each item you skip is flagged in your profile as `[PENDING — add later]`.
>
> Target: 5–10 items. Below 5, your profile is tagged `[LIMITED DATA]` and downstream workflows will be thinner.

Wait for the student's response. Do not move to the next section until they respond or explicitly skip.

---

## After All Parts Are Complete

**Review before writing:**
> Before I save your profile, here's what's still open or marked as placeholder: [list any skipped items].
> Want to fill any of these now, or leave them?

Then write the profile to:
```
[plugin data path]/student-profile.md
```

with the following sections:

```markdown
# REVA Law Student Profile
*Created: [DATE]*

## Programme & Year
- Programme: [value]
- Year / Semester: [value]
- AIBE Target Date: [value or N/A]
- Moot Court Active: [yes — competition name | no]

## Subjects This Semester
| Subject | Professor | Confidence |
|---|---|---|
| [subject] | [professor] | [strong/okay/shaky/avoid] |

## Learning Style
[drill-me | explain-to-me | mixed]

## Case Brief Format
[IRAC | FILAC | Indian Narrative | custom — description]

## Upcoming Deadlines
[list]

## Materials
[list of uploaded/pasted items, or PENDING flags]

## Data Quality
[FULL DATA | LIMITED DATA — fewer than 5 materials]
```

Confirm with the student:
> "Here's what I captured — anything wrong or missing before I save?"

---

## Quick Start Path

If the student chose quick (2 minutes):
- Ask only Q0.1, Q0.2, Q0.3.
- Write config with `[DEFAULT]` markers on all other fields.
- Close with:
  > "Done. All 12 commands are ready to use. I've used sensible defaults for case-brief format and drill intensity — when a workflow's output feels off, that's usually a default worth tuning. Run `/cold-start-interview --full` any time for the full setup."

---

## Pause and Resume

Tell the student up front:
> "If you need to stop, say 'pause' and I'll save your progress. Run `/cold-start-interview` again later and I'll pick up where you left off."

On pause, write a partial profile with `<!-- SETUP PAUSED AT: [section] -->` at the top and `[PENDING]` on unanswered fields.

On re-run with a paused profile:
> "Welcome back. You paused at [section]. Your earlier answers are saved. Continue from here, or start fresh?"
