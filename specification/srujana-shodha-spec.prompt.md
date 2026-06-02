# Plan: `reva.srujana-shodha` Plugin (Faculty Research & Doctoral Journey Companion)

**TL;DR:** A unified, standalone, Markdown-native Copilot plugin (`reva.srujana-shodha` / `@reva-scholar`) combining two key academic research domains: (1) Faculty research advisor (funding opportunity mapping, manuscript drafting, and grant proposal reviews) and (2) Doctoral journey companion (guiding PhD scholars and guides through all 9 lifecycle stages). Features a dual-persona mode (`@reva-scholar` / `/guide` trigger) for seamless transition between faculty research coaching, student self-management, and supervisor roster reviews. Phase 1 is CSE/CSA-first; other branches use placeholders.

---

## Phase 0 — Input Material Authoring *(prerequisite; blocks later phases)*

Collect/author these before plugin files can be finalized:

1. **REVA PhD Regulations — Sections 14+** (publication requirements, thesis submission rules, examination — available in `references/reva-PhD-regulations.md`)
2. **CSE publication venues list** — IEEE Transactions, ACM, Springer conferences tagged by tier (Q1/Q2/Q3)
3. **India funding landscape digest** — DST-SERB, DBT, CSIR JRF/SRF, UGC fellowships, ICMR, industry grants (v2.0 digest)
4. **REVA thesis format template** — Appendix 4 of REVA PhD Regulations 2025
5. **UGC CARE list + Scopus/WoS guidance** — journal selection heuristics, anti-predatory red flags
6. **Branch placeholder files** — ECE, Management, Life Sciences, etc. (empty structures; user populates later)

---

## Phase 1 — Plugin Scaffolding

- `plugins/srujana-shodha/plugin.json` — id: `reva.srujana-shodha`, version 2.0.0; lists rules + workflows; registers `/guide` slash command; registers `@reva-scholar` agent.
- `plugins/srujana-shodha/package.json` — exposes `reva-scholar` agent with slash commands: `/grant`, `/manuscript-check`, `/proposal-check`, and `/guide` (for supervisor mode).
- `plugins/srujana-shodha/mcp.json` — MCP server config connecting to REVA Scholar API.
- `plugins/srujana-shodha/README.md`

---

## Phase 2 — Rules Layer *(14 files)*

| File | Purpose |
|---|---|
| `rules/ADVISOR_IDENTITY.md` | Faculty research advisor persona: competency profiling, brand building |
| `rules/SCHOLAR_IDENTITY.md` | Default scholar persona: empathetic coach; stage-aware, regulation-enforcing |
| `rules/GUIDE_IDENTITY.md` | Activated by `/guide`: strategic supervisor advisor |
| `rules/REVA_PHD_REGULATIONS.md` | Distilled hard rules: deadlines, credit floors, publication minimums, cancellation triggers |
| `rules/RESEARCH_ETHICS.md` | Plagiarism thresholds, authorship norms, RPE course content, SIGSOFT standards from CSE Handbook (Unified) |
| `rules/SCHOOL_ROUTING.md` | Branch detection → loads CSE materials; graceful placeholder message for other branches |
| `rules/PUBLICATION_STANDARDS.md` | Journal tier guidance, predatory red flags, UGC CARE list, conference tiers |
| `rules/WELLBEING_STANDARD.md` | When to suggest a break vs. escalate; PhD-specific mental health red flags; references `kaizen-wellbeing-reva` |
| `rules/IKIGAI_ALIGNMENT.md` | Defines ikigai check triggers (onboarding, stage transitions, signs of disengagement) |
| `rules/INDIA_RESEARCH_CONTEXT.md` | Specific constraints and contexts for Indian government and state funding agencies |
| `rules/SDG_MAPPING_STANDARD.md` | Standards for aligning academic research to UN Sustainable Development Goals (SDGs) |
| `rules/PERSONAL_BRAND_STANDARD.md` | Guidelines for faculty profile, ORCID, h-index, and citation brand building |
| `rules/GRANT_PROPOSAL_STANDARD.md` | Structure and formatting compliance standards for India public sector grant submissions |
| `rules/SCHOLARLY_WRITING_STANDARD.md` | Grammar, terminology, empirical standards, and style guides for academic papers |

---

## Phase 3 — Agents Layer *(24 files)*

**Core (3):**
- `agents/core/orchestrator.md` — Routes Faculty, Scholar vs. `/guide` mode; activates correct stage agent
- `agents/core/stage-tracker.md` — Auto-computes milestone dates from provisional registration date + supervisor-confirmed progress inputs
- `agents/core/memory-steward.md` — Manages profile context, progress updates, and semantic memory synchronization

**Faculty Specialist Agents (8):**
- `agents/faculty/competency-profiler.md` — Maps research profile, ORCID, and SDG alignments
- `agents/faculty/opportunity-scout.md` — Scans for funding options and interdisciplinary partners
- `agents/faculty/collaboration-architect.md` — Structures department and international co-author networks
- `agents/faculty/funding-navigator.md` — Directs proposal compliance to SERB/DST/DBT briefs
- `agents/faculty/research-pipeline-coach.md` — Orchestrates data-gathering, experiments, and logging
- `agents/faculty/journal-targeter.md` — Evaluates target journals, indexing, and publication fit
- `agents/faculty/work-product-reviewer.md` — Audits drafts, checklists, and grant review rubrics
- `agents/faculty/personal-brand-builder.md` — Guides citation outreach, conference prep, and brand mapping

**Scholar lifecycle agents (9):**
- `agents/scholar/topic-scout.md` | Stage 0: Research area mapping, guide eligibility check, topic feasibility
- `agents/scholar/coursework-navigator.md` | Stage 1: Credit pathway routing, ARM/RPE coaching, IA prep
- `agents/scholar/synopsis-builder.md` | Stage 2: Pre-registration colloquium prep; synopsis structure template
- `agents/scholar/research-coach.md` | Stage 3: Lit review (PRISMA-lite), methodology selection, experiment design
- `agents/scholar/publication-coach.md` | Stage 4: Paper targeting, drafting, reviewer response coaching; publication tracker
- `agents/scholar/thesis-writer.md` | Stage 5: Chapter-by-chapter guidance, format compliance, anti-plagiarism checklist
- `agents/scholar/patent-agent.md` | Stage 6: Invokes `patent-generator` workflows adapted for scholar context
- `agents/scholar/grant-agent.md` | Stage 7: India grant calendar, SERB/DST/DBT/ICMR structures; adapts funding workflows
- `agents/scholar/book-agent.md` | Stage 8: Research monograph / book proposal, publisher targeting, chapter outline

**Support & Guide agents (5):**
- `agents/scholar/daily-planner.md` — Breaks current milestone into weekly/daily micro-tasks
- `agents/scholar/blocker-breaker.md` — Blocker triage: classifies blocker → routes to targeted help
- `agents/scholar/wellness-companion.md` — Wellbeing check-ins, imposter syndrome, stress/anxiety relief
- `agents/scholar/ikigai-compass.md` — Research–ikigai alignment mapping across stages
- `agents/guide/guide-advisor.md` — `/guide` mode: scholar roster view, progress alerts, feedback templates

---

## Phase 4 — Workflows Layer *(26 files)*

**Faculty-facing Workflows (10):**
- `workflows/onboarding.md` — Faculty profile setting, SDG mapping, ORCID verification
- `workflows/opportunity-mapping.md` — Matching research expertise to call briefs
- `workflows/funding-hunt.md` — Systematic funding search and eligibility check
- `workflows/research-lifecycle.md` — Step-by-step drafting, logging, and evaluation
- `workflows/brand-sprint.md` — Profile optimization, citation mapping, and outreach
- `workflows/sdg-impact-audit.md` — Assessing publications against UN SDG indicators
- `workflows/grant-check.md` — `/grant` command: review proposal against agency templates
- `workflows/manuscript-check.md` — `/manuscript-check` command: manuscript structural and ethics review
- `workflows/proposal-check.md` — `/proposal-check` command: grant proposal quality and budget audit
- `workflows/session-closer.md` — Session summary, commitment logging, and memory save

**Scholar-facing Workflows (16):**
- `workflows/00_onboarding.md` — Scholar profile setup (FT/PT, registration date, guide)
- `workflows/01_entrance-prep.md` — Mock interviews, RM study prep, presentation dry run
- `workflows/02_coursework.md` — Course tracking, credit verification, exam prep
- `workflows/03_synopsis.md` — Synopsis outline builder, pre-registration defense prep
- `workflows/04_research-cycle.md` — Lit review cycle, logging, progress tracker
- `workflows/05_publication-pipeline.md` — Paper draft, target selection, peer feedback
- `workflows/06_thesis-sprint.md` — Formatting checklist, pre-submission colloquium
- `workflows/07_patent-workflow.md` — IP screening, Form 1/2/3 helper
- `workflows/08_grant-proposal.md` — PhD fellowship and seed grant proposals
- `workflows/09_book-proposal.md` — Monograph chapter plan, academic publisher targeting
- `workflows/10_guide-dashboard.md` — `/guide` command: roster review, milestone alerts
- `workflows/11_session-closer.md` — Summary capture and next micro-tasks refresh
- `workflows/12_daily-standup.md` — 3-point standup: yesterday, today, blockers
- `workflows/13_stuck-triage.md` — Blocker pathing (conceptual, emotional, regulatory)
- `workflows/14_wellness-checkin.md` — Mentoring check-in, stress levels monitor
- `workflows/15_ikigai-audit.md` — Annual alignment audit (passion, values, society)

---

## Phase 5 — Context & Memory Templates

**`context/` (committed example templates):**
- `scholar-profile.md.example` — Onboarding metadata, batch, candidate type, guide, stage
- `research-tracker.md.example` — Milestones timeline, review logs, calculated deadlines
- `publication-pipeline.md.example` — Under-review, accepted, and published track
- `daily-log.md.example` — Standup logs, task list, blocker notes

**`memory/` (gitignored local files):**
- `soul.md` — Research and learning profile identity
- `ikigai.md` — Alignment map and tension audit logs
- `tasks.md` — Milestone checklist, weekly planning, micro-tasks
- `wellbeing-log.md` — Personal wellness check-in record
- `semantic/research-pipeline.md` — Ongoing research threads, logs, methodologies
- `semantic/publication-log.md` — Detailed submission tracking and reviews
- `semantic/progress-reports.md` — DRPC biannual comments and actions history
- `semantic/episodic/` — Session-by-session notes logs

---

## Phase 6 — References Folder

```
plugins/srujana-shodha/references/
  schools/
    cse/
      researcher-handbook.md        ← empirical standards for CSE researchers
      publication-venues.md         ← publication venue guide (Scopus, WoS, UGC-CARE)
      methodology-guide.md          ← software engineering empirical methods
    ece/
      researcher-handbook.md.placeholder
    management/
      researcher-handbook.md.placeholder
  reva-phd-regulations-digest.md    ← quick-reference card for credit pathways and milestones
  ugc-care-guidance.md              ← UGC journal indexing change context
  india-funding-landscape.md        ← fellowship and seed funding agency database
  thesis-format-guide.md            ← margins, fonts, chapter order layout standards
  phd-milestone-calculator.md       ← timeline auto-calculation logic spec
```

---

## Scope Boundaries

- **In scope**: Faculty research advisor workflows, 9-stage PhD scholar lifecycle workflows, supervisor `/guide` mode, Indian funding landscape, CSE branch reference guidelines.
- **Out of scope**: Direct submission API connections to external journals; automated push notifications; ECE/Management branch handbooks (placeholders only in Phase 1).
- **Blocked until input**: None.

---

## Verification Criteria

1. Manifest files (`plugin.json`, `package.json` under `plugins/srujana-shodha`) resolve correctly inside the marketplace environments.
2. The `@reva-scholar` agent successfully responds to `/grant`, `/manuscript-check`, `/proposal-check` and `/guide` triggers.
3. Onboarding routes correctly based on school inputs (CSE loads full guidelines; ECE returns placeholder).
4. Stage tracker computes precise milestone deadlines based on candidate credit pathways (18/30/46/50 credits).
5. All references in `references/` comply with `CONSTITUTION.md` attribution and duplication standards.
