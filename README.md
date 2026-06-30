# SrujanaSangama — Private AI Agent & Skill Module Repository

Welcome to the **SrujanaSangama Private AI Agent & Skill Module Repository** for REVA University. This platform serves as a centralized private hub for academic and professional agents, domains, and capabilities across the REVA campus ecosystem.

To achieve complete multi-platform compatibility for REVA University, the repository utilizes a **dual-engine architecture**. This approach allows a single, unified codebase to share core prompt logic and external tools (using the Model Context Protocol standard) while loading dynamically into separate AI hosts: **Google Antigravity** and **GitHub Copilot** (via custom prompt instructions or workspaces).

> [!NOTE]
> **Important Terminology Update:**
> We have transitioned from standalone plugins to **Modules** integrated directly into our core domains. All references to plugins now map to these integrated modules.

---

## 1. Unified Directory Layout

A single unified repository contains all core modules, reference guides, and execution workflows:

```plaintext
SrujanaSangama/
├── domains/                     # Core Academic & Admin Modules (Shared read-only folders)
│   ├── onboarding/              # Initial workspace onboarding & profile management
│   ├── personal-productivity/   # GTD tasks, personal LLM-wiki, weekly reviews
│   ├── teaching-learning/       # Course design, active learning sessions, assessments
│   ├── srujana-shodha/          # Research grants, publications, PhD guide companion
│   ├── admissions-branding/     # Enrolment funnel analysis & campaign management
│   ├── placement-tpc/           # Company profiles, readiness audits, training plans
│   ├── academic-admin/          # OBE, BOS approval, exam scheduling, SLCM, IQAC AQAR
│   ├── innovator/               # Consulting briefs, Indian patent drafting (Forms 1/2/3), MOUs
│   ├── kaizen-excellence/       # Department/School Kaizen, FDP records, wellbeing checks (Hitaishin)
│   └── strategic-planning/      # Strategic IDP milestone tracking, Summit goal prep
├── skills/                      # Shared Reference Modules (ADDIE, OBE-NBA, Patents, GTD, etc.)
├── validators/                  # Automatic compliance scripts (OBE, NIRF, Admissions, etc.)
├── mcp/                         # Model Context Protocol servers for live data integration
└── docs/                        # Guidelines, Constitution, and developer docs
```

---

## 2. Available Modules, Copilot Agents & Slash Commands

Here is the complete registry of all specialized AI agents and workflows available in the repository, organized by domain:

### 🎓 `@reva-scholar` — Faculty Research & PhD Companion
*Path:* [`domains/srujana-shodha`](file:///d:/Github/SrujanaSangama/domains/srujana-shodha)
* **Description**: A research companion that acts as a Faculty Research Advisor (funding opportunities, manuscript drafting, SDG audits) and a PhD Scholar Journey Companion (guiding doctoral candidates through the 9 lifecycle stages).
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
*Path:* [`domains/teaching-learning`](file:///d:/Github/SrujanaSangama/domains/teaching-learning)
* **Description**: Aligned with the ADDIE instructional model, this agent assists faculty in course formulation, syllabus mapping, assessment integrity, and building smart course buddies.
* **Slash Commands**:
  - `/audit`: Perform a programmatic audit on syllabus documents, checking alignment with AICTE guidelines.
  - `/course-check` / `/design-course`: Validate course unit plans, syllabus designs, and outcomes.
  - `/assessment-check` / `/build-assessment`: Review course exams, quizzes, and continuous evaluation formats against Bloom's Taxonomy.
  - `/build-course-buddy`: Configure local student-facing teaching assistant instances.

---

### 🛡️ `@claw` — AcademicianClaw Personal OS (Personal Productivity)
*Path:* [`domains/personal-productivity`](file:///d:/Github/SrujanaSangama/domains/personal-productivity)
* **Description**: A personal productivity engine modeled after the OpenClaw architecture, offering session orchestration, project tracking, and automated context building.
* **Slash Commands**:
  - `/onboard`: Initialize personal productivity preferences and workspaces.
  - `/weekly-review`: Conduct weekly alignment audits on active projects and commitments.
  - `/project-kickoff`: Set up a new task tracking space and timelines.
  - `/deep-research`: Run a multi-agent loop for web and local research checks.
  - `/session-close`: Close current sessions, committing notes and tasks.
  - `/new-skill`: Scaffolding generator to write a new MCP tool or local helper script.

---

### 🌿 `@reva-kaizen` — Kaizen Wellbeing & FDP Coach
*Path:* [`domains/kaizen-excellence`](file:///d:/Github/SrujanaSangama/domains/kaizen-excellence)
* **Description**: A supportive self-care and professional growth companion focused on continuous improvement, identifying signs of burnout, monitoring workload fatigue, and FDP logs.
* **Slash Commands**:
  - `/kaizen-coach`: Guided reflection audits for energetic, psychological, and workload mapping (Hitaishin wellbeing framework).
  - `/fdp-plan`: Gap analysis and training schedule aligned to faculty growth needs.

---

### 💡 `@reva-innovator` — Consulting & Product Advisor
*Path:* [`domains/innovator`](file:///d:/Github/SrujanaSangama/domains/innovator)
* **Description**: Supports faculty and students in translating academic research into real-world applications, industry consulting, and intellectual property (IP) assets.
* **Slash Commands**:
  - `/patent`: Draft Indian patent specifications (Forms 1/2/3) and audit claims against patentability thresholds.
  - `/consult-brief`: Generate consulting deliverables, timeline, billing frameworks, and sign-offs.

---

### 🏢 `@reva-admin` — Academic Administration
*Path:* [`domains/academic-admin`](file:///d:/Github/SrujanaSangama/domains/academic-admin)
* **Description**: Assists administrative teams, BOS members, and department heads in maintaining UGC, NAAC, and NBA criteria alignment.
* **Slash Commands**:
  - `/attainment`: Calculate Course Outcome (CO) and Program Outcome (PO) attainment margins.
  - `/bos-approve`: Format BOS agendas, draft minutes, and perform compliance checks.
  - `/slcm-report`: Query SLCM data and export NIRF-ready files.

---

## 3. Storage Architecture: Memory & Reference Info

To maintain security, privacy, and integrity, SrujanaSangama utilizes a **three-tier storage architecture** that separates shared intelligence, private/team data, and official university documentation:

1. **`SrujanaSangama/` (Shared Modules - Read-Only)**
   - Managed centrally by REVA IT and synced via OneDrive.
   - Contains all domain modules, prompt boundaries, custom slash commands, MCP servers, and validation scripts.
   - Read-only for general users to prevent unauthorized changes or security drifts.

2. **`srujana-memory/` (Personal/Team Specific Storage - Read-Write)**
   - Created locally or in your private OneDrive space.
   - Stores all personalized persistent information, such as your professional profile, goals, daily/weekly task boards, private reflective journals, and team-specific collaborations.
   - **`my-memory/`**: Confidential files (`soul.md`, GTD task list, Obsidian-compatible wiki notes, GPS goal settings) that are never shared.
   - **`public-memory/`**: Shareable portfolio files (resumes, publication lists, patent lists) used by agents to compile CVs and appraisal evidence.
   - **`collaborations/`**: Multi-user shared spaces (e.g. `scholar-guide/`, `pi-copi/`) for research teams or supervision groups.

3. **`reva-information/` (University Reference Information - Read-Only)**
   - Synced via OneDrive (managed by REVA IT).
   - Contains official university guidelines, academic regulations (UGC/AICTE compliance, PhD handbook), NBA/NAAC accreditation frameworks, and programme syllabi.
   - Kept in a sibling directory to keep the agent grounded in current REVA policies without cluttering private spaces.

---

## 4. How to Sync & Set Up Your Workspace

### Step 1: Sync SrujanaSangama to File Explorer

The Srujana folder is hosted on REVA's OneDrive. Follow these steps to sync it:
1. **Open the OneDrive Link**: Access the Srujana folder on OneDrive via:
   [Srujana OneDrive Directory Link](https://revaedu-my.sharepoint.com/:f:/g/personal/srujana_reva_edu_in1/IgAco6ckZfiyR4zS4TWxU6YBAQ76h3BtkHDkYZR0eit7qnk)
2. **Select SrujanaSangama Folder**: Inside the OneDrive folder list, tick the checkbox next to the **`SrujanaSangama`** folder.
3. **Click Sync**: In the top menu bar, click the **"Sync"** button. This will sync the folder to your local device.
4. **Access in File Explorer**: The folder will now appear in your Windows File Explorer under your `OneDrive - REVA University` directory.
5. **Quick Access**: For convenience:
   - Right-click the `SrujanaSangama` folder → Select **Pin to Quick Access**.
   - Or, right-click the folder → Select **Send to** → **Desktop (create shortcut)**.
6. **Sync `reva-information`**: Repeat the sync process for the shared `reva-information` folder shared by REVA IT.

---

### Step 2: Create Workspace Folder Structure

Set up the workspace folder structure on your local drive or within your personal OneDrive. The directories must be arranged as siblings to allow relative pathing to resolve correctly:

```plaintext
Parent-Folder/ (e.g., d:\Github\ or c:\Workspaces\)
├── SrujanaSangama/      # Synced from OneDrive (Read-Only)
├── srujana-memory/      # Your private storage (Read-Write)
│   ├── my-memory/
│   ├── public-memory/
│   └── collaborations/
└── reva-information/    # Synced from OneDrive (Read-Only reference files)
```

---

### Step 3: Configure VS Code Multi-Root Workspace

To bind all three roots together so your AI agent has simultaneous access to the shared modules, your private memory, and the university references, configure a multi-root workspace:

1. Open VS Code.
2. Select **File** → **Add Folder to Workspace...**
3. Select and add the three folders in this exact order:
   - `SrujanaSangama`
   - `srujana-memory`
   - `reva-information`
4. Select **File** → **Save Workspace As...**
5. Save the file inside the `srujana-memory` folder as **`srujana.code-workspace`**.

The workspace file should contain the following JSON structure:
```json
{
  "folders": [
    {
      "path": "../SrujanaSangama"
    },
    {
      "path": "."
    },
    {
      "path": "../reva-information"
    }
  ]
}
```

---

### Step 4: Run the Onboarding Agent

Once the multi-root workspace is open in your AI tool (Claude Code, VS Code Copilot, or Google Antigravity):
1. Activate the **onboarding** module.
2. Run the onboarding command:
   ```
   /onboard
   ```
3. Complete the guided interview to automatically populate your `soul.md` profile, teaching portfolio mapping, and goal steering configs!

---

## 5. Terms of Use

By installing, deploying, or utilizing any modules or materials from this repository, you explicitly agree to the terms detailed in the [LICENSE](file:///d:/Github/SrujanaSangama/LICENSE) file:
* **Confidentiality**: The code, prompts, and documentation are confidential and proprietary to REVA University. Distributing or disclosing them to third parties is strictly prohibited.
* **Authorized Access**: Access is limited to authorized students and employees of REVA University.
* **Attribution**: Any internal modifications must retain copyright notices and credit REVA University.

---

*REVA University — Educate to Enterprise
Maintained by Dr. Sanjay Chitnis (@sanchitnis), in collaboration with Claude.ai & Google Antigravity*
