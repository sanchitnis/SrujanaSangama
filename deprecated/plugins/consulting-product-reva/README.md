# Consulting & Product Development Plugin (REVA Innovator Pack)

> **Plugin ID:** `reva.consulting-product-reva` | **Agent Handle:** `@reva-innovator` | **Version:** 1.0.0

Designed for REVA University faculty innovators, consulting chairs, and supervisors to navigate corporate engagements, technology transfer, intellectual property (IP) drafting, and experiential student mentoring.

---

## 💡 Core Capabilities

### 1. Intellectual Property & Patents
* **Invention Disclosures**: Guides faculty through extracting core innovative concepts from coursework, projects, or lab prototypes.
* **Patent Claim Drafting**: Generates first-draft claims aligned to Indian Patent Office standards (connects with `patent-generator` for Form 1/2/3).
* **Prior-Art Simulation**: Accelerates search validation to assess patentability indices before filing.

### 2. Corporate Partnerships & MOUs
* **MOU Auditing**: Reviews corporate partnership, research, or training drafts against REVA University institutional compliance frameworks.
* **MOU Scoping**: Structures milestones, training deliverables, and IP allocations for research cell negotiations.

### 3. Industry Consulting
* **Consulting Scoping**: Drafts project delivery briefs, budget estimations, and practitioner-in-residence schedules from ambiguous corporate briefs.
* **Experiential Course Design**: Bridges academic courses to live industry problems, aligning mini-projects with corporate connects.

---

## 🛠️ Slash Commands

* **`/patent`**: Audits project designs for IP value, checks prior art, and formats Form 1/2/3 draft specs.
* **`/mou-check`**: Audits draft agreements against university legal and research cell policy standards.
* **`/consulting-brief`**: Structures corporate consulting requests into standard milestone proposals and budgets.

---

## 📂 Directory Layout

```plaintext
plugins/consulting-product-reva/
├── plugin.json         # Google Antigravity Manifest
├── package.json        # GitHub Copilot VS Code Manifest
├── README.md           # This file
├── rules/              # PRODUCT_IP_GUIDELINES.md, CONSULTING_SAFETY_RULES.md
└── workflows/          # patent-draft.md, mou-audit.md, scope-consulting.md
```
