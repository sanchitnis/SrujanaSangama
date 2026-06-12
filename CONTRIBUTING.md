# Contributing to SrujanaSangama — Developer & Administrator Guide

Thank you for contributing to the SrujanaSangama Private AI Agent & Skill Plugin Marketplace. This guide covers how to set up development environments, write specifications, synchronize plugin implementations, and manage repository governance.

---

## 1. Operational Mode System (Production vs Development)

SrujanaSangama enforces a strict **Operational Mode System** to prevent AI agents from leaking or modifying governance and system specification files when interacting with end-users.

| Mode | Trigger | System Behavior |
|---|---|---|
| **Production** (default) | Activated if `context/mode.md` is absent or set to `mode: production`. | AI agents serve users, running only rules and workflows. All files in `specification/`, `eval/`, `CONSTITUTION.md`, and `AGENTS.md` are **read-only** and write-locked. |
| **Development** | Enabled by creating `context/mode.md` with `mode: development`. | Agentic Scrum is active. AI agents can access, plan, modify, and synchronize files in `specification/`, `eval/`, and run `spec-sync`. |

### How to Enter Development Mode (Maintainers Only)
Only the repository architect/maintainer (**Sanjay Chitnis @sanchitnis**) may set development mode on local workstations:
```powershell
# 1. Copy the gitignored mode configuration template
copy context\mode.md.example context\mode.md

# 2. Open context\mode.md and edit it to set:
mode: development

# 3. Work on specifications, run tests/audits, and synchronize code.

# 4. Return to production mode before finishing the session:
del context\mode.md
```

> [!CAUTION]
> `context/mode.md` is strictly **gitignored** and must never be committed to the remote repository.

---

## 2. Developer Workflow: Agentic Scrum

SrujanaSangama utilizes **Agentic Scrum** (Spec-Driven Development) to keep specifications and implementations in lockstep.

```
[Write/Approve Spec in plan/ or specification/]
                      ↓
    [Coordinator Agent: Generate *-tasks.md]
                      ↓
  [Implementor Agent: Execute tasks one by one]
                      ↓
    [Verifier Agent: Check criteria & PASS/FAIL]
```

### Writing Backlog Ideas
Unscheduled features, bugs, or suggestions should be recorded in [`specification/BACKLOG.md`](specification/BACKLOG.md) before writing full specifications:
```markdown
### [YYYY-MM-DD] [PluginName] — [Feature name]
- **Source**: observation | retro | user-report
- **Priority**: High | Medium | Low
- **Notes**: One-sentence context of the requirement.
- **Status**: Idea | Ready-to-spec | Resolved
```

---

## 3. Running the Spec-Sync Audit Tool

Whenever rules, workflows, or agents are added/modified, you must run the synchronization script to check for schema drift, unregistered files, or spec discrepancies:

```powershell
# Run a dry run to check for drift (does not write reports)
python skills/spec-sync/scripts/spec_sync.py --dry-run

# Run a full sync to write the latest audit logs to eval/logs/
python skills/spec-sync/scripts/spec_sync.py
```

Weekly runs of `spec_sync.py` are executed automatically via GitHub Actions (triggered every Monday at 09:00 UTC) to ensure the master branch remains synchronized.

---

## 4. Git Branching & Pull Request Process

### Setup Your Fork
1. Fork [github.com/sanchitnis/SrujanaSangama](https://github.com/sanchitnis/SrujanaSangama).
2. Clone the fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/SrujanaSangama.git
   cd SrujanaSangama
   ```
3. Checkout a branch with a prefix matching the plugin:
   ```bash
   git checkout -b law/fix-irac-prompt
   git checkout -b teach/audit-rubric-fixes
   git checkout -b research/add-funding-sources
   ```

### Branch Prefixes:
- `law/` : Law Student companion (`law-student-reva`)
- `teach/` : Educator companion (`teaching-learning-reva`)
- `research/` : Scholar/Advisor companion (`srujana-shodha`)
- `admin/` : Administration (`academic-admin-reva`)
- `kaizen/` : Wellbeing (`kaizen-wellbeing-reva`)
- `consult/` : Consulting (`consulting-product-reva`)
- `docs/` : Marketplace documentation or guides

### Pull Request Checklist
Before submitting a PR to the main repository, verify:
- [ ] No workflow produces completed code or final decisions on behalf of the user (Human-in-the-loop).
- [ ] Any legal or administrative data points carry references to active UGC, BCI, or NBA standards.
- [ ] The `spec_sync.py` script returns no failures.
- [ ] Custom prompts or workflows do not weaken the safety rails defined in `rules/`.

---

## 5. Hosting a Local Campus Mirror (IT Administrators)

To minimize external internet dependency across campus lab networks, you can host a local mirror:

1. **Clone to internal server:**
   ```bash
   git clone https://github.com/sanchitnis/SrujanaSangama.git /mnt/shared/SrujanaSangama
   ```
2. **Register mirror path on workstations:**
   - **Windows (Mapped Drive)**: `agy marketplace add srujanasangama Z:\SrujanaSangama`
   - **Windows (UNC)**: `agy marketplace add srujanasangama \\campus-server\shared\SrujanaSangama`
   - **Linux/Mac**: `agy marketplace add srujanasangama /mnt/shared/SrujanaSangama`
3. **IT Scheduled Task (Cron job):**
   Pull the latest updates periodically:
   ```bash
   cd /mnt/shared/SrujanaSangama
   git pull origin main
   ```
