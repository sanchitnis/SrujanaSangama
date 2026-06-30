# Agent Registry
_Last updated: 2026-05-08_
_How to use: Orchestrator reads this to route requests. Trigger Description is the routing signal._

---

## Core Agents (system — always active)

| ID  | Name | Skill File | Prompt File | Trigger Description |
|-----|------|-----------|-------------|---------------------|
| C01 | Orchestrator | `agents/core/orchestrator.md` | `prompts/session/ORCHESTRATOR.md` | [always active — entry point for all messages] |
| C02 | Memory Steward | `agents/core/memory-steward.md` | `prompts/agents/MEMORY_STEWARD.md` | remember, forget, note that, what do you know about me, update my profile, I always, store this, what have you learned |
| C03 | Persona Engine | `agents/core/persona-engine.md` | [internal — no direct prompt] | [injected into every agent call automatically] |
| C04 | Skill Generator | `agents/core/skill-generator.md` | `prompts/workflows/SKILL_GENERATOR.md` | create an agent, add a skill, build a specialist, generate a skill, I need a tool for |
| C05 | Permission Guardian | `agents/core/permission-guardian.md` | [internal — no direct prompt] | [triggered by any state-changing action] |

---

## Specialist Agents — Productivity

| ID  | Name | Skill File | Prompt File | Trigger Description |
|-----|------|-----------|-------------|---------------------|
| S01 | Writing Partner | `agents/skills/writing-partner.md` | `prompts/agents/WRITING_PARTNER.md` | write, draft, email, letter, report, edit, proofread, agenda, document, blog, article, proposal, message, summarise |
| S02 | Research Analyst | `agents/skills/research-analyst.md` | `prompts/agents/RESEARCH_ANALYST.md` | research, find out, what is, explain, compare, analyse, benchmark, fact-check, what do experts say, latest on, overview of |
| S03 | Task Manager | `agents/skills/task-manager.md` | `prompts/agents/TASK_MANAGER.md` | task, todo, remind, deadline, schedule, plan, pending, overdue, milestone, follow up, priority, blocked, what should I do |

---

## Specialist Agents — Technical

| ID  | Name | Skill File | Prompt File | Trigger Description |
|-----|------|-----------|-------------|---------------------|
| T01 | Code Architect | `agents/skills/code-architect.md` | `prompts/agents/CODE_ARCHITECT.md` | code, script, function, debug, fix error, review code, refactor, implement, algorithm, test, SQL, regex, CLI, API |
| T02 | Data Interpreter | `agents/skills/data-interpreter.md` | `prompts/agents/DATA_INTERPRETER.md` | data, CSV, spreadsheet, chart, visualise, plot, trend, pattern, anomaly, dataset, correlation, numbers, analyse this file |

---

## Specialist Agents — Learning & Growth

| ID  | Name | Skill File | Prompt File | Trigger Description |
|-----|------|-----------|-------------|---------------------|
| L01 | Learning Coach | `agents/skills/learning-coach.md` | `prompts/agents/LEARNING_COACH.md` | teach me, learn, quiz, practice, study plan, step by step, I want to understand, test my knowledge, flashcard, spaced repetition |
| L02 | Reflection Facilitator | `agents/skills/reflection-facilitator.md` | `prompts/agents/REFLECTION_FACILITATOR.md` | reflect, journal, how am I doing, weekly review, look back, what changed, retrospective, I've been thinking, processing |
| L03 | Habit Tracker | `agents/skills/habit-tracker.md` | `prompts/agents/HABIT_TRACKER.md` | habit, streak, check in, log it, I just did, routine, every day, mark as done, I completed, how's my streak |
| L04 | Idea Incubator | `agents/skills/idea-incubator.md` | `prompts/agents/IDEA_INCUBATOR.md` | brainstorm, idea, what if, explore, imagine, possibilities, how might we, creative, innovate, rethink, alternatives, thought experiment |

---

## Specialist Agents — Domain Extensions

| ID  | Name | Skill File | Prompt File | Trigger Description |
|-----|------|-----------|-------------|---------------------|
| D01 | Academic Advisor | `agents/skills/academic-leadership-advisor.md` | `prompts/agents/ACADEMIC_ADVISOR.md` | academic council, accreditation, NBA, NAAC, NIRF, UGC, AICTE, NEP, programme approval, faculty load, policy draft, curriculum committee, senate, regulatory |

---

## Specialist Agents — Technical Automation

| ID  | Name | Skill File | Prompt File | Trigger Description |
|-----|------|-----------|-------------|---------------------|
| T03 | Computer Agent | `agents/skills/computer-agent.md` | `prompts/agents/COMPUTER_AGENT.md` | run this, execute, open file, create folder, move file, rename, delete, list files, find files, read this file, write to file, copy, what's in this folder, run my script |
| T04 | Web Agent | `agents/skills/web-agent.md` | `prompts/agents/WEB_AGENT.md` | search for, look up online, go to website, fetch this URL, what does this page say, check if this site, find on the web, latest news about, scrape, download from |

---

## Specialist Agents — CEE (Chief Execution Engine)

| ID  | Name | Skill File | Prompt File | Trigger Description |
|-----|------|-----------|-------------|---------------------|
| E01 | CEE Triage Agent | `agents/skills/cee-triage-agent.md` | `prompts/agents/CEE_TRIAGE.md` | inbox, dump this, process these notes, triage, I got an email, meeting notes, sort this, what do I do with, capture, here is my dump, clear my inbox, quick triage |
| E02 | CEE Briefing Agent | `agents/skills/cee-briefing-agent.md` | `prompts/agents/CEE_BRIEFING.md` | morning briefing, daily brief, today's focus, today's priorities, weekly audit, weekly review CEE, Friday wrap, Sunday review, drift report, focus metrics, how am I doing against my objectives |

---

## Workflow Prompts (multi-step — paste directly, no routing needed)

| ID  | Name | Prompt File | When to use |
|-----|------|-------------|-------------|
| W01 | Weekly Review | `prompts/workflows/WEEKLY_REVIEW.md` | End of week — reflects, reviews tasks/habits, sets next-week priorities |
| W02 | Project Kickoff | `prompts/workflows/PROJECT_KICKOFF.md` | Starting a new project — defines, decomposes, captures tasks |
| W03 | Deep Research | `prompts/workflows/DEEP_RESEARCH.md` | Multi-angle systematic research with structured brief output |
| W04 | Skill Generator | `prompts/workflows/SKILL_GENERATOR.md` | Creating a new specialist agent SKILL.md file |
| W05 | Morning Briefing | `workflows/07_morning-briefing.md` | Daily CEE briefing — paste at session start or via Gemini /schedule 6 AM |
| W06 | Weekly Alignment Audit | `workflows/08_weekly-alignment-audit.md` | End-of-week 7-phase audit — triggered post-Friday 6 PM IST or Sat/Sun |
| W07 | Onboarding | `workflows/00_onboarding.md` | First-time setup for a new faculty member |
| W08 | Session Closer | `workflows/session-closer.md` | Close a session — produce SESSION_SUMMARY block for update_memory.py |

---

## Auto-Generated Agents
_Populated by Skill Generator as new skills are created_

| ID  | Name | Skill File | Prompt File | Tags | Generated | Date |
|-----|------|-----------|-------------|------|-----------|------|
| —   | —    | —         | —           | —    | —         | —    |

---

## Registry Stats
- Core agents: 5
- Specialist agents: 9 (productivity) + 2 (technical: T01/T02) + 2 (automation: T03/T04) + 1 (domain: D01) = **14**
- CEE agents: 2
- Workflow prompts: 8 (W01–W08)
- Auto-generated: 0
- Deprecated: 0

---

## How to Add a New Agent

1. Paste `prompts/workflows/SKILL_GENERATOR.md` into Claude with the agent description
2. Claude outputs: `agents/skills/[name].md` + `prompts/agents/[NAME].md`
3. Save both files to the correct directories
4. Add one row to this registry table
5. New agent is immediately available for routing
