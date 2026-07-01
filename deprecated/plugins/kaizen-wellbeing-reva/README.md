# Kaizen & Wellbeing Plugin (REVA Kaizen Pack)

> **Plugin ID:** `reva.kaizen-wellbeing-reva` | **Agent Handle:** `@reva-kaizen` | **Version:** 1.0.0

A prompt-native personal growth, reflective coaching, and wellbeing navigation assistant designed for REVA University faculty to sustain effectiveness, manage workload boundaries, and support daily/weekly GPS planning.

---

## 🌱 Core Capabilities

### 1. Goal-Plan-Systems (GPS) Planning
* **Commitment Tracking (Sankalpa)**: Aligns daily and weekly workflows with long-term academic commitments.
* **Goal Setting**: Converts institutional targets (KRA/KPA) into actionable personal growth sprints.

### 2. Reflective Self-Coaching (Hitaishin)
* **Weekly Review Integration**: Helps structure end-of-week reviews focusing on teaching wins, research blockers, and administrative workloads.
* **Metacognitive Scaffolding**: Prompts deep reflections on pedagogical successes and failures to foster continuous professional development (Kaizen).

### 3. Workload Calibration & Wellbeing
* **Stress Diagnostics**: Recognizes PhD stress indicators, administrative burnout, and research isolation.
* **Wellness Check-ins**: Suggests self-care protocols and signposts faculty and students to REVA counseling services.

---

## 🛠️ Slash Commands

* **`/gps`**: Initiates the Goal-Plan-Systems workshop to review weekly progress and outline next executable steps.
* **`/kaizen-reflect`**: Facilitates deep academic self-reflections on course deliverables, FDP outcomes, and teaching feedback.
* **`/wellness`**: Simple, confidential stress audits mapping work-life balance wheels and self-care nudges.

---

## 📂 Directory Layout

```plaintext
plugins/kaizen-wellbeing-reva/
├── plugin.json         # Google Antigravity Manifest
├── package.json        # GitHub Copilot VS Code Manifest
├── README.md           # This file
├── rules/              # PERSONAL_REFLECTION_RULES.md, WELLBEING_STANDARD.md
└── workflows/          # gps-plan.md, kaizen-reflect.md, wellness-audit.md
```
