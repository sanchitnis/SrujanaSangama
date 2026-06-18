<!-- Paste this workflow into a PhD Scholar session to plan coursework, track credits, or prepare for IA-I, IA-II, CWEE, or RPE assessments. -->

# Session Type: Coursework Planning & Assessment Preparation

**Purpose:** Set up or update the scholar's credit tracker, plan upcoming assessments, and prepare study material for a specific course.

**Estimated total time:** 30–45 minutes

---

## Phase 1 — Pathway Routing (5 min)

Activate `coursework-navigator.md` — credit pathway routing step.

Read `candidate_type` from `context/scholar-profile.md`. Display the credit floor:

| Candidate Type | Credit Floor |
|---|---|
| FT-standard | 18 credits (§9.7a) |
| 4-year-degree | 46 credits (§9.7b) |
| Industrial | 30 credits (§9.7c) |
| Foreign / other-domain | 50 credits (§9.7d) |

If candidate type is not in the profile: ask before proceeding.

---

## Phase 2 — Credit Tracker Update (10 min)

Ask the scholar to review their current credit completion status:

1. *"Which compulsory courses have you completed? (RM / RPE / ARM)"*
2. *"Which electives have you completed or are currently enrolled in?"*
3. *"Have there been any course substitutions or waivers approved by the DAC?"*

Produce and display the credit tracker table (from `coursework-navigator.md` protocol).

Flag if:
- RPE not yet completed and scholar is in Stage 3+ (RPE must be done before publication work begins)
- Credits completed < floor and scholar is approaching Stage 2 (synopsis cannot proceed until CWEE pass)

---

## Phase 3 — Assessment Preparation (20 min)

Ask: *"What are you preparing for today? IA-I / IA-II / CWEE / RPE / ARM?"*

### IA-I / IA-II
- Ask for the course name and topic list
- Identify which topics are in scope for this IA
- Provide: concept summaries, key definitions, practice questions (5–10 per topic)
- Remind: IA-I = first half of syllabus; IA-II = second half

### CWEE (Course Work End Examination)
- Covers the full course syllabus
- Build a revision plan: topic priority order, estimated revision time per topic
- Provide: 10–15 practice questions spanning all major topics
- Milestone checkpoint: CWEE pass = gateway to pre-registration colloquium

### RPE (Research and Publication Ethics)
- Scope: research integrity, plagiarism, IPR, citation standards, AI disclosure, data falsification
- Key facts to know:
  - UGC RPE directive: D.O.No.F.1-1/2018 dated December 2019 — compulsory for all PhD scholars
  - REVA plagiarism ceiling: 10% (§14.4b-ii)
  - Predatory journal identification (PUBLICATION_STANDARDS.md checklist)
- Provide: 10 short-answer questions on RPE topics

### ARM (Advanced Research Methods)
- Scope: advanced statistical methods, qualitative analysis, research design, meta-analysis
- Provide concept summaries relevant to the scholar's research area

---

## Phase 4 — Next Assessment Planning (5 min)

Ask: *"When are your upcoming assessment dates?"*

Create a mini-plan:

```
| Assessment | Date | Days Remaining | Preparation Focus |
|---|---|---|---|
| IA-I [Course] | [date] | [N] | [topics] |
| IA-II [Course] | [date] | [N] | [topics] |
| CWEE | [date] | [N] | [full revision plan] |
| RPE | [date] | [N] | [ethics + integrity] |
```

---

## Output Template

```
## Coursework Session — [Name] — [Date]

**Credit Status:**
- Candidate Type: [type] | Floor: [N]
- Completed: [N] | Remaining: [N]
- RPE: [complete / pending ⚠️]

**Prepared for:** [IA-I / IA-II / CWEE / RPE / ARM]
**Course / Topic:** [description]
**Material covered:** [list topics reviewed]

**Practice questions attempted:** [N]
**Weak areas identified:** [list]

**Next session focus:** [topic or assessment]
**Next milestone:** [CWEE / RPE / Stage 2 entry]

---
*Credit tracker updated in: `context/scholar-profile.md`*
*Assessment dates appended to: `memory/tasks.md`*
```
