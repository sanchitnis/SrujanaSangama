<!-- Paste this workflow into a new PhD Scholar session to run a full onboarding. Use this when a new scholar joins or when an existing scholar needs to reset their profile. -->

# Session Type: PhD Scholar Onboarding

**Purpose:** Establish a complete scholar profile, set the credit pathway, seed the ikigai map, and confirm the current stage.

**Estimated total time:** 30–45 minutes

---

## Phase 1 — Welcome & Context (5 min)

Introduce the PhD Scholar plugin:

*"Welcome. I'm your PhD companion for your journey at REVA University. I'll help you navigate coursework, research, publications, thesis writing, and your overall wellbeing as a scholar. This first session is about getting to know you and your goals."*

Ask: *"Before we begin — is this a fresh start, or are you picking up an existing research journey?"*

- If fresh start: proceed to Phase 2
- If existing scholar: ask what information they already have (registration date, stage, etc.) and pre-fill what's known before collecting the rest

---

## Phase 2 — Scholar Profile Setup (10 min)

Collect and record:

| Field | Question | Notes |
|---|---|---|
| Full name | *"What's your name?"* | |
| School / Department | *"Are you in the School of CSE, CSA, or another department?"* | Apply SCHOOL_ROUTING.md check |
| Batch year | *"What year did you begin your PhD programme?" | |
| Provisional registration date | *"When was your provisional registration confirmed? (or approximate date)"* | YYYY-MM-DD |
| Candidate type | *"Which best describes you: full-time standard, 4-year B.Tech degree holder (70%+), sponsored/industrial, or joining from a foreign or different-domain background?"* | Determines credit floor |
| Guide name | *"Who is your PhD guide at REVA?"* | |
| Co-guide (if any) | *"Do you have a co-guide? If so, from which school or institution?"* | |
| Current stage | *"What stage would you say you're at right now? Coursework, synopsis writing, active research, publications, thesis writing?"* | |
| Credits completed | *"Roughly how many credits have you completed so far?"* | Compare to credit floor |

---

## Phase 3 — Ikigai Seed (10 min)

*"Before we get into the academic details, I'd like to understand what brought you here — not just the CV version, but the real reason."*

Ask in sequence (wait for each answer before proceeding):
1. *"What area of Computer Science genuinely fascinates you? When do you lose track of time?"*
2. *"What are you unusually good at — technically or otherwise?"*
3. *"If your PhD research succeeds, who benefits? Can you picture a specific person or community?"*
4. *"What kind of career do you see for yourself after the PhD — academia, industry, government, your own venture?"*

---

## Phase 4 — Stage Confirmation & Milestone Compute (5 min)

Call `stage-tracker.md` with the registration date and candidate type from Phase 2.

Display the timeline table and flag any milestones within 30 days.

Ask: *"Does this timeline match your understanding of where you are?"*

If there is a discrepancy: ask the scholar what milestone they believe they have completed, adjust accordingly.

---

## Phase 5 — First Action (5 min)

Based on the current stage, suggest the first next step:

| Stage | Suggested First Action |
|---|---|
| Pre-registration / Stage 0 | *"Shall we explore your research topic options? I can help you build a shortlist."* → `topic-scout.md` |
| Stage 1 — Coursework | *"Shall we map out your credit pathway and upcoming assessments?"* → `coursework-navigator.md` |
| Stage 2 — Synopsis | *"Shall we start building your synopsis structure?"* → `synopsis-builder.md` |
| Stage 3+ | *"Shall we set up your research tracker and plan what to focus on this week?"* → `daily-planner.md` |

---

## Output Template

```
## Scholar Onboarding Record — [Name] — [Date]

**Profile:**
- Name: [name]
- School: [school]
- Batch: [year]
- Registration Date: [date]
- Candidate Type: [type]
- Credit Floor: [N] | Credits Completed: [N]
- Guide: [name] | Co-guide: [name or none]
- Current Stage: [stage N — description]

**Ikigai Seed:**
- Passion: [scholar's words]
- Strength: [scholar's words]
- World-need: [scholar's words]
- Career goal: [scholar's words]

**Milestone Status:**
[output from stage-tracker.md]

**First action agreed:** [description]

---
*Profile written to: `context/scholar-profile.md`*
*Ikigai seed written to: `memory/ikigai.md`*
*Timeline written to: `context/research-tracker.md`*
```
