# Patent Generator (Indian Patent Extraction & Drafting Tool)

> **Plugin ID:** `reva.patent-generator` | **Agent Handle:** *(Workflow-driven)* | **Version:** 0.1.0

A prompt-driven standalone workflow tool designed for REVA University faculty and student inventors. It guides users through extracting invention details, checking patentability, conducting simulated prior art search, scoring, and generating draft Indian patent applications (Form 1, Form 2, and Form 3 specs) completely within a Markdown-native framework.

---

## 💡 Core Capabilities

### 1. Indian Patent Office (IPO) Compliance
* **Standardized Formats**: Automatically structures the output into the precise legal sections required by IPO Form 1 (Application), Form 2 (Provisional/Complete Specification), and Form 3 (Statement & Undertaking).
* **Technical Spec Builder**: Generates Title, Field of Invention, Background, Objectives, Summary, Detailed Description, Claims, and Abstract.

### 2. Prior-Art & Patentability Simulation
* **Prior Art Scanner**: Simulates patent database searches (IP India, Google Patents, Espacenet) to identify potential conflicts.
* **Scoring Rubric**: Scores inventions against critical IPO criteria (Novelty, Inventive Step, Industrial Applicability).

### 3. Human-in-the-Loop Brainstorming
* Interactive prompts to refine claim scopes, bypass Section 3 exclusions, and strengthen novelty arguments.

---

## 🛠️ Unified 8-Step Sequential Workflow

The tool operates via a sequential pipeline of 8 paired workflow+instructions files:
1. **`01_input`**: Initiates the session and captures the core description of the invention.
2. **`02_extract`**: Runs extraction of key components (technical problems, solutions, parameters).
3. **`03_patentability`**: Evaluates section boundaries and Section 3 exclusions.
4. **`04_prior_art`**: Guides the simulated prior art search and keyword mapping.
5. **`05_scoring`**: Computes patentability ratings and highlights claim adjustments.
6. **`06_draft_template`**: Scaffolds the complete Form 2 specification outline.
7. **`07_application`**: Generates full IPO-compliant text (Field, Description, Claims, Abstract).
8. **`08_export`**: Validates legal formatting and exports the final package.

---

## 📂 Directory Layout

```plaintext
plugins/patent-generator/
├── plugin.json         # Google Antigravity Manifest
├── package.json        # GitHub Copilot VS Code Manifest
├── README.md           # This file
├── workflow.md         # Workflow orchestrator rules
├── workflows/          # 8 sequential workflow + instructions files
└── lib/                # patentWorkflow.js mechanical utility
```