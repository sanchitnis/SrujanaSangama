<!-- Paste this workflow into a research session to trigger the Autonomous AI Research Agent (Voila Protocol) -->

# Session Type: Auto-Research — Autonomous AI Research Agent

**Purpose:** Run an autonomous AI research cycle using free tools, structured sprints, and recursive self-improvement to convert a research idea or gap into a validated, submittable paper.

**Philosophy Baseline:** Grounded in `research-philosophy.md` & `voila.md` (Auto-Research Protocol).

---

## Kickoff & Environment Setup (Phase 0)

1. **Ask the Researcher**:
   - What is the primary research question, target topic, or paper gap?
   - What are the time and compute constraints? (Default: Free-tier models & Colab).
   - What is the target venue or definition of "done"? (Conference deadline, journal, or working paper draft).

2. **Initialize Workspace Scaffold** in `../srujana-memory/collaborations/<project-slug>/`:
   ```
   ├── PROJECT_BRIEF.md       # Status, claim, venue, wiki links
   ├── BACKLOG.md             # Prioritized research task backlog
   ├── SPRINTS.md             # Sprint goals & retrospectives
   ├── logs/
   │   ├── INDEX.md           # Master daily log index
   │   └── YYYY-MM-DD.md      # Sharded daily log
   ├── wiki/                  # Obsidian knowledge vault (Home.md, Glossary.md)
   ├── data/, code/, results/ # Experiments & artifacts
   └── paper/                 # Versioned drafts (v0.1, v0.2, vFinal) & CHANGELOG.md
   ```

---

## Sprint 1 — Exploration

- **LOOK**: Search literature broadly across OpenAlex, arXiv, PubMed, or EuropePMC.
- **ORIENT**: Formulate 2–4 candidate claims. Rate each against the **Four-Part Test**:
  1. *Surprising to experts?*
  2. *Fruitful ("So what?")?*
  3. *Rigorous (falsifiable)?*
  4. *Feasible with free resources?*
- **OPERATE**: Run deep checks on the top candidates to confirm the gap is unfulfilled.
- **PONDER**: Present top options to the researcher. Log the chosen direction in `PROJECT_BRIEF.md`.

---

## Sprint 2 — Question Sharpening

- **LOOK**: Deep search around the specific candidate claim.
- **ORIENT**: Formulate a single falsifiable claim sentence. Design the baseline, metrics, and experimental harness.
- **OPERATE**: Build a minimal "digital twin" / scoring harness. Run sanity checks and EVAL against known ground-truth cases before running full experiments.
- **PONDER**: Verify feasibility against current compute budget. Update `SPRINTS.md`.

---

## Sprint 3 — Experiment Execution

- **LOOK**: Check live free-tier API endpoints and Colab GPU state.
- **ORIENT**: Plan resumable experimental passes with progress checkpointing.
- **OPERATE**: Execute experimental runs. Log raw metrics to `results/`. Validate data, check signal-vs-noise ratios (between-condition vs within-condition variance).
- **PONDER**: Inspect outputs for anomalies. Apply **Recursive Self-Improvement**: *What workflow change would make the next loop faster and more rigorous?*

---

## Sprint 4 — Paper Writing & PC Reviewer Gate

- **LOOK**: Confirm target venue authoring template, page limits, and double-blind rules.
- **ORIENT**: Outline the paper strictly around validated empirical evidence.
- **OPERATE**: Draft manuscript section-by-section. Run the **PC Reviewer Audit**:
  - Audit for overclaiming, missing baselines, unruled-out confounds, and AI prose patterns.
  - Address highest-leverage weaknesses.
- **PONDER**: Version release as `paper/v0.1` (or `vFinal`). Update `paper/CHANGELOG.md`.

---

## Output Summary

End every auto-research session with a concise synthesis:
- **Current Claim**: [Falsifiable single-sentence claim]
- **Current Sprint**: [Exploration / Question Sharpening / Experiments / Writing]
- **Key Evidence**: [Validated metric vs baseline]
- **Wiki & Logs Updated**: `PROJECT_BRIEF.md`, `logs/YYYY-MM-DD.md`, `wiki/Home.md`
