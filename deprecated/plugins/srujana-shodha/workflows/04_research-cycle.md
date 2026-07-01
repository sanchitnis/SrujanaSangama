<!-- Paste this workflow into a PhD Scholar session for a biannual DRPC review cycle, systematic literature review, or experiment logging session. -->

# Session Type: Research Cycle — Lit Review, Experiments & Biannual Review

**Purpose:** Support the scholar's active research phase — systematic literature review, experiment design and logging, DRPC progress report preparation, and stage-tracker refresh.

**Estimated total time:** 45–90 minutes depending on focus

---

## Phase 1 — Stage Tracker Refresh (5 min)

Open with a milestone check:
- Call `stage-tracker.md` to refresh the timeline
- Identify the next upcoming milestone and days remaining
- Ask: *"Has your guide confirmed any milestone completions since our last session?"*

If yes: update `context/research-tracker.md` milestone log.

---

## Phase 2 — Research Session Type Selection (3 min)

Ask: *"What shall we focus on today?"*

| Option | Activate |
|---|---|
| A — Systematic literature review | Phase 3a |
| B — Experiment design or results analysis | Phase 3b |
| C — Biannual DRPC progress report | Phase 3c |
| D — Research methodology clarification | `research-coach.md` → methodology selection |

---

## Phase 3a — Systematic Literature Review (PRISMA-lite) (30–45 min)

Activate `research-coach.md` — PRISMA-lite protocol.

1. Define 3–5 search terms
2. Select databases: IEEE Xplore, ACM DL, Scopus, Google Scholar, arXiv
3. Define inclusion/exclusion criteria (date range, publication type, relevance)
4. Group papers by theme (not chronology)
5. Extract gap statement (3 sentences)

Output format:
```
Search terms: [list]
Databases: [list]
Papers reviewed: N → included: N

Themes:
1. [theme] — [summary + gap]
2. [theme] — ...

Research gap: [3 sentences]
```

---

## Phase 3b — Experiment Design & Results Logging (30 min)

Activate `research-coach.md` — experiment design protocol.

1. Convert research question to H0 + H1
2. Identify variables (independent, dependent, control)
3. Define baseline and comparison method
4. Select metrics (accuracy, F1, latency, etc.)
5. Select statistical test (t-test / Wilcoxon / ANOVA / Mann-Whitney)
6. Log results in structured format:

```
Experiment: [name / ID]
Hypothesis: H1 = [statement]
Method: [what was run]
Baseline: [what it was compared to]
Result: [metric value] vs. baseline [value]
Statistical test: [test name] | p-value: [value]
Conclusion: [H1 supported / not supported]
Threats to validity: [list]
```

**CONSTITUTION §15 check:** If results are described as "significant", confirm a p-value is reported.

---

## Phase 3c — Biannual DRPC Progress Report (30–45 min)

Activate `research-coach.md` — biannual progress report protocol.

Work through the 5-section report structure:
1. Work completed since last review (with evidence)
2. Current milestone status (vs. `stage-tracker.md` timeline)
3. Challenges and blockers (with proposed resolutions)
4. Plan for next 6 months (specific, measurable)
5. Publication status update (§14.1 tracker)

Check: Is the publication minimum on track? Display the §14.1 dashboard (from `publication-coach.md`).

---

## Phase 4 — Memory Update (5 min)

After the session:
- Offer to update `context/research-tracker.md` with experiment log or milestone confirmation
- Offer to append the progress report draft to `memory/semantic/progress-reports.md.example`
- Update `memory/tasks.md` with next research tasks

---

## Output Template

```
## Research Cycle Session — [Name] — [Date]

**Session type:** [Lit Review / Experiment / DRPC Report]

**Milestone check:**
- Next milestone: [milestone] — [N days remaining]
- Any milestone confirmed this session: [yes/no — details]

**Work done this session:**
[summary of lit review / experiment / report section completed]

**Publication minimum status:**
- Option [A/B/C] progress: [N/required completed]
- Engineering floor (≥1 Q1/Q2/Q3): [met / not yet]

**Next action:**
1. [specific task + estimated time]
2. [specific task + estimated time]

---
*Research tracker updated: `context/research-tracker.md`*
*Tasks updated: `memory/tasks.md`*
```
