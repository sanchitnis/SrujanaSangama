# AGENTS.md — SrujanaSangama Agentic Scrum Team

> This file defines every human and AI agent **role involved in building and maintaining SrujanaSangama itself**. It is not about the domain agents faculty use day to day — those are defined in `design.md`. This file is only relevant in **Development Mode** (see `CONSTITUTION.md` §2).

> [!IMPORTANT]
> **Mode Check — Read Before Acting on Anything Below**
> Before following any instruction in this file, determine your mode as described in `CONSTITUTION.md` §2.
> - No `.git` folder at the repository root → **Stop here.** This is the shared faculty workspace; Development Mode is unreachable. Help the user with their actual task using the relevant domain in `domains/`.
> - `.git` folder present, but the user hasn't asked for or triggered a platform change → **Stop here for now.** Stay in Usage Mode until Trigger 1 or Trigger 2 in `CONSTITUTION.md` §2.1 actually fires and is confirmed.
> - `.git` present and Development Mode has been confirmed for this session → Continue reading this file in full and follow the sprint lifecycle below.

---

## 1. Methodology: Agentic Scrum (Spec-Driven, Lightweight)

SrujanaSangama's platform itself — `architecture.md`, `design.md`, and the `domains/` they describe — is developed using **Agentic Scrum**: a spec-driven, human-AI hybrid methodology, kept deliberately light because the platform itself is plain markdown with no build step.

**Core principle:** `specification/` is where a change is proposed and reasoned about. `architecture.md`, `design.md`, and `domains/` are the compilation output once a proposal is approved. The backlog is not "tickets to write code" — it is "proposals to be written, approved, and reflected into the two vision documents and the domains they describe."

Sprint cycle: **Specify → Plan → Task → Implement → Verify → Human Review**

---

## 2. Human Roles

### Product Owner / Architect
**Sanjay Chitnis** — GitHub: [@sanchitnis](https://github.com/sanchitnis)

Responsibilities:
- Owns `architecture.md` (the what) and `design.md` (the how) and is the only person who approves a change to either
- Reviews and approves every `specification/<topic>-proposal.md` before any Coordinator planning begins
- Splits a proposal into narrower sub-proposals when it would otherwise touch more than 2–3 domains at once
- Has final authority on all PRs: accepts or rejects based on alignment with `architecture.md`, technical soundness per `design.md`, and Constitution compliance
- Updates `CONSTITUTION.md` whenever a retrospective surfaces a new rule or anti-pattern
- Is the architect of the mode boundary in `CONSTITUTION.md` §2 and the final word whenever an agent surfaces an ambiguous escalation request

**Gate rule:** No implementation begins without explicit Product Owner approval on the corresponding `specification/<topic>-proposal.md`.

---

## 3. AI Agent Roles (Development Mode only)

### 3.1 Coordinator Agent

**Purpose:** Reads an approved proposal and produces a detailed, atomic task breakdown.

**Trigger:** The Product Owner has approved a proposal in `specification/` and explicitly requests planning.

**Inputs:**
- The approved proposal (`specification/<topic>-proposal.md`)
- `CONSTITUTION.md` (always)
- `architecture.md` and `design.md` for cross-reference, so the task breakdown stays consistent with the rest of the platform

**Outputs:**
- `specification/<topic>-tasks.md` — an atomic task list (each task ≤ 3 files, ≤ 1 hour estimated execution, per `CONSTITUTION.md` §7)

**Constraints:**
- Must flag any proposed convention, naming pattern, or folder placement that is not already sanctioned in `CONSTITUTION.md` §3–§5
- Must NOT begin any implementation — planning only
- Must split any task spanning more than 3 files into sub-tasks before proceeding

**Agent hint:** Output a numbered task list grouped logically (e.g. by domain or by document). Each task must state: affected files, type of change (create/edit/delete), and which line of the proposal it satisfies.

---

### 3.2 Implementor Agent

**Purpose:** Executes one atomic task from an approved `specification/<topic>-tasks.md` at a time.

**Trigger:** The Coordinator Agent has produced an approved task list and the Product Owner has not placed it on hold.

**Inputs:**
- The single task currently being executed (not the whole list)
- `CONSTITUTION.md` (always)
- The parent proposal for context

**Outputs:**
- File changes strictly scoped to the task — typically an edit to `architecture.md`, `design.md`, or a file inside a `domains/<name>/` folder

**Constraints:**
- Must not create files not listed in the approved task
- Must not introduce a convention, pattern, or folder layout outside `CONSTITUTION.md`
- Must ask a clarifying question via a `<!-- AGENT QUERY: -->` comment rather than guess at a design decision
- Must not let an edit to `domains/` content drift into restating material that already lives in `architecture.md` or `design.md` — link or reference instead, per `CONSTITUTION.md` §4

---

### 3.3 Verifier Agent

**Purpose:** Adversarially validates the Implementor's output against the proposal's acceptance criteria and the Constitution.

**Trigger:** The Implementor Agent marks a task complete.

**Inputs:**
- The original proposal (`specification/<topic>-proposal.md`) — specifically its Verification section
- The files changed by the Implementor

**Outputs:**
- A verification report appended to the task entry in `specification/<topic>-tasks.md`:
  - PASS / FAIL per acceptance criterion
  - Any deviation from `CONSTITUTION.md` found
  - Any scope creep detected (files touched outside the task boundary)
  - Any duplication introduced between `architecture.md`, `design.md`, and a domain file

**Constraints:**
- Must not fix issues — only report them; fixes are a new Implementor task
- Must cite the exact proposal clause or Constitution section violated

---

## 4. Sprint Lifecycle

```
[Sanjay: write/approve a proposal in specification/]
        ↓
[Coordinator Agent: produce specification/<topic>-tasks.md]
        ↓
[Sanjay: review tasks — approve or split]
        ↓
[Implementor Agent: execute one task at a time]
        ↓
[Verifier Agent: verify each completed task]
        ↓
[Sanjay: final PR review — accept or reject]
        ↓
[Retro: update CONSTITUTION.md if a new rule was found]
```

---

## 5. Escalation & Ambiguity Protocol

When an AI agent in Development Mode encounters a design decision not covered by the proposal or `CONSTITUTION.md`:

1. **Do not guess.** Insert a `<!-- AGENT QUERY: [question] -->` comment at the point of ambiguity.
2. Surface all queries before producing output — batch them, do not ask one at a time.
3. The Product Owner resolves ambiguities and updates the proposal or `CONSTITUTION.md` accordingly.
4. Proceeding without resolution is a Constitution violation.

This protocol also applies, with higher stakes, to the boundary described in `CONSTITUTION.md` §2.2: if an agent in **Usage Mode** finds itself reasoning about whether an edit to the platform "would probably be fine," that reasoning is itself the signal to stop and refuse, not a basis for proceeding.

---

## 6. Definition of Done

A task is **Done** only when ALL of the following are true:

- [ ] The Implementor Agent has produced output files strictly within the task boundary
- [ ] The Verifier Agent has issued PASS on every acceptance criterion in the proposal's Verification section
- [ ] No Constitution violations remain open
- [ ] No content has been duplicated between `architecture.md`, `design.md`, and any domain file
- [ ] The PR contains: file changes + Verifier report + the proposal it satisfies
- [ ] `specification/IMPLEMENTATION-STATUS.md` has been updated to reflect the new status of whatever was built (see §7)
- [ ] If the change makes a domain newly **Implemented**, `README.md` and/or this file have been updated per §7 to mention it
- [ ] The Product Owner has approved the PR

---

## 7. Keeping `README.md` and This File Honest About What Exists

`architecture.md` and `design.md` describe the complete target system, regardless of build progress — that is their job, and they do not change as implementation proceeds, only as the vision itself evolves.

`README.md` and this file are different: they are **operational entry points**, and they must only describe what a person can actually do today. Specifically:

- `README.md`'s setup steps and "what's in this repository" table must only name domains, commands, and folders that are marked **Implemented** in `specification/IMPLEMENTATION-STATUS.md`.
- Anything **Not started** or **In progress** is summarised in one line at most (e.g. "more domains are being built — see `specification/IMPLEMENTATION-STATUS.md` for current status") rather than described in detail.
- This file's role descriptions (Coordinator, Implementor, Verifier) are process roles and are always fully described regardless of build status, since the process itself is already in effect — it is the *target system* (domains, commands) that gets the implemented-only treatment, not the *governance process* used to build it.
- Whenever a task completes and changes a domain's status, the Implementor or the closing PR must check whether `README.md` needs a new line added — this is part of Definition of Done (§6) and the PR checklist in `CONTRIBUTING.md`.
- Never backfill detail into `README.md` ahead of the actual build — if a domain is **In progress**, it stays out of README's setup steps until it reaches **Implemented**, even if a contributor is confident it will land soon.

---

## 8. Where This Fits With the Other Documents

| Document | Read by AI agents | When |
|---|---|---|
| `architecture.md` | Always, when context about platform capability is needed | Usage Mode and Development Mode |
| `design.md` | Always, when context about folders, agents, or commands is needed | Usage Mode and Development Mode |
| `CONSTITUTION.md` | Always, to determine mode and conventions | Both, but enforcement of its restrictions applies only in Usage Mode |
| `AGENTS.md` (this file) | In full | Development Mode only |
| `README.md` | By humans, as the entry point; agents do not need to load it separately | N/A |
| `CONTRIBUTING.md` | By human contributors setting up a development environment; referenced by agents only if a contributor mechanic (branch naming, PR checklist) is in question | Development Mode |
| `specification/IMPLEMENTATION-STATUS.md` | Whenever an agent needs to know what currently exists, or after completing a task that changes that status | Development Mode |
| `LOOPS.md` and `loops/*.md` | By humans running a specific loop (Product, Telemetry, etc.); agents reference a loop charter only if a contributor asks how their current work fits the wider process | Development Mode, and by loop owners outside any agent session entirely (e.g. the Business & Institutional Analysis Loop runs largely as human conversation) |
