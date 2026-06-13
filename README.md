# SrujanaSangama — Private AI Agent & Skill Plugin Marketplace

Welcome to the **SrujanaSangama Private AI Agent & Skill Plugin Marketplace** for REVA University. This platform serves as a centralized private hub for academic and professional agents and capabilities across the REVA campus ecosystem.

To achieve complete multi-platform compatibility for REVA University, the repository utilizes a **dual-engine architecture**. This approach allows a single, unified codebase to share core prompt logic and external tools (using the Model Context Protocol standard) while loading dynamically into separate AI hosts: **Google Antigravity** and **GitHub Copilot**.

---

## 1. Unified Directory Layout

A single plugin directory contains the manifests for both hosts alongside shared rules, reference guides, and execution workflows:

```plaintext
SrujanaSangama/
├── .antigravity-marketplace/
│   └── marketplace.json         # Google Antigravity Central Index
├── .github/
│   └── copilot-marketplace.json # GitHub Copilot Private Registry Map
├── plugins/                     # Private Plugin Directory
│   ├── teaching-learning-reva/  # T - Educator Hat: Course, session, content, assessment integrity
│   ├── srujana-shodha/          # R - Scholar Hat: Projects, grant proposals, manuscript writing
│   ├── academic-admin-reva/     # A - Administrator Hat: Programs, BOS, compliance, CO attainments
│   ├── consulting-product-reva/ # C - Consultant Hat: Experiential labs, patents, MOU reviews
│   └── kaizen-wellbeing-reva/   # K - Self-Improver Hat: Kaizen coach, wellbeing reflection (Hitaishin)
├── specification/               # System Specifications and Abstractions
└── docs/                        # Guidelines and Reference Documentation
```

---

## 2. Available Plugins, Copilot Agents & Slash Commands

Here is the complete registry of all specialized AI agents and workflows available in the marketplace, categorized by academic track:

### 🎓 `@reva-scholar` — Faculty Research & PhD Companion
*Path:* [`plugins/srujana-shodha`](file:///d:/Github/SrujanaSangama/plugins/srujana-shodha)
* **Description**: A dual-purpose research companion that acts as a Faculty Research Advisor (funding opportunities, manuscript drafting, SDG audits) and a PhD Scholar Journey Companion (guiding doctoral candidates through the 9 lifecycle stages).
* **Slash Commands**:
  - `/grant`: Check research drafts or ideas against active public/corporate funding calls and templates.
  - `/manuscript-check`: Audit research manuscript drafts for literature mapping, hypothesis clarity, formatting compliance, and plagiarism risk.
  - `/proposal-check`: Perform structural, budget, and novelty checks on grant proposals.
  - `/guide`: Enable supervisor dashboard mode for tracking candidate progress and milestones.
* **Core Workflows**:
  - `onboarding`: Setup faculty research maps and profile records.
  - `00_onboarding`: Initialize PhD scholar credit floors, timelines, and registration.
  - `sdg-impact-audit`: Review publications against UN Sustainable Development Goals (SDGs) and NEP 2020 indicators.
  - `brand-sprint`: Boost researcher visibility across ORCID, Google Scholar, and citation networks.

---

### 🍎 `@reva-educator` — Teaching & Learning Advisor
*Path:* [`plugins/teaching-learning-reva`](file:///d:/Github/SrujanaSangama/plugins/teaching-learning-reva)
* **Description**: Aligned with the ADDIE instructional model, this agent assists faculty in course formulation, syllabus mapping, assessment integrity, and building smart course buddies.
* **Slash Commands**:
  - `/audit`: Perform a programmatic audit on syllabus documents, checking alignment with AICTE guidelines.
  - `/course-check`: Validate course unit plans, syllabus designs, and outcomes.
  - `/assessment-check`: Review course exams, quizzes, and continuous evaluation formats against Bloom's Taxonomy.
  - `/build-course-buddy`: Configure local student-facing teaching assistant instances.

---

### ⚖️ `@reva-law-student` — Law Student Companion
*Path:* [`plugins/law-student-reva`](file:///d:/Github/SrujanaSangama/plugins/law-student-reva)
* **Description**: A Socratic study assistant for REVA School of Legal Studies, assisting students with case analysis, IRAC framework practice, and bar exam prep.
* **Slash Commands**:
  - `/cold-start-interview`: Interactive profile setup for law courses.
  - `/socratic-drill`: Learn core constitutional and criminal law concepts via active questioning.
  - `/case-brief`: Generate structural briefs from raw Indian court judgments.
  - `/outline-builder`: Build review outline trees for exam prep.
  - `/aibe-prep`: Generate practice questions for the All India Bar Examination.
  - `/flashcards`: Drill case names, standard legal maxims, and doctrines.
  - `/study-plan`: Create custom study plans for legal subjects.
  - `/irac-practice`: Solve mock legal problems using the Issue-Rule-Application-Conclusion framework.
  - `/moot-court-trainer`: Interactive simulations for moot court oral arguments.
  - `/legal-writing`: Review memos, briefs, and draft notices for grammar and legal formatting.
  - `/exam-forecast`: Generate topic notes and outline answers.
  - `/session`: Close the current study session and save progress logs.

---

### 🛡️ `@claw` — AcademicianClaw Personal OS
*Path:* [`plugins/academician-claw`](file:///d:/Github/SrujanaSangama/plugins/academician-claw)
* **Description**: A personal productivity engine modeled after the OpenClaw architecture, offering session orchestration, project tracking, and automated context building.
* **Slash Commands**:
  - `/onboard`: Initialize personal productivity preferences and workspaces.
  - `/weekly-review`: Conduct weekly alignment audits on active projects and commitments.
  - `/project-kickoff`: Set up a new task tracking space and timelines.
  - `/deep-research`: Run a multi-agent loop for web and local research checks.
  - `/session-close`: Close current sessions, committing notes and tasks.
  - `/new-skill`: Scaffolding generator to write a new MCP tool or local helper script.

---

### 🌿 `@reva-kaizen` — Kaizen Wellbeing Coach
*Path:* [`plugins/kaizen-wellbeing-reva`](file:///d:/Github/SrujanaSangama/plugins/kaizen-wellbeing-reva)
* **Description**: A supportive self-care companion focused on identifying signs of burnout, monitoring workload fatigue, and establishing wellness checkins.
* **Slash Commands**:
  - `/gps`: Guided reflection audits for energetic, psychological, and workload mapping.

---

### 💡 `@reva-innovator` — Consulting & Product Advisor
*Path:* [`plugins/consulting-product-reva`](file:///d:/Github/SrujanaSangama/plugins/consulting-product-reva)
* **Description**: Supports faculty and students in translating academic research into real-world applications, industry consulting, and IP assets.
* **Slash Commands**:
  - `/patent`: Draft patent specifications (Forms 1/2/3) and audit claims against patentability thresholds.

---

### 🏢 `@reva-admin` — Academic Administration
*Path:* [`plugins/academic-admin-reva`](file:///d:/Github/SrujanaSangama/plugins/academic-admin-reva)
* **Description**: Assists administrative teams, BOS members, and department heads in maintaining UGC and NAAC criteria alignment.
* **Slash Commands**:
  - `/attainment`: Calculate Course Outcome (CO) and Program Outcome (PO) attainment margins.

---

## 3. How to Install & Deploy on Campus Workstations

### For Google Antigravity Users
1. Register the central SrujanaSangama index in your Antigravity environment:
   ```bash
   antigravity-cli marketplace add srujanasangama <registry-endpoint-url>
   ```
2. View and install available plugins:
   ```bash
   # List plugins in the marketplace
   antigravity-cli marketplace plugins srujanasangama

   # Install a specific plugin
   antigravity-cli marketplace install reva.srujana-shodha
   ```

### Workspace Memory and Information Setup

Since this repository is read-only for security and integrity, all live user memory and university reference files are configured outside of this repository.

1. **Create `srujana-memory`**:
   - Create a folder named `srujana-memory` on your local Desktop or in the parent directory of your repositories.
   - Inside it, create two directories:
     - `my-memory/` — for private data (e.g. `soul.md`, `context/`, `semantic/`, `episodic/`, `habits/`). Copy templates from `plugins/academician-claw/memory/` or run `python3 scripts/local/init.py` once the workspace is open.
     - `public-memory/` — for public portfolios and resumes. It must contain a `profile.md` (resume) and directories: `publications/`, `patents/`, `projects/`, and `reports/`.
     - Create any collaborative team directories if needed: `scholar-guide/`, `pi-copi/`, `guide-team/`, `reva-<team>/`.
2. **Create `reva-information`**:
   - Create a sibling folder named `reva-information` at the same level as your repository folder (i.e. `../reva-information/`).
   - Populate this folder with markdown files containing REVA University public handbooks, regulations, syllabus, and policies.
3. **Configure VS Code Multi-Root Workspace**:
   - Save your workspace as a `.code-workspace` file (e.g., `srujana.code-workspace`) with the following folders:
     ```json
     {
       "folders": [
         { "path": "SrujanaSangama" },
         { "path": "srujana-memory" },
         { "path": "reva-information" }
       ]
     }
     ```

---

## 4. Terms of Use

By installing, deploying, or utilizing any plugins or materials from this repository, you explicitly agree to the terms detailed in the [LICENSE](file:///d:/Github/SrujanaSangama/LICENSE) file:
* **Confidentiality**: The code, prompts, and documentation are confidential and proprietary to REVA University. Distributing or disclosing them to third parties is strictly prohibited.
* **Authorized Access**: Access is limited to authorized students and employees of REVA University.
* **Attribution**: Any internal modifications must retain copyright notices and credit REVA University.
