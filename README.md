# SrujanaSangama - REVA University AI Agent Workspace

> [!IMPORTANT]
> **For AI Agents:** Do not read or parse this README file further. Go directly to the cross-IDE entry instruction file [AGENTS.md](SrujanaSangama/AGENTS.md) to understand routing constraints, domain categorization, and permissions.

Welcome to SrujanaSangama, REVA University's shared system of Markdown-based AI agent modules, domain commands, rules, and reusable skills.
Srujana means creation and sangama is confluence of all your ideas and work to take REVA University forward in the era of AI.

---

# PART A: Usage Mode (For Regular Users - Default)

This section is for faculty, staff, researchers, and administrators who use SrujanaSangama with AI-enabled IDEs (such as Claude Code, GitHub Copilot in VS Code, Kiro, or Google Antigravity) to assist with daily and strategic tasks.

> [!NOTE]
> Regular users **do not modify** any files in the `SrujanaSangama/` folder. All personal data, working logs, and outputs must be written to your personal `srujana-memory/` folder. You do not need to read `CONSTITUTION.md`, `CONTRIBUTING.md`, or the internal codebase specifications.

## 1. Quick Setup & Workspace Installation

To set up your workspace, prepare three sibling folders on your local drive (default: `Documents/` folder):

1. **SrujanaSangama (Read-Only)**
   - Open the SrujanaSangama OneDrive folder: [OneDrive SrujanaSangama Link](https://revaedu-my.sharepoint.com/:f:/r/personal/srujana_reva_edu_in1/Documents/srujana/SrujanaSangama?csf=1&web=1&e=Rdhymo)
   - Click **"Add shortcut to My Files"** in the OneDrive web interface to create a synced link in your local OneDrive folder.
2. **reva-information (Read-Only)**
   - Open the reva-information OneDrive folder: [OneDrive reva-information Link](https://revaedu-my.sharepoint.com/:f:/r/personal/srujana_reva_edu_in1/Documents/srujana/reva-information?csf=1&web=1&e=q2VpWr)
   - Click **"Add shortcut to My Files"** to create a synced link on your local drive at the same level.
3. **srujana-memory (Read-Write)**
   - Create a new, empty folder named `srujana-memory` at the same level as the other two folders which will save all your personal work and information that is private to you.

### The Sibling Folder Layout
Your local workspace directory must look like this:
```text
Parent-Folder (e.g., Documents)/
├── SrujanaSangama/     # Synced read-only folder
├── reva-information/   # Synced read-only folder
└── srujana-memory/     # Your personal read-write folder
```

### Opening the Workspace
Open VS Code (or your chosen AI IDE) and select **File > Open Workspace from File...**, then select:
`SrujanaSangama/srujanasangama.code-workspace`

This workspace configuration automatically mounts all three folders together. 

> [!TIP]
> **Path Independence**: The workspace file uses relative paths (e.g. `../srujana-memory/`) so it remains completely user-independent. It works out of the box regardless of your operating system username or local path configuration. The shared folders are automatically configured as read-only.

---

## 2. Getting Started (First-Time Onboarding)

If you are opening this workspace for the first time, your personal profile and memory files must be set up. 

Ask your AI agent to begin onboarding by sending the following message in the chat:
```text
Use the onboarding domain and run /onboard.
```
The AI agent will guide you step-by-step through setting up your profile in `srujana-memory/`.

---

## 3. How to Use the System

Once onboarded, start any session by asking the AI agent to assist you within a specific domain. The AI agent will read the instructions in the repository to guide you. Below is the list of available domains and their primary commands:

* **onboarding**
  - `/onboard`: Sets up user profile, creates local `srujana-memory` structures, and performs a resume audit.
* **personal-productivity**
  - `/morning-briefing`: Daily agenda and task alignment.
  - `/weekly-review` / `/weekly-alignment-audit`: End-of-week task auditing.
  - `/deep-research`: Conducts structured literature and web searches.
  - `/skill-generator`: Packages a workflow into a reusable skill.
  - `/project-kickoff`: Sets up metadata for a new project.
* **teaching-learning**
  - `/curriculum-design-lifecycle`: End-to-end course/curriculum design.
  - `/lesson-plan`: Drafts modular lesson plans.
  - `/question-paper-reviewer`: Checks question papers against Blooms Taxonomy and REVA standards.
  - `/assessment-check` / `/course-check` / `/session-check`: Formative review of educational materials.
* **srujana-shodha**
  - `/research-lifecycle`: Guides through academic research phases from coursework to thesis defense.
  - `/manuscript-check`: Audits drafts before journal submission.
  - `/funding-hunt` / `/opportunity-mapping`: Locates suitable grants and projects.
  - `/grant-check` / `/proposal-check`: Reviews grant proposals.
  - `/sdg-impact-audit`: Maps research contribution to Sustainable Development Goals.
  - `/brand-sprint`: Builds researcher brand and online profiles.
* **academic-admin**
  - `/attainment-check`: Evaluates course/program outcome attainment.
* **innovator**
  - `/patent-draft`: Full multi-step workflow for patentability analysis and patent application drafting.
* **kaizen-excellence**
  - `/gps-plan`: Drafts strategic improvement goals.
* **admissions-branding**
  - Assists with institutional branding and marketing materials.
* **placement-tpc**
  - Connects students with placement preparation and career development tools.
* **strategic-planning**
  - Formulates institutional growth strategies and developmental goals.

### How to Invoke Commands
Simply ask the AI agent:
* *"Under the `teaching-learning` domain, run `/question-paper-reviewer` on my draft paper"*
* *"Use the `srujana-shodha` domain and run `/funding-hunt` for a green energy project"*

---

# PART B: Development Mode (For Developer Collaborators)

This section is only relevant if a `.git` folder exists at the root of `SrujanaSangama/`, indicating a development checkout.

If `.git` is present, contributors can modify `SrujanaSangama` files to add or improve domains, commands, and skills.

For this purpose, you should get you added as a collaborator and clone the sanchitnis/SrujanaSangama GitHub repo.

## 1. Workspace Rules in Development Mode
- **SrujanaSangama** becomes read-write. Changes are managed via git.
- **srujana-memory** is strictly used for testing commands with synthetic or mock user data for testing purpose and not your personal data.
- **Before making any modifications**, read:
  - `CONSTITUTION.md` - Immutable rules, Mode triggers, and conventions.
  - `CONTRIBUTING.md` - Detailed instructions on the proposal and pull request workflow.

## 2. Complete Repository Structure
```text
SrujanaSangama/
├── AGENTS.md                 # Cross-IDE router for agents
├── GEMINI.md                 # Gemini / Antigravity shim
├── CONSTITUTION.md           # Governance, modes, and conventions
├── CONTRIBUTING.md           # Contributor mechanics
├── IMPLEMENTATION-STATUS.md  # Current status of implemented domains
├── srujana.code-workspace    # Shared multi-root workspace file
├── domains/                  # Faculty/admin modules by domain
├── .agents/                  # Workspace customizations
│   └── skills/               # Shared reusable reference modules (e.g. science plugins)
├── validators/               # Quality-gate scripts for checking formats
├── scripts/                  # Helper scripts (file I/O, date math, parsing)
└── specification/            # Proposals, tasks, and system specifications
```

---

## Terms Of Use

Use of this repository is limited to authorized REVA University users. The modules, prompts, specifications, and documentation are confidential and proprietary to REVA University. Do not distribute them outside authorized channels.

Maintained by Dr. Sanjay Chitnis (@sanchitnis).
