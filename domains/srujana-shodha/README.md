# Srujana Shodha Domain (Research & Auto-Research Platform)

> **Domain Path:** `domains/srujana-shodha` | **Agent Handle:** `@shodha` (Research, PhD Supervision & Auto-Research) | **Version:** 2.0.0

The central intelligence domain for research excellence, PhD lifecycle management, grant writing, scholarly publication, and **Autonomous AI-Driven Research (Auto-Research)** across REVA University.

---

## 🔬 Domain Overview

`srujana-shodha` empowers faculty researchers, PhD scholars, and student innovation teams to perform high-impact, rigorous, and ethically grounded research. It combines institutional compliance (REVA PhD Regulations, UGC-CARE, SERB/DST grant standards) with state-of-the-art **Autonomous Agentic Research (Voila Protocol)**.

---

## 🚀 Core Capabilities

### 1. Autonomous AI Research Agent (Auto-Research / Voila Protocol)
- **The LOOP Engine**: Executes iterative research sprints through **Look $\rightarrow$ Orient $\rightarrow$ Operate $\rightarrow$ Ponder**.
- **Recursive Self-Improvement**: Evaluates both research findings and workflow processes after every cycle to adapt future execution.
- **Free/Open Resource Model**: Built for rate-limited, free-tier LLM APIs (Gemini, OpenRouter free models) and free GPU runtimes (Colab) with full state-resumability.
- **Obsidian-Compatible Knowledge Base**: Maintains a lightweight `wiki/` with `[[wikilinks]]`, `Home.md` Map of Content (MOC), and a `Glossary.md`.
- **Sharded Execution Logs**: Keeps daily log files (`logs/YYYY-MM-DD.md`) and a master `logs/INDEX.md` to prevent context explosion.

### 2. Research Philosophy & Quality Baseline
- **The Four-Part Question Test**: Evaluates candidate research claims for **Surprisingness to experts**, **Fruitfulness**, **Rigor**, and **Resource Feasibility**.
- **Ground Truth Integrity & Non-Self-Grading**: Enforces strict verification using canonical primary data sources, failure-mode sanity checks, signal-vs-noise testing, and independent evaluator "digital twins".
- **Claim-to-Evidence Calibration**: Matches paper claims strictly to empirical evidence boundaries, eliminating overclaiming.

### 3. PhD Lifecycle Supervision
- **Comprehensive Milestone Management**: Guides scholars from entrance prep, coursework, synopsis defense, biannual DRPC reviews, and thesis sprints.
- **DRPC Progress Reports**: Automates progress report compilation aligned with REVA PhD regulations.
- **Stuck Triage & Advisor Alignment**: Resolves research bottlenecks, methodology dead-ends, and guide-scholar communication loops.

### 4. Scholarly Publication & Peer Review Pipeline
- **Target Journal Selection**: Maps papers to UGC-CARE, Scopus Q1–Q4, and Web of Science indexed journals.
- **PRISMA-Lite Literature Reviews**: Structured 5-step systematic literature mapping and gap extraction.
- **Automated PC Reviewer Audit**: Evaluates manuscript drafts against conference Program Committee criteria prior to release (`paper/v0.1`, `v0.2`, `vFinal`).

### 5. Grants, Patents & Innovation Output
- **Extramural Funding Proposals**: Formats grant applications for DST, SERB, DBT, CSIR, and AICTE schemes.
- **Patent & Invention Disclosures**: Converts research breakthroughs into structured provisional and complete patent specifications.
- **SDG & Societal Impact Audit**: Maps research outcomes directly to UN Sustainable Development Goals (SDGs).

---

## 🛠️ Slash Commands

| Command | Purpose |
|---|---|
| `/auto-research` | **Kicks off the Autonomous AI Research Agent loop (Voila Protocol) for end-to-end scientific discovery.** |
| `/00_onboarding` | Research profile setup & thesis baseline. |
| `/01_entrance-prep` | PhD entrance examination preparation & syllabus review. |
| `/02_coursework` | Coursework credit tracking & methodology selection. |
| `/03_synopsis` | Synopsis drafting & defense preparation. |
| `/04_research-cycle` | Active research phase: lit review, experiment logging, & DRPC reports. |
| `/05_publication-pipeline` | Manuscript drafting, journal selection, & peer review tracking. |
| `/06_thesis-sprint` | Dissertation chapter writing sprint. |
| `/07_patent-workflow` | Invention disclosure & patent specification generation. |
| `/08_grant-proposal` | Extramural grant proposal generator (SERB/DST/AICTE). |
| `/09_book-proposal` | Monograph & academic book proposal workflow. |
| `/10_guide-dashboard` | PhD guide supervision & scholar monitoring dashboard. |
| `/11_session-closer` | Research session synthesis & task update. |
| `/12_daily-standup` | Daily research standup check-in. |
| `/13_stuck-triage` | Triage research blockers & methodology dead-ends. |
| `/14_wellness-checkin` | Scholar wellbeing & burnout prevention check. |
| `/15_ikigai-audit` | Research topic & career purpose alignment. |
| `/brand-sprint` | Google Scholar, ORCID, Scopus ID, & Vidwan profile setup. |
| `/funding-hunt` | Hunt for national and international research calls & grants. |
| `/grant-check` | Audit grant proposals against funding agency rubrics. |
| `/manuscript-check` | Quality & formatting check for journal submissions. |
| `/opportunity-mapping` | Identify relevant calls-for-papers and research conferences. |
| `/proposal-check` | Synopsis & thesis proposal compliance audit. |
| `/research-lifecycle` | Interactive research roadmap navigator. |
| `/sdg-impact-audit` | Map research outcomes to UN Sustainable Development Goals. |

---

## 📋 Governance & Domain Rules

- `ADVISOR_IDENTITY.md`: Senior research mentor persona & guidance standards.
- `GRANT_PROPOSAL_STANDARD.md`: Proposal templates for SERB, DST, DBT, and AICTE.
- `GUIDE_IDENTITY.md`: PhD guide supervision standards & DRPC compliance rules.
- `INDIA_RESEARCH_CONTEXT.md`: UGC regulations, NRF guidelines, SERB/DST norms.
- `PUBLICATION_STANDARDS.md`: UGC-CARE, Scopus Q1–Q4, and IEEE/ACM standards.
- `RESEARCH_ETHICS.md`: Anti-plagiarism limits (Turnitin/iThenticate), data authenticity rules.
- `REVA_PHD_REGULATIONS.md`: Official REVA University PhD ordinance & regulations.
- `SCHOLARLY_WRITING_STANDARD.md`: Academic prose, citation integrity, and LaTeX guidelines.

---

## 📂 Directory Layout

```plaintext
domains/srujana-shodha/
├── AGENTS.md                 # Domain Router & Auto-Research Agent Protocol (Voila)
├── README.md                 # This file
├── commands/                 # Slash command execution prompts
│   ├── auto-research.md      # Auto-Research Agent execution workflow
│   ├── 04_research-cycle.md  # Research cycle & experiment logging
│   ├── 05_publication-pipeline.md
│   └── ...                   # 26 workflow commands
└── rules/                    # Domain policies, ethics & compliance guidelines
    ├── INDIA_RESEARCH_CONTEXT.md
    ├── REVA_PHD_REGULATIONS.md
    └── ...
```
