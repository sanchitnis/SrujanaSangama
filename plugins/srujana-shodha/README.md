# SrujanaShodha — Faculty Research & Doctoral Journey Companion

> **Plugin ID:** `reva.srujana-shodha` | **Agent Handles:** `@reva-scholar` (default / faculty), `/guide` (supervisor mode) | **Version:** 2.0.0

A unified, prompt-native personal research and doctoral companion for REVA University faculty and PhD scholars. Deployed across the campus under a **dual-engine architecture** (loads natively in Google Antigravity and GitHub Copilot).

---

## 🔬 Core Capabilities

### 1. Faculty Research Advisor
Provides strategic intelligence for faculty research careers:
* **Competency Profiling**: Identifies research gaps and maps publications to UN Sustainable Development Goals (SDGs).
* **Opportunity Scouting**: Scans funding bodies (ANRF/SERB, DST, DBT, MeitY, CSIR) and matches active calls to profiles.
* **Publication & Citation brand**: Scaffolds manuscript structures, manages h-index building, and audits citation networks.

### 2. PhD Scholar Lifecycle Companion
Guides doctoral candidates through all **9 lifecycle stages**:
* **Stage 0: Topic Scout** — Topic selection, feasibility, and guide allocation caps checking.
* **Stage 1: Coursework Navigator** — Maps credit pathways (18/30/46/50 credits), ARM/RPE preparation, and IA exams.
* **Stage 2: Synopsis Builder** — Synopsis structuring and colloquium mock defense.
* **Stage 3: Research Coach** — Lit reviews (PRISMA-lite), empirical experiment logs, and progress reports.
* **Stage 4: Publication Coach** — Journal targeting (Scopus, WoS, UGC-CARE) and reviewer rebuttals.
* **Stage 5: Thesis Writer** — Chapter drafts, formatting compliance (Appendix 4), and plagiarism checks (ceiling 10%).
* **Stage 6: Patent Agent** — IP screening and Form 1/2/3 creation (connects to `patent-generator`).
* **Stage 7: Grant Agent** — Fellowships, seed grants, and budget structuring.
* **Stage 8: Book Agent** — Academic monographs, outlines, and academic press targeting.

### 3. Supervisor Mode (`/guide`)
Enables research guides to manage their rosters:
* Track scholar milestones and alerts.
* Direct feedback templates for progress reviews and colloquium sign-offs.

---

## 🛠️ Slash Commands

* **`/grant`**: Scans a research abstract or draft against ANRF/DST/DBT templates for call alignment.
* **`/manuscript-check`**: Audits drafts for methodology rigor, literature citations, and plagiarism risks.
* **`/proposal-check`**: Detailed audit of grant proposal drafts, budgets, and NITI Aayog compliance.
* **`/guide`**: Launches the supervisor dashboard.

---

## 📂 Directory Layout

```plaintext
plugins/srujana-shodha/
├── plugin.json         # Google Antigravity Manifest
├── package.json        # GitHub Copilot VS Code Manifest
├── mcp.json            # Model Context Protocol remote config
├── README.md           # This file
├── rules/              # Enforced identity and regulation rules (14 files)
├── workflows/          # Procedural operational prompt pipelines (26 files)
├── agents/             # Specialist runtime actors (core, faculty, scholar, support)
├── context/            # Committed .example profile templates
└── references/         # Regulations, venue digests, and funding landscape databases
```
