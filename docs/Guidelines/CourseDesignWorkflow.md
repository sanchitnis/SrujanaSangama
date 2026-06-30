# Course Design Workflow
## Human-AI Collaborative Process for REVA University

> **Purpose.** This document defines the end-to-end workflow for faculty to design a course using the SrujanaSangama AI platform and the REVA Course File Template. It resolves standing design decisions, states the two supported entry workflows, and marks every point where a human sign-off is mandatory before the course proceeds.

---

## Prerequisites (before starting)

Faculty must have:
- Cloned the SrujanaSangama repository locally.
- A GitHub Education account **or** an institutional generative AI licence (Google Antigravity / GitHub Copilot).
- VS Code (with the SrujanaSangama plugin installed) or access to the Antigravity IDE.
- Read the following documents before writing a single CO:
  1. [`Course_Designer_Guidelines_Universal.md`](file:///d:/SrujanaSangama/docs/Guidelines/Course_Designer_Guidelines_Universal.md) — universal rules for all programme types
  2. [`COURSE_DESIGN_STANDARD.md`](file:///d:/SrujanaSangama/plugins/teaching-learning-reva/rules/COURSE_DESIGN_STANDARD.md) — non-negotiable quality rules and HOTS dominance requirement
  3. [`Course_File_Template_DualLevel.md`](file:///d:/SrujanaSangama/docs/Guidelines/Course_File_Template_DualLevel.md) — the template to fill

---

## Resolved Design Decisions

The following questions were open in the original draft. They are now resolved.

### Decision 1 — Differentiation Model

**Resolved: Option (b) — Outcomes are the same for all students; differentiation is managed by the awareness/advanced mark split, not by separate activities or separate COs.**

Every student is taught and assessed on the same Course Outcomes. The Course File Template enforces this via the **dual-level design** (§3 and §14 of the template):
- **Awareness level** — the floor every student must clear (protects placement-readiness).
- **Advanced level** — depth that requires a student to exceed the awareness marks ceiling; the only path above 8 CGPA.

Faculty do **not** create separate course outcomes for fast learners. The same CO is written once; the question paper and rubric split the marks, with awareness marks capping out below the 8-CGPA band.

> This decision was made by the curriculum committee and is a **non-negotiable template requirement** (COURSE_DESIGN_STANDARD.md). Individual course leads may adjust the awareness/advanced mark ratio within ±5% of the 70/30 split, with HoD/Director approval.

---

### Decision 2 — Assessment Mark Ratio (Theory + Lab Courses)

**Resolved: The standard split is 70% awareness marks : 30% advanced marks across all CIA and SEE components.**

The overall credit weightage for a course depends on its L-T-P type (defined in `Course_Designer_Guidelines_Universal.md`). Within that overall split, the dual-level mark ratio applies as follows:

| Component | Standard weight | Awareness portion | Advanced portion |
|---|---|---|---|
| Internal Assessment 1 (IA-1 / Crit 1) | 20 marks | ≈14 marks | ≈6 marks |
| Internal Assessment 2 (IA-2 / Crit 2) | 20 marks | ≈14 marks | ≈6 marks |
| Continuous Evaluation (Assignments / CE) | 10 marks | ≈7 marks | ≈3 marks |
| End-Semester Exam / Final Jury (SEE) | 50 marks | ≈35 marks | ≈15 marks |
| **Total** | **100 marks** | **≈70 marks** | **≈30 marks** |

**Calibration check (mandatory):** A student who scores full awareness marks but zero advanced marks must land below the 8-CGPA equivalent in the institution's marks-to-grade conversion. Faculty must complete the calibration check table in §14.1 of the Course File Template before the course runs.

> Course leads may apply to their HoD for a ratio variation (e.g., 65/35 for a highly project-based course). Any variation requires HoD sign-off and a note in the Course File.

---

### Decision 3 — Exemplar Source for Course Outcomes

**Resolved: Course Outcomes are written by the faculty using the REVA Course Design Standard as the quality benchmark. The AI generates a first-draft CO set for faculty review — the faculty member is always the author of record.**

The exemplar and CO-writing guidance is:
- Use strong Bloom's action verbs at L4–L6 (Analyse, Evaluate, Create) for at least 60% of COs.
- Use the NBA 11 POs as the mapping framework (PO full names are in §19 of the template).
- Every course must include at least one Enterprise Skills CO (`CO-ES`) targeting initiative, collaboration, ethical reasoning, communication, adaptability, or creativity.
- IKS and Sustainability integration must appear in at least one unit per course (declared in §5.1 of the template).

The AI skill `/course-check` can audit a draft CO set against these rules.

---

## Workflow 1 — Upload & Reformat Existing Course Document

Use this workflow when the faculty member already has a course file or syllabus document.

1. **Open SrujanaSangama in VS Code / Antigravity.**
2. **Upload the existing course document** into the workspace.
3. **Prompt the AI:**
   ```
   /course-check <path-to-existing-document>
   ```
   The AI will audit the document against the 7 quality dimensions and flag gaps.
4. **Review the audit report.** Address all HARD STOP flags before proceeding.
5. **Prompt the AI to reformat the document** into the Course File Template:
   ```
   Using Course_File_Template_DualLevel.md as the target structure, reformat <document> 
   into the template. Map existing COs to the CO table, flag any missing sections, 
   and propose the awareness/advanced split for §14.
   ```
6. **Faculty reviews and completes all ‹placeholder› fields**, especially:
   - §3 Dual-level scope per unit
   - §5.1 IKS / Sustainability declaration
   - §5.2 Portfolio Artefact Specification
   - §14.1 Calibration check
   - §14.2 AI-triviality check per instrument
   - §19 CO-PO mapping (NBA 11 POs)
7. **Run `/course-check` on the completed template.** All 7 dimensions must be PASS or CONDITIONAL before submission.

> **🟡 GOVERNANCE SIGN-OFF — Point 1:** Faculty submits the completed Course File for **Peer Review** by a subject expert. Peer reviewer signs §22 (or appends a review note). Proceed only after peer sign-off.

---

## Workflow 2 — Draft from Course Outcomes

Use this workflow when the faculty member is designing a new course from scratch.

1. **Open SrujanaSangama in VS Code / Antigravity.**
2. **Write your intended Course Outcomes in the chat interface**, in plain language. Example:
   ```
   I am designing a 4-unit course on Robotics & Embedded Systems for 5th-semester 
   students. The graduate should be able to: [list your intended learning goals]
   ```
3. **Prompt the AI to generate a structured CO set:**
   ```
   Using COURSE_DESIGN_STANDARD.md, convert these goals into 5-6 COs with:
   - Bloom's level tags (L1–L6)
   - One CO-ES targeting an enterprising human skill
   - NBA PO mapping suggestions
   - Awareness/Advanced classification per CO
   ```
4. **Faculty reviews and finalises the CO set.** Revise any CO that uses weak verbs (understand, know, be aware of).
5. **Prompt the AI to build the full Course File:**
   ```
   Using Course_File_Template_DualLevel.md, generate a complete Course File draft 
   for this CO set. Fill all awareness/advanced scope rows in §3 and propose 
   the §14 assessment split.
   ```
6. **Faculty completes all ‹placeholder› fields** (same checklist as Workflow 1, Steps 6–7).
7. **Run `/course-check` on the completed template.**

> **🟡 GOVERNANCE SIGN-OFF — Point 1:** Same peer review requirement as Workflow 1. Proceed only after peer sign-off.

---

## Governance Sign-Off Points

These are the mandatory human approval gates before a course proceeds to the next stage. AI cannot substitute for any of these.

| Sign-Off | Who approves | What they check | When |
|---|---|---|---|
| **Gate 1 — Peer Review** | Subject-expert peer (nominated by HoD) | CO quality, Bloom's levels, CO-PO mapping accuracy, enterprise skill CO present | After completing the Course File draft |
| **Gate 2 — HoD / Director Approval** | HoD or School Director | Dual-level calibration verified (§14.1 complete), portfolio artefacts defined (§5.2), IKS/Sustainability declared (§5.1) | Before the course runs in a semester |
| **Gate 3 — BOS Ratification** | Board of Studies | New courses, substantially revised COs, new PSOs, or any change to the CO-PO mapping strength | Annual BOS meeting; any mid-cycle CO change above threshold |
| **Gate 4 — Post-Offering Reflection** | Faculty + HoD | Dual-level health check completed (§21), CO attainment reported for advanced COs separately (§18), AI-triviality check retrospectively reviewed | After each offering, before next semester's file is approved |

> **Course files with incomplete governance records (missing signatures, skipped calibration checks, or unresolved HARD STOP flags) will not be accepted by the Academic Administration plugin (`@reva-admin`).**

---

## PEO / PSO Relationship to Course Design

> This resolves the earlier open question on the sequencing of PEOs, PSOs, and course design.

**The correct order is:**

```
1. School approves PEOs and POs/PSOs (Phase 2 of the curriculum lifecycle)
         ↓
2. Faculty design courses mapped to those POs/PSOs (Phase 3 — this workflow)
         ↓
3. CO attainment data aggregates up to PO/PSO attainment
```

Faculty must not design courses before the programme's PO/PSO framework is finalised. If the PO/PSO framework is not yet available, the course file draft may proceed but cannot be submitted for Gate 2 approval until the mapping is complete.

The curriculum review cycle (filling gaps) happens at BOS level, not at the individual course level.

---

## Quick Reference

| I want to… | Use this |
|---|---|
| Audit an existing course file | `/course-check <file>` |
| Generate a CO set from learning goals | Workflow 2, Step 3 prompt |
| Check my CO Bloom's levels | `COURSE_DESIGN_STANDARD.md` |
| Complete the CO-PO mapping table | §19 of `Course_File_Template_DualLevel.md` (NBA 11 POs) |
| Verify assessment AI-triviality | §14.2 of the template |
| Design activities per unit | `/activity-design-ai-ready <unit-description>` |
| Submit for BOS | `@reva-admin` — `/attainment` workflow |

---

*Version 2.0 | Updated: June 2026 | Resolved decisions: Differentiation model (b), Mark ratio (70/30), Exemplar source (faculty-authored, AI-assisted) | Governance gates: 4 mandatory sign-off points added*
