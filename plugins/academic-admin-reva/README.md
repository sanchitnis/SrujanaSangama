# Academic Administration Plugin (REVA Admin Pack)

> **Plugin ID:** `reva.academic-admin-reva` | **Agent Handle:** `@reva-admin` | **Version:** 1.0.0

A specialized administrative, accreditation, and compliance agent pack designed for REVA University faculty and program chairs to manage OBE direct/indirect attainments, Board of Studies (BOS) regulatory compilations, and SAR audits.

---

## 🏛️ Core Capabilities

### 1. CO-PO Attainment Calculation
* **Direct & Indirect calculation**: Synthesizes scores from continuous internal assessments (CIA), end-semester exams, and student surveys.
* **Remediation Planner**: Automatically highlights gaps below thresholds and proposes actionable student-facing interventions.
* **Heatmap Generator**: Generates visual representations of outcomes coverage across the program curriculum.

### 2. Board of Studies (BOS) & Governance
* **BOS Proposal Formatter**: Prepares change proposals formatted to UGC, AICTE, and NEP 2020 standards.
* **BOS Agenda & Minutes**: Drafts agendas, briefings, compliance checklists, and meeting minute transcripts for secretary review.

### 3. Accreditation SAR Compile (NBA/NAAC)
* **SAR Documentation**: Compiles evidence folders and writes Criterion-wise Self-Assessment Report responses.
* **Accreditation Readiness**: Scans folders to check for missing signatures, incomplete rubrics, or outdated course logs.

### 4. NIRF & Institutional Positioning
* **NIRF Parameter Scraper**: Scans institutional pipelines to compile research parameters, faculty metrics, and placement outputs for VC review.

---

## 🛠️ Slash Commands

* **`/attainment`**: Computes direct/indirect CO attainments, maps threshold gaps, and drafts remedial actions.
* **`/accredit`**: Audits folders and gathers evidence to compile SAR dossiers for NBA and NAAC reviews.
* **`/nirf-accelerate`**: Performs institutional parameter audits and outlines rankings gap strategies.
* **`/bos-approve`**: Structures new syllabus revisions into compliance checklists and draft minutes for BOS Board deliberation.

---

## 📂 Directory Layout

```plaintext
plugins/academic-admin-reva/
├── plugin.json         # Google Antigravity Manifest
├── package.json        # GitHub Copilot VS Code Manifest
├── README.md           # This file
├── rules/              # REGULATORY_COMPLIANCE.md, BOS_GOVERNANCE_STANDARD.md
└── workflows/          # attainment-check.md, bos-approve.md, sar-compile.md
```
