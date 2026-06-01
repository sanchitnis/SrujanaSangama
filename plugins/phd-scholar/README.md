# PhD Scholar — REVA Doctoral Journey Companion

> Plugin ID: `reva.phd-scholar` | Version: `1.0.0` | Publisher: `reva-university`

A stage-aware doctoral journey companion for REVA University PhD scholars in Computer Science and Applications (CSE/CSA). Guides scholars through every stage of the PhD lifecycle — and gives research supervisors a dedicated `/guide` mode to manage their scholar roster.

---

## Purpose

PhD scholars at REVA navigate a complex, multi-year journey: coursework, research, publications, thesis writing, patents, grants, and wellbeing — with limited day-to-day guidance between supervisor meetings. PhD Scholar acts as a persistent, context-aware companion that knows where the scholar is in their journey and surfaces exactly the right support at each stage.

---

## Dual Persona

| Mode | Trigger | Persona |
|---|---|---|
| **Scholar Mode** (default) | Any session without `/guide` | Empathetic, stage-aware doctoral coach |
| **Guide Mode** | `/guide` slash command | Strategic research supervisor advisor |

When `/guide` is active, the scholar-facing persona is suppressed and the supervisor gets a roster management + feedback template view.

---

## The 9-Stage PhD Lifecycle

| Stage | Name | Key Workflows |
|---|---|---|
| Stage 0 | Topic Scouting & Guide Selection | `01_entrance-prep.md` |
| Stage 1 | Coursework | `02_coursework.md` |
| Stage 2 | Synopsis & Pre-Registration Colloquium | `03_synopsis.md` |
| Stage 3 | Research Cycle | `04_research-cycle.md` |
| Stage 4 | Publication Pipeline | `05_publication-pipeline.md` |
| Stage 5 | Thesis Writing & Pre-Submission Colloquium | `06_thesis-sprint.md` |
| Stage 6 | Patent Filing | `07_patent-workflow.md` |
| Stage 7 | Grant Hunting | `08_grant-proposal.md` |
| Stage 8 | Book / Monograph | `09_book-proposal.md` |

Support workflows (`12_daily-standup.md`, `13_stuck-triage.md`, `14_wellness-checkin.md`, `15_ikigai-audit.md`) are active across all stages.

---

## School Routing

This plugin is currently fully built for **School of Computer Science and Applications (CSE/CSA)**. Scholars from other schools (ECE, Management, Life Sciences, etc.) will receive a graceful placeholder message directing them to the R&D Cell until their school materials are ready.

---

## Credit Pathways

Automatically detects candidate type and routes to the correct credit pathway:

| Candidate Type | Credit Floor | Section |
|---|---|---|
| FT/PT standard (M.Tech/M.Sc eligible) | 18 credits | §9.7a |
| Industrial experience (rich industry background, any Master's) | 30 credits | §9.7c |
| 4-year degree holder (B.Tech 70%+ direct) | 46 credits | §9.7b |
| Foreign/other-domain candidate | 50 credits | §9.7d |

---

## Publication Minimums (2018+ Batch, per §14.1)

For Engineering & Applied Sciences scholars, at least one publication must be in a Q1/Q2/Q3 journal. Three options to satisfy the minimum:

- **Option A:** 3 peer-reviewed journals (Scopus/WoS/UGC) + 1 reputed conference
- **Option B:** 2 peer-reviewed journals (Scopus/WoS/UGC) + 1 granted patent + 1 reputed conference
- **Option C:** 2 Q1/Q2 journals + 1 reputed conference

Scholar must be main author in all publications. At least one publication must be active at thesis submission time.

---

## Cross-Plugin Dependencies

| Dependency | Used By | Purpose |
|---|---|---|
| `plugins/patent-generator` | `agents/scholar/patent-agent.md`, `workflows/07_patent-workflow.md` | Full patent filing chain — no duplication |
| `plugins/research-reva` | `agents/scholar/grant-agent.md`, `workflows/08_grant-proposal.md` | Funding hunt workflow (forked with attribution) |
| `plugins/kaizen-wellbeing-reva` | `agents/scholar/wellness-companion.md`, `workflows/14_wellness-checkin.md` | Deep wellbeing support escalation |

---

## Plugin Layout

```
plugins/phd-scholar/
├── plugin.json                    # Antigravity manifest
├── package.json                   # Copilot manifest
├── README.md                      # This file
├── rules/
│   ├── SCHOLAR_IDENTITY.md        # Default scholar persona
│   ├── GUIDE_IDENTITY.md          # /guide supervisor persona
│   ├── SCHOOL_ROUTING.md          # CSE/CSA vs other-school routing
│   ├── RESEARCH_ETHICS.md         # Ethics + plagiarism (forked from research-reva)
│   ├── PUBLICATION_STANDARDS.md   # Venue tiers, predatory checks
│   ├── IKIGAI_ALIGNMENT.md        # Purpose–research alignment
│   ├── WELLBEING_STANDARD.md      # PhD mental health protocols
│   └── REVA_PHD_REGULATIONS.md    # Hard regulatory rules (REVA 2025)
├── agents/
│   ├── core/
│   │   ├── orchestrator.md
│   │   └── stage-tracker.md
│   ├── scholar/                   # One agent per lifecycle domain
│   └── guide/
│       └── guide-advisor.md
├── workflows/                     # 16 workflow files (00–15)
├── context/                       # .example profile + tracker files
├── memory/                        # .gitignore + .example memory files
│   └── semantic/
└── references/
    ├── reva-PhD-regulations.md    # Source: repo root references/
    ├── reva-phd-regulations-digest.md
    ├── india-funding-landscape.md
    ├── thesis-format-guide.md
    ├── ugc-care-guidance.md
    ├── phd-milestone-calculator.md
    └── schools/
        ├── cse/
        │   ├── researcher-handbook.md
        │   ├── methodology-guide.md
        │   └── publication-venues.md
        ├── ece/
        │   └── researcher-handbook.md.placeholder
        └── management/
            └── researcher-handbook.md.placeholder
```

---

## Governance

- **Source regulations:** `references/reva-PhD-regulations.md` (REVA University PhD Regulations 2025)
- **Ethics fork attribution:** See `rules/RESEARCH_ETHICS.md` header — forked from `plugins/research-reva/rules/RESEARCH_ETHICS.md`
- **CONSTITUTION compliance:** §3 (agent subfolders), §6 (YAML frontmatter in rules), §7 (workflow comment header), §8 (memory .example + .gitignore), §10 (attribution), §11 (graceful placeholder), §13 (≤3 files/task), §15 (no misuse of "significant")
- **Tasks spec:** `plan/tasks-revaPhDScholar.md` — APPROVED 2026-06-01
