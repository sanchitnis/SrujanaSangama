# AGENTS.md - SrujanaSangama Router

This file is the cross-IDE entry instruction for agents working in the SrujanaSangama repository. Its main job is to route context cheaply and safely.

---

# PART A: Usage Mode Router (For Regular Users - DEFAULT)

All sessions start in Usage Mode. If you do not detect a `.git` folder at the repository root, you must remain in Usage Mode.

## 1. Mandatory Constraints for Usage Mode
* **Do NOT read** `CONSTITUTION.md`, `CONTRIBUTING.md`, `IMPLEMENTATION-STATUS.md`, or any files in the following folders: `specification/`, `eval/`, `validators/`, `web/`, or `scripts/`.
* **Do NOT read Part B** of this file. You must stop reading `AGENTS.md` right at the end of Part A.
* **Do NOT modify** any files within the `SrujanaSangama/` folder. All personal profiles, session logs, outputs, and memory states must be read from and written to `../srujana-memory/`.
* **Read-Only Sibling folders**: You may read files in `../reva-information/` only when explicitly needed for a task.
* **Always Use Relative Paths**: You must always use relative paths (e.g., `../srujana-memory/`, `../reva-information/`) rather than absolute paths in all files, commands, rules, and links to ensure user-independence across different systems.

## 2. Onboarding Check (First-Time Users)
If the user's personal memory in `../srujana-memory/` does not exist or onboarding has not happened:
- Do not proceed with other tasks. 
- Prompt the user to run `/onboard` to set up their workspace.
- Guide them step-by-step to initialize their profiles.

## 3. Context Routing Protocol
When a request is received, do not preload the entire repository. Read only what is needed:

1. **Classify the request** into one of the 10 domains:
   - onboarding
   - personal-productivity
   - teaching-learning
   - srujana-shodha
   - admissions-branding
   - placement-tpc
   - academic-admin
   - innovator
   - kaizen-excellence
   - strategic-planning
2. **Read the Domain Index**: Open `domains/<domain>/AGENTS.md` (or `domains/<domain>/README.md` if the former does not exist).
3. **Load the Command**: If the user names or implies a slash command (e.g. `/onboard`, `/question-paper-reviewer`), read *only* the specific command file `domains/<domain>/commands/<command>.md`.
4. **Locate Local Context**: Read memory files in `../srujana-memory/` and institutional references in `../reva-information/` as required for the concrete task.

---
### STOP: NO NEED TO READ FROM THIS POINT ONWARDS IF IN USAGE MODE.
---

# PART B: Development Mode Router (For Developer Collaborators)

This section is active only if a `.git` folder exists at the repository root, indicating a developer checkout, and the contributor approves Development Mode.

## 1. Mode Escalation Trigger
If the user's request requires creating, editing, or deleting files in `domains/`, `.agents/skills/`, `validators/`, `specification/`, `eval/`, or root governance documents, check for a `.git` folder:
- If `.git` does not exist, refuse the request. Explain that this is a read-only distribution folder.
- If `.git` exists, ask for confirmation: *"This would modify SrujanaSangama itself. I see a `.git` folder here. Do you want to switch to Development Mode?"*
- Once confirmed, you remain in Development Mode for the rest of the session.

## 2. Development Process (Agentic Scrum)
In Development Mode, follow this lifecycle in full:
1. **Specify**: Read `CONSTITUTION.md` and this file in full. Draft or update a proposal in `specification/<topic>-proposal.md`.
2. **Plan**: Wait for the Product Owner (`@sanchitnis`) to approve the proposal.
3. **Task**: Break the implementation into atomic tasks under `specification/<topic>-tasks.md`. Limit each task to at most 3 files and ~1 hour of work.
4. **Implement**: Execute only one approved task at a time. Write code strictly in the files specified. Insert `<!-- AGENT QUERY: ... -->` for unresolved ambiguities.
5. **Verify**: Run automated validations or manual checks. Append verification notes to the task file.
6. **Human Review**: Submit changes to the Product Owner for final check. Update `IMPLEMENTATION-STATUS.md` upon any filesystem change.
7. **Path Guidelines**: Always specify relative paths (e.g. `../srujana-memory/`) instead of absolute paths in all configuration files, markdown links, scripts, and documentation to maintain user-independence.

## 3. Development Roles
- **Product Owner / Architect**: Sanjay Chitnis (`@sanchitnis`).
- **Coordinator Agent**: Reads the approved proposal and drafts tasks; does not implement.
- **Implementor Agent**: Executes one approved task at a time; touches only files assigned.
- **Verifier Agent**: Checks compliance with the proposal, CONSTITUTION, and design patterns; does not implement or fix directly.
