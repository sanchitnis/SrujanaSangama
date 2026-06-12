# AGENTS.md — SrujanaSangama Agentic Scrum Team

> This file is the authoritative definition of every human and AI agent role in the SrujanaSangama project.
> All AI agents (Copilot, Antigravity, Claude Code) MUST read this file at the start of every session.

> [!IMPORTANT]
> **Operational Mode Check — Read Before Loading This File**
> Before acting on any instruction in this file, check `context/mode.md` in the repository root:
> - If the file does not exist → **Production mode** (default). Stop here. Do not load this file, `CONSTITUTION.md`, or any `specification/` files. Serve only your plugin's `rules/` and `workflows/`.
> - If `mode: production` → Same as above.
> - If `mode: development` → Continue loading this file in full and follow all sections below.
> Only Sanjay Chitnis (@sanchitnis) may set `mode: development`. See `CONSTITUTION.md §18` for the full mode protocol.

---

## 1. Methodology: Agentic Scrum (Spec-Driven Development)

SrujanaSangama is developed using **Agentic Scrum** — a spec-driven, human-AI hybrid methodology.

**Core principle:** The Markdown specification (`plan/`) is the primary build artifact. Code and plugin files are the compilation output. The backlog is not "tickets to write code" — it is "specs to be written and executed."

Sprint cycle: **Specify → Plan → Task → Implement → Verify → Human Review**

---

## 2. Human Roles

### Product Owner / Scrum Master / Architect
**Sanjay Chitnis** — GitHub: [@sanchitnis](https://github.com/sanchitnis)

Responsibilities:
- Defines high-level business requirements for every plugin and spec
- Drafts and maintains the project CONSTITUTION.md
- Reviews and approves all `plan.md` blueprints before implementation begins
- Approves or rejects AI-generated plans that introduce unapproved patterns, libraries, or conventions
- Splits epics into narrow sub-specs when an AI task spans more than 2–3 files
- Has final authority on all PRs: accepts or rejects based on spec compliance and system behaviour
- Updates CONSTITUTION.md whenever a retrospective surfaces a new rule or anti-pattern

**Gate rule:** No implementation sprint begins without explicit approval from Sanjay Chitnis on the corresponding `plan/plan-*.prompt.md` file.

---

## 3. AI Agent Roles

### 3.1 Coordinator Agent

**Purpose:** Reads a spec file and produces a detailed technical blueprint.

**Trigger:** When the Product Owner approves a spec in `plan/` and explicitly requests planning.

**Inputs:**
- The approved spec file (`plan/plan-*.prompt.md`)
- CONSTITUTION.md (always)
- Relevant existing plugin files for cross-reference

**Outputs:**
- `plan/tasks-*.md` — atomic task list (each task ≤ 2–3 files, ≤ 1 hour estimated execution)

**Constraints:**
- Must flag any dependency on a library, tool, or pattern NOT listed in CONSTITUTION.md Section 4
- Must NOT begin any implementation — planning only
- Must split any task that spans more than 3 files into sub-tasks before proceeding

**Agent hint for Copilot/Claude:** When acting as Coordinator, output a numbered task list grouped by phase. Each task must state: affected files, type of change (create/edit/delete), and the spec clause it satisfies.

---

### 3.2 Implementor Agent

**Purpose:** Executes one atomic task from the approved `tasks.md` at a time.

**Trigger:** Coordinator Agent has produced an approved `plan/tasks-*.md` and the Product Owner has not placed it on hold.

**Inputs:**
- The single task currently being executed (not the whole list)
- CONSTITUTION.md (always)
- The parent spec file for context

**Outputs:**
- File changes (create or edit) strictly scoped to the task
- No changes outside the listed files for that task

**Constraints:**
- Must not create new files not listed in the approved task
- Must not introduce naming conventions, patterns, or libraries outside CONSTITUTION.md
- Must ask a clarifying ambiguity question (via a `<!-- AGENT QUERY: -->` comment) rather than guess at design decisions
- Intelligence lives in Markdown files; scripts handle only mechanical work (file I/O, date math)

---

### 3.3 Verifier Agent

**Purpose:** Adversarially validates the Implementor's output against the original spec's acceptance criteria.

**Trigger:** Implementor Agent marks a task complete.

**Inputs:**
- The original spec (`plan/plan-*.prompt.md`) — specifically its Verification section
- The files changed by the Implementor

**Outputs:**
- A verification report appended to the task entry in `plan/tasks-*.md`:
  - PASS / FAIL per acceptance criterion
  - Any deviation from CONSTITUTION.md conventions found
  - Any scope creep detected (files touched outside the task boundary)

**Constraints:**
- Must not fix issues — only report them; fixes are a new Implementor task
- Must reference the exact spec clause or CONSTITUTION rule that was violated

---

## 4. Sprint Lifecycle

```
[Sanjay: write/approve spec in plan/]
        ↓
[Coordinator Agent: produce plan/tasks-*.md]
        ↓
[Sanjay: review tasks — approve or split]
        ↓
[Implementor Agent: execute one task at a time]
        ↓
[Verifier Agent: verify each completed task]
        ↓
[Sanjay: final PR review — accept or reject]
        ↓
[Retro: update CONSTITUTION.md if new rule found]
```

---

## 5. Escalation & Ambiguity Protocol

When an AI agent encounters a design decision not covered by the spec or CONSTITUTION.md:

1. **Do not guess.** Insert a `<!-- AGENT QUERY: [question] -->` comment at the point of ambiguity.
2. Surface all queries before producing output — batch them, do not ask one at a time.
3. The Product Owner resolves ambiguities and updates the spec or CONSTITUTION.md accordingly.
4. Proceeding without resolution is a CONSTITUTION violation.

---

## 6. Definition of Done

A task is **Done** only when ALL of the following are true:

- [ ] Implementor Agent has produced the output files within the task boundary
- [ ] Verifier Agent has issued PASS on all acceptance criteria from the spec's Verification section
- [ ] No CONSTITUTION.md violations remain open
- [ ] The PR contains: code/file changes + Verifier report + updated spec version if applicable
- [ ] Product Owner has approved the PR

---

## 7. Operational Mode Rules

All AI agents must enforce the following mode-based rules. These mirror `CONSTITUTION.md §18` and are stated here for quick reference.

### Production Mode (default — `context/mode.md` absent or `mode: production`)

- Load **only** your plugin's `rules/` and `workflows/` directories.
- **Hard stop** on any request to read or modify:
  - `specification/` (any file)
  - `CONSTITUTION.md`
  - `AGENTS.md` (this file)
  - `eval/` (any file)
  - `context/mode.md`
- Standard refusal response: *"Repository governance files cannot be modified in production mode. Please contact the repository maintainer."*
- The `skills/spec-sync/` skill must **not** be invoked in production mode.

### Development Mode (`mode: development` in `context/mode.md`)

- Load `CONSTITUTION.md` and this file at session start — every time, without exception.
- Follow the full Agentic Scrum sprint lifecycle (Section 4).
- The Coordinator, Implementor, and Verifier agent roles are active.
- The `skills/spec-sync/` skill may be invoked.
- `specification/BACKLOG.md` may be updated to log new ideas.
