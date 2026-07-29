# Srujana Shodha Domain Router & Auto-Research Agent Process

> **Domain Path:** `domains/srujana-shodha`  
> **Primary Purpose:** Advanced Academic Research, PhD Lifecycle Supervision, Grant & Publication Management, and Autonomous AI-Driven Scientific Discovery (Auto-Research).  
> **Philosophy Baseline:** Grounded in `research-philosophy.md` & the `voila.md` Autonomous Research Agent Protocol.

---

## 1. Load Order & Routing Protocol

1. Read root `AGENTS.md` to confirm Usage or Development Mode.
2. Identify whether the request concerns general research guidance, grant writing, publication pipeline, thesis sprints, or **Auto-Research**.
3. If a slash command is named (e.g. `/auto-research`, `/research-cycle`, `/publication-pipeline`), read *only* the matching file in `commands/`.
4. Read rules in `rules/` only when named directly.
5. Store all research logs, wiki notes, datasets, and draft outputs in the user's `../srujana-memory/` or project workspace — **never edit shared domain infrastructure files for user session outputs**.

---

## 2. Core Research Philosophy & Quality Baseline

Every research activity in `srujana-shodha` must adhere to four foundational principles:

### A. The Four-Part Research Question Test
Before committing compute or writing time, evaluate candidate research claims against:

| Test | Criterion | Failure Mode to Guard Against |
|---|---|---|
| **Surprising to Experts** | Would a domain expert find the outcome non-obvious? | Generating "new-to-me" knowledge (learning) instead of "new-to-field" knowledge (research). |
| **Fruitful** | Does proving/disproving this claim open new pathways or change practice? | Solving a trivial, inconsequential problem ("So what?"). |
| **Rigorous** | Have alternative explanations and confounds been systematically ruled out? | Overclaiming beyond what the evidence strictly supports. |
| **Feasible** | Can this be completed with available free/open compute, time, and datasets? | Ambition outrunning resource constraints. |

### B. Validation & Non-Self-Grading Culture
- **Ground Truth Integrity**: Pull baseline metrics and standard benchmark statistics from canonical primary sources. Never hand-transcribe or hallucinate baseline numbers.
- **Sanity Checks**: Write failure-mode tests before trusting simulator or scraper outputs.
- **Signal vs. Noise**: Confirm that between-condition variation is strictly greater than within-condition (replicate) noise before claiming a finding.
- **Independent Evaluators**: Never allow a model under evaluation to grade its own output. Use deterministic digital twins, classical simulators, or held-out ground-truth scoring scripts.
- **Claim-to-Evidence Matching**: Narrow claims to match exact empirical boundaries (e.g., "improves GSM8K by 4%" instead of "improves general mathematical reasoning").

---

## 3. Autonomous Research Agent Process (The LOOP Engine)

When executing autonomous research tasks or `/auto-research`, the agent operates through **the LOOP**:

```
        ┌─────────────────────────────────────────────┐
        │                                               │
        ▼                                               │
   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌────────────┐
   │  LOOK   │───▶│ ORIENT  │───▶│ OPERATE │───▶│   PONDER   │───┐
   └─────────┘    └─────────┘    └─────────┘    └────────────┘   │
   Gather lit,    Formulate      Build code,     Reflect on      │
   check free     claim against  execute, run    findings AND    │
   resources &    4-part test    EVAL & check    adjust process  │
   environment                   ground-truth    itself          │
                                                                 │
        ◀─────────────────────────────────────────────────────────┘
```

### The Four Research Sprints
1. **Sprint 1 — Exploration**: Broad literature scan, mapping gaps, drafting 2–4 candidate claims, and presenting top options to the researcher.
2. **Sprint 2 — Question Sharpening**: Converting the selected idea into a falsifiable claim, building the minimal evaluation harness (digital twin), and validating the measurement pipeline.
3. **Sprint 3 — Experiment Execution**: Running resumable experimental passes, validating intermediate data, checking signal-vs-noise, and logging raw outputs.
4. **Sprint 4 — Paper Writing**: Structuring the manuscript around validated findings, running automated PC Reviewer audits, and compiling target-venue ready artifacts.

### Recursive Self-Improvement
After every **Ponder** step, the agent must ask:  
> *"Now that I've completed this loop, how should a smarter version of me modify the NEXT loop (both research content AND workflow process)?"*

If process bottlenecks or validation gaps are identified, update working execution guidelines immediately for subsequent loops.

---

## 4. Free Resource & Operational Constraints

- **Free Tooling Default**: Rely on free-tier LLM endpoints (e.g. OpenRouter free models, Gemini Developer API), free GPU environments (Google Colab free tier), and open-access repositories (arXiv, PubMed, EuropePMC).
- **Resumable Execution**: Always write experimental scripts with checkpointing. Free tiers disconnect or rate-limit; scripts must resume from the last saved state without losing data or repeating API calls.
- **Dynamic Endpoint Adaptation**: Query live API model lists at runtime rather than hardcoding static model names that may be deprecated.

---

## 5. Memory, Knowledge Management & Scaffolding

For every auto-research project, maintain a structured scaffold in `../srujana-memory/`:

```
srujana-memory/collaborations/<project-name>/
├── PROJECT_BRIEF.md       # Current status, active claim, venue, wiki links
├── BACKLOG.md             # Prioritized tasks & stretch goals
├── SPRINTS.md             # Sprint goals, shipped features, retrospectives
├── logs/
│   ├── INDEX.md           # Master daily log index
│   └── YYYY-MM-DD.md      # Sharded daily execution logs
├── wiki/                  # Obsidian-compatible knowledge base with [[wikilinks]]
│   ├── Home.md            # Map of Content (MOC)
│   ├── Glossary.md        # Domain jargon & definitions
│   └── ...                # Concept & decision notes
├── data/, code/, results/ # Experimental scripts & data
└── paper/                 # Versioned drafts (v0.1, v0.2, vFinal) & CHANGELOG.md
```

---

## 6. Program Committee (PC) Reviewer Quality Gate

Before finalizing any paper release (`paper/v0.1`, `v0.2`, `vFinal`), invoke the internal **PC Reviewer Audit**:
- Score against target venue criteria (Relevance, Originality, Rigor, Clarity).
- Audit for overclaiming, missing baselines, unruled-out confounds, reproducibility gaps, and AI prose patterns.
- Require all critical weaknesses to be addressed before declaring the release complete.

---

## 7. Local Commands Registry

- `00_onboarding` — Research profile setup & thesis baseline.
- `01_entrance-prep` — PhD entrance examination guidance.
- `02_coursework` — Research methodology & coursework tracking.
- `03_synopsis` — Comprehensive research synopsis drafting.
- `04_research-cycle` — Literature review (PRISMA), experiment design, & DRPC reports.
- `05_publication-pipeline` — Manuscript drafting, journal selection & peer review.
- `06_thesis-sprint` — Thesis chapter drafting & dissertation assembly.
- `07_patent-workflow` — Invention disclosure & patent specification writing.
- `08_grant-proposal` — Extramural research funding proposal generator.
- `09_book-proposal` — Academic book/monograph proposal workflow.
- `10_guide-dashboard` — PhD guide supervision & scholar progress dashboard.
- `11_session-closer` — Research session synthesis & task update.
- `12_daily-standup` — Daily research check-in.
- `13_stuck-triage` — Debugging research blockers & methodology dead-ends.
- `14_wellness-checkin` — Scholar wellbeing & burnout prevention.
- `15_ikigai-audit` — Research topic & career purpose alignment.
- `auto-research` — Autonomous AI research agent loop (Voila Protocol).
- `brand-sprint` — Scholar digital identity & Google Scholar/ORCID setup.
- `funding-hunt` — Identifying national (SERB, DST, AICTE) and global grants.
- `grant-check` — Grant proposal quality audit.
- `manuscript-check` — Manuscript readiness & journal criteria check.
- `onboarding` — PhD scholar / faculty researcher domain onboarding.
- `opportunity-mapping` — Identifying call-for-papers and research conferences.
- `proposal-check` — Synopsis & thesis proposal compliance verification.
- `research-critique` — Critical evaluation of STEM research publications, theses, and reports.
- `research-lifecycle` — End-to-end research lifecycle roadmap.
- `sdg-impact-audit` — Mapping research outcomes to UN Sustainable Development Goals.
- `session-closer` — Standard session wrap-up.

---

## 8. Local Rules Registry

- `ADVISOR_IDENTITY.md` — Senior research advisor persona & coaching tone.
- `GRANT_PROPOSAL_STANDARD.md` — Format standards for DST, SERB, DBT & AICTE proposals.
- `GUIDE_IDENTITY.md` — PhD guide supervision standards & DRPC compliance.
- `IKIGAI_ALIGNMENT.md` — Passion, competence, institutional need & societal impact alignment.
- `INDIA_RESEARCH_CONTEXT.md` — UGC regulations, NRF guidelines, SERB/DST funding norms.
- `PERSONAL_BRAND_STANDARD.md` — Google Scholar, Scopus ID, ORCID, and Vidwan profile standards.
- `PUBLICATION_STANDARDS.md` — UGC-CARE, Scopus Q1–Q4, and IEEE/ACM indexing requirements.
- `RESEARCH_ETHICS.md` — Plagiarism thresholds (Turnitin/iThenticate), IRB approval, & data authenticity.
- `REVA_PHD_REGULATIONS.md` — REVA University PhD ordinance, course credit, and thesis rules.
- `SCHOLARLY_WRITING_STANDARD.md` — Academic prose, active voice, citation integrity, and latex formats.
- `SCHOLAR_IDENTITY.md` — Scholar empowerment & self-directed learning mindset.
- `SCHOOL_ROUTING.md` — School-specific research directions (C&IT, ECE, Mech, Science, Law, Management).
- `SDG_MAPPING_STANDARD.md` — UN SDG 17 targets alignment methodology.
- `WELLBEING_STANDARD.md` — Mental health, workload balancing, and burnout mitigation guidelines.

---

## 9. Output Boundary

All research artifacts, daily logs, Obsidian notes, experimental code, and paper drafts **MUST** be written to `../srujana-memory/` or collaboration workspaces. Do not modify files in `domains/srujana-shodha/` during user research execution sessions.
