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

---

## Workflow Prompts (multi-step — paste directly, no routing needed)

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

---

## Auto-Generated Agents
_Populated as new skills are created_

| ID | Name | Agent File | Tags | Date |
|----|------|-----------|------|------|
| — | — | — | — | — |

---

## Registry Stats
- Core agents: 2
- Specialist agents: 8
- Workflow prompts: 10
- Auto-generated: 0

---

## How to Add a New Agent
1. Define the agent's trigger description and domain
2. Create `agents/skills/[agent-name].md` following the YAML frontmatter pattern
3. Add one row to the Specialist Agents table above
4. The Orchestrator will immediately route to it on next session load
