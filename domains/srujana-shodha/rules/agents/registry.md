# Agent Registry — SrujanaShodha
_Last updated: 2026-05-29_
_How to use: Orchestrator reads this to route faculty requests. Trigger Description is the signal that routes to that agent._

---

## Core Agents (system — always active)

| ID | Name | Agent File | Trigger Description |
|----|------|-----------|---------------------|
| C01 | Orchestrator | `agents/core/orchestrator.md` | [always active — entry point for all messages] |
| C02 | Memory Steward | `agents/core/memory-steward.md` | remember, forget, note that, what do you know about me, update my profile, I always, store this, what have you learned, my pipeline status |

---

## Specialist Agents — Research Advisory

| ID | Name | Agent File | Trigger Description |
|----|------|-----------|---------------------|
| R01 | Competency Profiler | `agents/skills/competency-profiler.md` | profile my competencies, what am I good at, what's my research identity, map my expertise, research strengths, what do I know deeply, zone map |
| R02 | Opportunity Scout | `agents/skills/opportunity-scout.md` | research idea, what should I research, find me a topic, research opportunity, where is the gap, what's worth publishing, new direction, research problem |
| R03 | Collaboration Architect | `agents/skills/collaboration-architect.md` | find collaborators, who should I work with, build a team, interdisciplinary, collaboration, partner, MoU, joint research, external collaborator, international partnership |
| R04 | Funding Navigator | `agents/skills/funding-navigator.md` | funding, grant, apply for grant, DST, DBT, UGC, SERB, AICTE, ICSSR, VGST, CSR, industry funding, international grant, fellowship, how do I get funded, find a grant |
| R05 | Research Pipeline Coach | `agents/skills/research-pipeline-coach.md` | plan my research, research design, methodology, how do I structure my project, research timeline, project stages, what next, data collection, literature review strategy |
| R06 | Journal Targeter | `agents/skills/journal-targeter.md` | where should I publish, target journal, best journal for my paper, which journal, conference to submit, journal recommendation, publication venue, submission target |
| R07 | Work Product Reviewer | `agents/skills/work-product-reviewer.md` | review my paper, check my abstract, feedback on my proposal, audit my manuscript, critique my work, review this draft, is this good enough, improve my writing |
| R08 | Personal Brand Builder | `agents/skills/personal-brand-builder.md` | build my brand, improve my profile, ORCID, Google Scholar, LinkedIn, ResearchGate, visibility, how do I get recognised, academic brand, researcher profile, citations |
| R09 | arXiv Searcher | `agents/skills/arxiv-searcher.md` | arxiv, literature search, find papers on arxiv, download paper, search literature, fetch arxiv paper, get paper source |

---

## Specialist Agents — Scholar Lifecycle & Support

| ID | Name | Agent File | Trigger Description |
|----|------|-----------|---------------------|
| S01 | Topic Scout | `agents/scholar/topic-scout.md` | find a guide, guide eligibility, topic mapping, topic feasibility, check guide vacancy |
| S02 | Coursework Navigator | `agents/scholar/coursework-navigator.md` | coursework credits, IA exams, CWEE prep, coursework routing, credit requirements |
| S03 | Synopsis Builder | `agents/scholar/synopsis-builder.md` | pre-registration colloquium, synopsis structure, synopsis template, synopsis defense |
| S04 | Research Coach | `agents/scholar/research-coach.md` | lit review strategy, methodology selection, research design, PRISMA, research logging |
| S05 | Publication Coach | `agents/scholar/publication-coach.md` | target journal selection, manuscript drafting, paper response coaching, publication tracker |
| S06 | Thesis Writer | `agents/scholar/thesis-writer.md` | thesis writing, formatting checklist, anti-plagiarism check, chapter draft, colloquium |
| S07 | Patent Agent | `agents/scholar/patent-agent.md` | patent filing, IP screening, Form 1/2/3 helper, patent-generator check |
| S08 | Grant Agent | `agents/scholar/grant-agent.md` | PhD fellowship, SERB JRF, DST fellowship, ICMR fellowship, seed grant proposal |
| S09 | Book Agent | `agents/scholar/book-agent.md` | book monograph, publisher target, book proposal, monograph chapter outline |
| S10 | Daily Planner | `agents/scholar/daily-planner.md` | weekly schedule, daily micro-tasks, task planning, milestone breakdown |
| S11 | Blocker Breaker | `agents/scholar/blocker-breaker.md` | stuck, blocker triage, conceptual obstacle, technical block, guide communication |
| S12 | Wellness Companion | `agents/scholar/wellness-companion.md` | wellness check, stress, fatigue, burnout, imposter syndrome, mental health |
| S13 | Ikigai Compass | `agents/scholar/ikigai-compass.md` | ikigai audit, research alignment, personal values check, passion mapping |
| S14 | Guide Advisor | `agents/guide/guide-advisor.md` | supervisor dashboard, scholar roster, scholar progress alerts, feedback template |

---

## Workflow Prompts (multi-step — paste directly, no routing needed)

### Faculty-facing Workflows
| ID | Name | Workflow File | When to Use |
|----|------|--------------|-------------|
| W01 | Onboarding | `workflows/onboarding.md` | First-time setup — competency profiling + memory initialisation |
| W02 | Opportunity Mapping | `workflows/opportunity-mapping.md` | After onboarding — structured research opportunity discovery |
| W03 | Funding Hunt | `workflows/funding-hunt.md` | Deep-dive into funding options for a specific research topic |
| W04 | Research Lifecycle | `workflows/research-lifecycle.md` | End-to-end project planning from idea to publication |
| W05 | Brand Sprint | `workflows/brand-sprint.md` | 90-day structured personal brand building programme |
| W06 | SDG Impact Audit | `workflows/sdg-impact-audit.md` | Audit a body of work against SDG + NEP 2020 indicators |
| W07 | Grant Check | `workflows/grant-check.md` | Review and improve a grant proposal draft |
| W08 | Manuscript Check | `workflows/manuscript-check.md` | Full peer-review-style manuscript audit |
| W09 | Proposal Check | `workflows/proposal-check.md` | Research/funding proposal compliance audit |
| W10 | Session Closer | `workflows/session-closer.md` | End-of-session memory update and next-action capture |

### Scholar-facing Workflows
| ID | Name | Workflow File | When to Use |
|----|------|--------------|-------------|
| W11 | Onboarding (Scholar) | `workflows/00_onboarding.md` | Setup scholar profile, registration date, guide, and stage |
| W12 | Entrance Prep | `workflows/01_entrance-prep.md` | Mock interviews, presentation prep, admission research |
| W13 | Coursework | `workflows/02_coursework.md` | Course tracking, IA assessments, credit floors checks |
| W14 | Synopsis | `workflows/03_synopsis.md` | Colloquium prep, synopsis outline and defense preparation |
| W15 | Research Cycle | `workflows/04_research-cycle.md` | Literature mapping, experiments, and logging |
| W16 | Publication Pipeline | `workflows/05_publication-pipeline.md` | Paper draft writing, target journal selection, and tracker |
| W17 | Thesis Sprint | `workflows/06_thesis-sprint.md` | Thesis formatting, plagiarism check, and viva defense prep |
| W18 | Patent Workflow | `workflows/07_patent-workflow.md` | Identifying patentable IP, draft helper for Forms 1/2/3 |
| W19 | Grant Proposal | `workflows/08_grant-proposal.md` | Doctoral fellowship proposals and seed grant calendar checks |
| W20 | Book Proposal | `workflows/09_book-proposal.md` | Book proposal layout and academic publisher targeting |
| W21 | Guide Dashboard | `workflows/10_guide-dashboard.md` | Supervisor view of roster status, alert thresholds, and logs |
| W22 | Session Closer (Scholar) | `workflows/11_session-closer.md` | Capture commitments, task list refresh, and wrap-up |
| W23 | Daily Standup | `workflows/12_daily-standup.md` | Daily 3-point standup: yesterday, today, blockers |
| W24 | Stuck Triage | `workflows/13_stuck-triage.md` | Blocker pathing for conceptual or regulatory issues |
| W25 | Wellness Checkin | `workflows/14_wellness-checkin.md` | Mentorship wellbeing logs and stress checks |
| W26 | Ikigai Audit | `workflows/15_ikigai-audit.md` | Scholar research alignment maps and annual audits |

---

## Auto-Generated Agents
_Populated as new skills are created_

| ID | Name | Agent File | Tags | Date |
|----|------|-----------|------|------|
| — | — | — | — | — |

---

## Registry Stats
- Core agents: 2
- Specialist agents: 23 (9 Faculty + 14 Scholar)
- Workflow prompts: 26 (10 Faculty + 16 Scholar)
- Auto-generated: 0

---

## How to Add a New Agent
1. Define the agent's trigger description and domain
2. Create `agents/skills/[agent-name].md` or `agents/scholar/[agent-name].md` following the YAML frontmatter pattern
3. Add one row to the appropriate Specialist Agents table above
4. The Orchestrator will immediately route to it on next session load
