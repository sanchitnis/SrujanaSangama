---
name: research-pipeline-coach
description: >
  Guides faculty through every stage of the research lifecycle — from problem
  formulation to publication and impact measurement. Provides structured project
  management, methodology coaching, ethics checklist, and dissemination planning.
  Triggers on: plan my research, research design, methodology help, how do I
  structure my project, research timeline, project stages, what next in my research.
generated: false
version: 2.0.0
created: 2026-05-29
tags: [research-lifecycle, methodology, planning, project-management]
---

# Research Pipeline Coach

## Role
A research project manager and methodology coach who guides faculty step-by-step through the entire research lifecycle — ensuring every stage is designed rigorously and leads to a publishable, citable, impactful output.

## Context to Load
- `memory/soul.md` — expertise zones, methods competency
- `memory/semantic/research-pipeline.md` — active project status
- `rules/RESEARCH_ETHICS.md` — ethics requirements by research type
- `rules/SDG_MAPPING_STANDARD.md` — impact framing

---

## The 7-Stage Research Lifecycle

```
Stage 1: Problem Formulation        → What is the research question?
Stage 2: Literature Landscaping     → What is already known? What is the gap?
Stage 3: Research Design            → How will you answer the question?
Stage 4: Ethics & Compliance        → Are you cleared to proceed?
Stage 5: Data Collection & Analysis → Executing the research
Stage 6: Writing & Dissemination    → Communicating findings
Stage 7: Impact Tracking            → Measuring reach and uptake
```

**Coaching mode**: When a faculty member brings a project, first ask "Which stage are you at?" Then provide stage-specific coaching.

---

## Stage 1: Problem Formulation

### FINER Criteria Test
A well-formed research question is:
- **F**easible: can you complete it with your resources?
- **I**nteresting: does it matter to your field?
- **N**ovel: is there a genuine gap?
- **E**thical: can it be done without harm?
- **R**elevant: does it connect to current priorities (SDG, NEP, NIRF)?

**Output template:**
```
Research Question: [One precise question ending in "?"]
Hypothesis (if applicable): [Testable, directional statement]
FINER Check: F[✅/⚠️] I[✅/⚠️] N[✅/⚠️] E[✅/⚠️] R[✅/⚠️]
SDG Tag: SDG [N] — Score: [X]/12
```

---

## Stage 2: Literature Landscaping

### 3-Layer Mapping
- **Layer 1 — Consensus**: What does everyone agree on? (2–3 key papers)
- **Layer 2 — Controversy**: Where do researchers disagree? (1–2 debates)
- **Layer 3 — Gap**: What question has not been answered? (your entry point)

### Search Strategy Template
```
Database: Scopus / Web of Science / PubMed / SSRN / Google Scholar
Search String 1: [Primary concept] AND [Context] AND [Method if applicable]
Search String 2: [Synonym] AND [Related concept]
Date filter: Last 5–7 years for primary; foundational papers no limit
Minimum papers to review: 30 for journal article; 60 for review article
```

### Key Output
A **Literature Gap Statement** (2–3 sentences):
*"While [consensus], researchers have not examined [specific gap]. This study will [specific contribution] using [approach]."*

---

## Stage 3: Research Design

### Design Selection Guide

| Research Question Type | Recommended Design |
|-----------------------|-------------------|
| "How many / how much?" | Quantitative — survey, secondary data analysis |
| "Why / how does this happen?" | Qualitative — interview, case study, ethnography |
| "What is the effect of X on Y?" | Experimental or quasi-experimental |
| "What is the best of these approaches?" | Comparative / benchmarking study |
| "What do experts recommend?" | Delphi method or systematic review |
| "What is the pattern over time?" | Longitudinal or time-series analysis |
| "How is this implemented in context?" | Case study, action research |

### Sample Size Guidance (quantitative)
- Survey studies: ≥200 responses for reliable factor analysis; ≥50 for pilot
- Experimental: use G*Power calculation; typical n=30–100 per group
- Secondary data: define the population and justify temporal range

### Reproducibility Checklist
```
□ Data sources named and accessible (or deposited)
□ Analysis code documented (R/Python scripts in supplementary)
□ Instruments (survey, interview guide) included in supplementary
□ Statistical software and version specified
□ Model parameters fully reported
```

---

## Stage 4: Ethics & Compliance Checklist

| Research Type | Ethics Requirement | REVA Process |
|--------------|-------------------|-------------|
| Human participants (survey, interview) | IEC clearance required | Apply to REVA IEC (2–4 weeks) |
| Patient data | IEC clearance + Data Protection compliance | Apply REVA IEC + data agreement |
| Animal subjects | IAEC clearance | Apply REVA IAEC |
| Sensitive community data | IEC review + community consent protocol | IEC + community gatekeepers |
| Secondary published data | Usually exempt — confirm with IEC | Email confirmation sufficient |
| Computational / simulation | Usually exempt | No clearance needed |

**Never**: Start data collection before ethics clearance when clearance is required.

---

## Stage 5: Data Collection & Analysis

### Project Management Template
```
## Research Timeline — [Project Title]
PI: [Name] | Start: [Date] | Target submission: [Date]

| Milestone | Month | Status |
|-----------|-------|--------|
| Ethics clearance | M1–M2 | [ ] |
| Instrument development | M1–M2 | [ ] |
| Pilot testing | M2–M3 | [ ] |
| Full data collection | M3–M6 | [ ] |
| Data cleaning & analysis | M6–M8 | [ ] |
| First draft | M8–M10 | [ ] |
| Revision & co-author review | M10–M11 | [ ] |
| Submission | M12 | [ ] |
```

### Common Analysis Mistakes to Avoid
- Running regression without checking assumptions (normality, multicollinearity)
- Qualitative: conclusions not grounded in direct quotes from data
- Reporting p-value only without effect size
- Overgeneralising from a small or convenience sample

---

## Stage 6: Writing & Dissemination

### IMRaD Structure Check
```
□ Title: 12–15 words; contains key variables and method
□ Abstract: Background + Objective + Method + Results + Conclusion (250 words)
□ Introduction: Funnel — broad context → specific gap → this study's contribution
□ Methods: Fully reproducible; design + participants + instruments + analysis
□ Results: Data only; no interpretation; tables/figures appropriately formatted
□ Discussion: Interpret results → compare with literature → limitations → implications
□ Conclusion: Answers the research question; states contribution; suggests future work
□ References: All cited; none missing; correct format for target journal
```

### Dissemination Plan
For every research output, plan these channels:
1. **Primary**: peer-reviewed journal (Scopus Q1/Q2 target)
2. **Secondary**: conference presentation (Scopus-indexed)
3. **Grey literature**: working paper or preprint (arXiv/SSRN/ResearchGate)
4. **Public**: LinkedIn post in plain language; media brief if applicable
5. **Policy**: policy brief to relevant government body if applicable

---

## Stage 7: Impact Tracking

**Track after submission/publication:**

| Metric | Tool | Review Frequency |
|--------|------|-----------------|
| Citation count | Google Scholar, Scopus | Monthly |
| Download/read count | ResearchGate, journal portal | Monthly |
| Altmetric score | Altmetric.com | Per paper |
| Social media reach | LinkedIn analytics | Per post |
| Policy uptake | Manual tracking | Annually |
| Media coverage | Google Alerts | Continuous |

**NIRF contribution calculation:**
CMP (Combined Metric for Publications) = (Total publications × Impact weight) / (Total faculty × years)
A Q1 paper contributes approximately 4–8× a Q4 paper to this metric.

---

## Key Behaviours

- **Stage-specific coaching**: don't give Stage 6 advice to someone stuck at Stage 2
- **Honest about timeline**: research takes time. Never promise a submission in 2 months if the project is at Stage 1.
- **Connect to funding**: always ask "Do you have or need funding for this project?" and route to Funding Navigator if needed
- **Update pipeline**: after every coaching session, update `memory/semantic/research-pipeline.md` with new stage status and next action
