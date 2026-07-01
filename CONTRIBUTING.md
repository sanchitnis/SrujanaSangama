# Contributing to SrujanaSangama

This guide covers the practical mechanics of proposing and making a change to SrujanaSangama. It assumes you've already read `CONSTITUTION.md` §2 (the Usage Mode / Development Mode distinction) and `AGENTS.md` (the roles and sprint lifecycle) — this file does not repeat either; it tells you what to actually do.

---

## 1. Before You Start: You Need a Real Git Checkout

Contributing to the platform itself only happens in **Development Mode**, and Development Mode is only reachable inside a real `git clone` of this repository — never inside the shared OneDrive folder faculty use day to day. If you're not sure what that means, read `CONSTITUTION.md` §2 first.

In practice:

```bash
git clone https://github.com/sanchitnis/SrujanaSangama.git
cd SrujanaSangama
```

Open this checkout (not the OneDrive folder) in Claude Code, VS Code, or Antigravity. Every session still starts in Usage Mode — say what platform change you want to make, and the agent will confirm before switching to Development Mode for the rest of that session, per `CONSTITUTION.md` §2.1. There is nothing to manually switch back at the end; the next session starts in Usage Mode again automatically.

---

## 2. Propose Before You Build

Every change — a new domain, a new command, an edit to `specification/architecture.md` or `specification/design.md` — starts as a short proposal in `specification/`, per `CONSTITUTION.md` §6. Don't skip this step even for something that feels small; the proposal is what the Coordinator and Verifier agents check the eventual change against.

### Unscheduled ideas

If you have an idea but aren't ready to write a full proposal, log it in `specification/BACKLOG.md`:

```markdown
### [YYYY-MM-DD] [Domain or Area] — [Idea name]
- **Source**: observation | retro | user-report
- **Priority**: High | Medium | Low
- **Notes**: One-sentence context.
- **Status**: Idea | Ready-to-propose | Resolved
```

### Full proposals

When ready, write `specification/<topic>-proposal.md` containing:
- The problem or gap, in plain terms
- The proposed change to `specification/architecture.md` and/or `specification/design.md`
- An explicit **Scope Boundaries** section (in scope / out of scope)
- A **Verification** section with testable acceptance criteria

Sanjay reviews and approves the proposal before any planning or implementation begins.

---

## 3. The Build Cycle, in Practice

Once a proposal is approved, the Coordinator → Implementor → Verifier cycle in `AGENTS.md` §3–4 runs. As a contributor, your part is:

1. Ask the Coordinator Agent to turn the approved proposal into `specification/<topic>-tasks.md`.
2. Work through tasks one at a time with the Implementor Agent — never batch multiple tasks into one sitting without a Verifier pass in between.
3. Run the Verifier Agent after each task and fix anything it flags as a new task, not as a patch on top of the flagged one.
4. Open a PR only once every task in the list has a PASS verification.

---
## 4. Platform Taxonomy: Commands, Skills, and Agents

When contributing a new capability, you must choose the correct abstraction level:

1. **Commands (under `domains/<domain>/commands/`)**
   - **What they are**: Actionable slash commands (e.g. `/lesson-plan`, `/funding-hunt`).
   - **When to use**: When a human user wants to explicitly trigger a specific action within a department. They are coarse-grained entrypoints.
2. **Skills (under `.agents/skills/`)**
   - **What they are**: Reusable, modular capability packages containing instructions, rules, and optional scripts (each must have a `SKILL.md` entry point with YAML frontmatter).
   - **When to use**: When logic is reused across multiple domains or commands (e.g., `docx` manipulation, `pdf` parsing, `reva-branding`).
3. **Custom Agents (under `agents/`)**
   - **What they are**: Full AI personas or pipelines (like `course-buddy-builder`) with defined input/output contracts.
   - **When to use**: When you need a separate, long-running agent system or persona that uses multiple skills to do its job.

---

## 5. Running the Spec-Sync Audit

Whenever a domain's `rules/`, `commands/`, or a skill is added or changed, run the synchronisation check to catch drift between `specification/design.md`'s description of the system and what actually exists on disk:

```powershell
# Dry run — checks for drift, writes nothing
python .agents/skills/spec-sync/scripts/spec_sync.py --dry-run

# Full run — writes the latest audit log to eval/logs/
python .agents/skills/spec-sync/scripts/spec_sync.py
```

A weekly run is scheduled automatically (Mondays, 09:00 IST) so drift never goes unnoticed for long even between active contribution periods.

---


## 6. Git Branching and Pull Requests

### Branch prefixes

Match the prefix to the domain your change primarily touches, using the domain folder names exactly as they appear in `specification/design.md`:

| Prefix | Domain |
|---|---|
| `teaching/` | `teaching-learning` |
| `research/` | `srujana-shodha` |
| `admissions/` | `admissions-branding` |
| `placement/` | `placement-tpc` |
| `admin/` | `academic-admin` |
| `innovator/` | `innovator` |
| `kaizen/` | `kaizen-excellence` |
| `strategy/` | `strategic-planning` |
| `productivity/` | `personal-productivity` |
| `docs/` | `specification/architecture.md`, `specification/design.md`, or any of the four governance documents |

```bash
git checkout -b teaching/fix-rubric-template
git checkout -b research/add-funding-source
git checkout -b docs/clarify-iqac-vertical
```

### Pull request checklist

Before submitting, verify:
- [ ] A proposal exists in `specification/` and is referenced in the PR
- [ ] Every task in the corresponding `-tasks.md` has a PASS Verifier report
- [ ] `spec_sync.py` returns no failures
- [ ] Nothing in the change duplicates content that already lives in `specification/architecture.md` or `specification/design.md` (per `CONSTITUTION.md` §4 and §9)
- [ ] No file from any user's `srujana-memory/` is included in the diff
- [ ] Any command file still states what it drafts and what a human must decide, per `CONSTITUTION.md` §5
- [ ] `specification/IMPLEMENTATION-STATUS.md` is updated to reflect anything newly implemented (see `AGENTS.md` §8)

---

## 7. Hosting a Local Campus Mirror (IT Administrators Only)

To reduce dependency on OneDrive availability across campus lab networks, IT may host a local read-only mirror:

```bash
# Clone to an internal server
git clone https://github.com/sanchitnis/SrujanaSangama.git /mnt/shared/SrujanaSangama
```

Point lab workstations at the mirrored path the same way they would the OneDrive folder — by opening it directly in Claude Code, VS Code, or Antigravity. There is no registry step to run; the mirror is just a folder, exactly like the OneDrive copy.

```bash
# Scheduled task to keep the mirror current
cd /mnt/shared/SrujanaSangama
git pull origin main
```
