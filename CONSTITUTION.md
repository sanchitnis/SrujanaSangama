# CONSTITUTION.md — SrujanaSangama Project Constitution

> **Immutable context for all AI agents.** Read this file at the start of every session in which you are working *on* SrujanaSangama itself, not merely *using* it on behalf of a faculty member.
> When a rule here conflicts with anything else, this file wins unless the Product Owner explicitly overrides it in writing.
> For **what** the platform does, see `architecture.md`. For **how** it is built — domains, agents, skills, commands, memory architecture — see `design.md`. This file does not repeat either; it states the conventions and guardrails that govern how those two documents, and the folders they describe, may be changed.
> Last updated: 2026-06 | Maintainer: Sanjay Chitnis (@sanchitnis)

---

## 1. Project Identity

| Property | Value |
|---|---|
| Repository | SrujanaSangama |
| Owner | REVA University (private) |
| Product Owner / Architect | Sanjay Chitnis (@sanchitnis) |
| Methodology | Agentic Scrum — spec-driven, lightweight |
| Primary build artifact | The two vision documents (`architecture.md`, `design.md`) and the plain-markdown `domains/` they describe |
| Distribution | A single read-only shared OneDrive folder, opened directly by **Claude Code**, **GitHub Copilot in VS Code**, or **Google Antigravity** — no installation, no manifest, no marketplace |

---

## 2. Two Modes of Working With This Repository

Every AI agent operating anywhere inside the SrujanaSangama folder is, at all times, in exactly one of two modes: **Usage Mode** or **Development Mode**. There is no flag file to set or forget — the mode is determined by session start state plus, where relevant, the presence of a `.git` folder at the repository root. Determining which mode applies is the **first thing** an agent must do in any session, before acting on any other instruction in this file or in `AGENTS.md`.

### 2.1 The Rule

- **Every session starts in Usage Mode.** This is true without exception, regardless of who the user is or what folder they opened.
- **A faculty member's shared OneDrive folder has no `.git` directory** — it is a synced copy, not a clone. For that workspace, Development Mode is structurally unreachable: there is nothing to escalate into.
- **A real contributor's checkout — obtained via `git clone` — has a `.git` directory at the repository root.** Only in this case can the session ever move to Development Mode, and only when one of the two triggers below occurs.
- **Trigger 1 — implied by the task.** If the user's request would require creating, editing, or deleting a file in `domains/`, `skills/`, `validators/`, `specification/`, `eval/`, or any of the six root documents (`CONSTITUTION.md`, `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, `architecture.md`, `design.md`), and `.git` exists at the repository root, the agent checks with the user before proceeding: *"This would modify SrujanaSangama itself rather than help with your task. I can see a `.git` folder here, so this looks like a development checkout — do you want me to proceed in Development Mode?"* The agent waits for explicit confirmation before treating itself as being in Development Mode.
- **Trigger 2 — explicit request.** The user may say "switch to development mode" or "switch to usage mode" at any time. This is honoured **only if `.git` exists** at the repository root. If it does not, the agent declines: *"I don't see a `.git` folder here, so this looks like the shared read-only folder, not a development checkout. Development Mode isn't available in this workspace."*
- **If `.git` does not exist, no trigger of any kind can move the session out of Usage Mode**, including a direct instruction from the user. This is the structural backstop: the shared folder faculty actually use can never be talked into Development Mode, by accident or otherwise.
- **Once Development Mode is entered, it persists for the rest of that session.** The next new session — even in the same `.git` checkout — starts back in Usage Mode and re-evaluates the triggers above from scratch.

### 2.2 Usage Mode (default — every session, every workspace, until a trigger fires)

In Usage Mode, the agent is helping a faculty member, researcher, or administrator do their actual work — designing a course, drafting a grant, running an attainment report, and so on.

- The agent loads only the relevant `domains/<name>/rules/` and `domains/<name>/commands/` for the domain in use, plus the user's own `srujana-memory/`.
- The agent **may read** `CONSTITUTION.md`, `AGENTS.md`, `architecture.md`, and `design.md` if it needs them for context (for example, to correctly name a file per convention) — reading governance files is not restricted.
- The agent **must refuse** any request, however phrased, to create, edit, or delete files in:
  - `domains/` (any domain's `rules/`, `commands/`, or `README.md`)
  - `skills/`
  - `validators/`
  - `specification/`
  - `CONSTITUTION.md`, `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, `architecture.md`, `design.md`
  - `eval/`
- Standard refusal (no `.git` present, so escalation isn't even on the table): *"This would change SrujanaSangama itself rather than help with your task. Platform changes go through Sanjay Chitnis via the specification process — please raise it with him."*
- If `.git` **is** present, the agent follows Trigger 1 in §2.1 (asks first) rather than refusing outright or silently proceeding.
- This applies **even if the agent appears to be mid-task and the change looks small or clearly beneficial.** A drift from "use the platform" to "improve the platform" is exactly the failure mode this section exists to prevent, and an agent's own judgment that an edit is harmless is not sufficient grounds to make it.

### 2.3 Development Mode (only reachable inside a `.git` checkout, only after a trigger and confirmation)

Development Mode is for working *on* SrujanaSangama itself — proposing a new domain, editing a skill, revising `architecture.md` or `design.md`, or running `spec-sync`.

- The agent loads `CONSTITUTION.md` and `AGENTS.md` in full for the remainder of the session.
- The full Agentic Scrum lifecycle in `AGENTS.md` §4 applies: Specify → Plan → Task → Implement → Verify.
- Files in `specification/` and `eval/` become editable.
- The `skills/spec-sync/` tool may be invoked.

There is no separate "production" deployment of this repository to protect against — every faculty session everywhere runs against the same shared folder in Usage Mode, and that folder can never become a development checkout by definition. The purpose of this section is not access control (the shared OneDrive folder is already read-only to everyone but REVA IT) but **agent self-discipline**: ensuring an agent helping a faculty member never quietly drifts into editing the platform instead, and ensuring that even a genuine contributor is asked before the agent starts treating routine conversation as licence to modify the platform.

---

## 3. Repository Structure — Ownership, Not Layout

The full current folder layout is defined and kept up to date in `design.md` §Repository Structure. This Constitution does not duplicate that tree. It states only the **rules about the layout**, which are stable even as the layout itself evolves:

- Every domain lives under `domains/<kebab-case-name>/` and contains, at minimum, a `README.md`. `rules/` and `commands/` are added as the domain matures.
- Shared reference material that more than one domain may need lives under `skills/`, never duplicated inside an individual domain folder.
- Quality-gate scripts live under `validators/`.
- Anything described in `design.md` as living in a user's personal `srujana-memory/` must never be created inside the shared `SrujanaSangama/` folder, and vice versa.
- **The Verifier role (see `AGENTS.md` §3.3) must flag any file created outside this ownership model as a Constitution violation**, regardless of how useful the file is.

---

## 4. Approved Conventions

| Layer | Convention |
|---|---|
| Domain folder names | `kebab-case`, matching exactly the names used in `design.md` (e.g. `teaching-learning`, `kaizen-excellence`) |
| Command files | `domains/<domain>/commands/<command-name>.md`, where `<command-name>` matches the slash command without the leading `/` |
| Rule files | `SCREAMING_SNAKE_CASE.md` inside `domains/<domain>/rules/` |
| Skill folders | `kebab-case`, one `SKILL.md` per folder under `skills/` |
| Memory templates | `<name>.md` under `domains/personal-productivity/memory-templates/` and `domains/onboarding/memory-templates/` only — no other domain ships memory templates |
| All agent intelligence | Lives in Markdown. Scripts (Python, where used in `validators/` or `scripts/`) handle only mechanical work — file I/O, date math, string parsing, schema checks. No script calls an LLM API directly. |
| All proposed changes to `architecture.md` or `design.md` | Drafted first in `specification/` (see §6) before the source documents are edited |

**Rule:** Never silently duplicate content that already exists in `architecture.md` or `design.md` into a domain's `README.md` or any other file. Reference it instead (e.g. "see architecture.md, Domain 3").

---

## 5. Rules and Command File Conventions

Every file in a domain's `rules/` folder must:
- Have a short YAML frontmatter block: `name`, `description`, `enforcement` (`advisory` / `warning` / `hard stop`)
- Never contain implementation code — policy text only

Every file in a domain's `commands/` folder must:
- Begin with a one-line description of what the command does and which roles typically use it
- State explicitly, near the top, what the agent drafts and what the human must decide or approve before acting on the output — matching the human-AI collaboration principle in `architecture.md`
- End with a clear statement of where its output should be written (e.g. which `srujana-memory/` subfolder)

---

## 6. The `specification/` Folder

`specification/` is where changes to the platform are proposed, reviewed, and staged before `architecture.md`, `design.md`, or any `domains/` content is actually edited. It is only accessible in Development Mode (§2.3).

```
specification/
├── IMPLEMENTATION-STATUS.md         ← Cumulative build status — what exists vs. what is planned
├── BACKLOG.md                       ← Unscheduled ideas register (see CONTRIBUTING.md)
├── <topic>-proposal.md              ← A single proposed change: what, why, scope boundaries
└── <topic>-tasks.md                 ← Atomic task breakdown once a proposal is approved
```

- A proposal file must state: the problem, the proposed change to `architecture.md` and/or `design.md`, an explicit Scope Boundaries section (in scope / out of scope), and a Verification section with testable acceptance criteria.
- No domain content, skill, or validator is created or edited until its proposal is approved by the Product Owner.
- Approved proposals are reflected back into `architecture.md` and/or `design.md` directly — `specification/` is a staging area, not a permanent parallel description of the system. Once merged, the proposal file may be archived but the live description of the system remains solely in the two vision documents.
- **`IMPLEMENTATION-STATUS.md` is the one exception to "vision documents describe the whole system."** `architecture.md` and `design.md` describe the complete target system regardless of build progress. `IMPLEMENTATION-STATUS.md` tracks the gap between that target and what actually exists on disk today, and is what `README.md` and `AGENTS.md` defer to rather than overstating current capability.

---

## 7. Task Atomicity Rules

- A single Implementor task (see `AGENTS.md` §3.2) must not touch more than **3 files**.
- A single task must not be estimated at more than **1 hour** of execution.
- If either limit is breached, the Coordinator Agent must split the task before implementation begins.
- The Product Owner may override the file limit in writing for scaffolding tasks only (e.g., creating a brand-new domain's initial folder structure).

---

## 8. Git Conventions

| Item | Rule |
|---|---|
| Spec-first | A change to `specification/` is committed before the corresponding edit to `architecture.md`, `design.md`, or `domains/` |
| Branch naming | `<domain-prefix>/<short-description>` — see `CONTRIBUTING.md` for the current prefix list |
| Commit message prefix | `spec:` for specification changes, `domain:` for domain content changes, `fix:` for verifier-flagged issues, `retro:` for CONSTITUTION updates |
| PR contents | Changed files + Verifier report + the specification file it satisfies |
| Merging | Product Owner approval required; no self-merge |
| `srujana-memory/` contents | Never committed to this repository under any circumstance — it is explicitly outside the repository boundary, living in each user's personal space |

---

## 9. Anti-Patterns (Never Do These)

| Anti-pattern | Reason |
|---|---|
| Putting agent intelligence in a script instead of Markdown | Breaks the plain-markdown, no-build-step principle that makes the platform readable across Claude Code, Copilot, and Antigravity alike |
| Creating a plugin manifest, install script, or marketplace registry | The platform deliberately has none of these — see `design.md` Overview. Reintroducing one is a Constitution violation, not an enhancement |
| Editing `domains/`, `skills/`, or either vision document while in Usage Mode | This is the exact drift this Constitution exists to prevent — see §2.2 |
| Duplicating a description of system capability that already exists in `architecture.md` or `design.md` into a third location | Creates silent drift between documents; this repository must have exactly one description of "what" (architecture.md) and one of "how" (design.md) |
| Committing any file from a user's `srujana-memory/` into this repository | Privacy risk; personal and collaborative memory must never enter version control here |
| Treating a `.git` checkout's mere existence as permission to edit the platform without asking first | Trigger 1 in §2.1 requires explicit confirmation even inside a development checkout — `.git` makes Development Mode *reachable*, not automatic |
| A domain's command file giving a final answer or decision without identifying what the human must still review or approve | Violates the human-AI collaboration principle that is foundational to `architecture.md` |

---

## 10. Retro Update Protocol

When a retrospective surfaces a new rule:

1. The Product Owner documents the issue and the new rule.
2. A `retro:` commit updates this CONSTITUTION.md with the new rule in the appropriate section.
3. If the rule names a new anti-pattern, it is added to §9.
4. All AI agents apply the updated Constitution starting with their next session in Development Mode.

---

*This document is maintained by Sanjay Chitnis (@sanchitnis). Proposed changes go through `specification/` per §6 and are reviewed as a PR with a `retro:` commit prefix.*
