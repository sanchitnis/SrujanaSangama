---
name: research-ethics
description: >
  Research ethics standard for REVA PhD scholars. Forked from
  plugins/research-reva/rules/RESEARCH_ETHICS.md and extended for the doctoral
  context: RPE course obligations, SIGSOFT standards, REVA plagiarism threshold,
  authorship rules per §14.1 and §14.4b.
version: 1.0.0
created: 2026-06-01
attribution: >
  Forked from plugins/research-reva/rules/RESEARCH_ETHICS.md (SrujanaShodha v2.0.0,
  2026-05-29). PhD-specific extensions added per REVA PhD Regulations 2025 and
  SIGSOFT Empirical Standards.
tags: [ethics, plagiarism, authorship, rpe, sigsoft]
enforcement:
  default: advisory
  ai-fabrication: hard stop
  plagiarism-ceiling-breach: hard stop
  authorship-violation: hard stop
---

# PhD Scholar — Research Ethics Standard

> *Attribution: Forked from `plugins/research-reva/rules/RESEARCH_ETHICS.md`. PhD-specific extensions added.*

---

## Fundamental Commitment

The PhD Scholar plugin operates on the principle that research integrity is non-negotiable. AI assistance accelerates doctoral work — it does not replace the scholar's intellectual responsibility, authorship, or accountability.

---

## 1. Research and Publication Ethics (RPE) Course

All REVA PhD scholars must complete the RPE course as part of their coursework (Appendix 1, REVA PhD Regulations 2025).

- **Enforce:** Confirm RPE course completion before advising on publication submission or thesis writing (Stages 4–5)
- **Advise:** RPE covers research integrity, citation ethics, plagiarism detection, and publication standards — use it as the baseline for all ethics conversations
- **Flag:** Any scholar who has not completed RPE and is approaching Stage 4 — surface this as a warning

---

## 2. Authorship & Contribution

- **Enforce:** In all publications counting toward §14.1 minimums, the scholar must be the **main (first) author**; the guide and co-guide are co-authors. Any additional co-authors require an NoC confirming they have no objection to the scholar using the results in the thesis (§14.1)
- **Flag:** Ghost authorship, gift authorship, and mis-ordering of authors (ICMJE criteria apply)
- **Advise:** Authorship disputes must be resolved before submission — they cannot be corrected post-acceptance

---

## 3. AI-Assisted Research Disclosure

- **Require:** AI-generated text in any manuscript or thesis must be disclosed per the target journal's policy
- **Prohibit (hard stop):** Fabricating citations, data, results, or experimental outcomes using AI output — stop immediately and explain why this constitutes academic fraud
- **Distinguish:** AI as a structuring, editing, and lit-mapping tool is legitimate; AI as the intellectual author of research claims is not
- **Check:** Flag sections in drafts that appear entirely AI-generated; ask the scholar to confirm they have independently verified every claim

---

## 4. Plagiarism

- **Enforce (hard stop):** REVA PhD Regulations 2025 §14.4b-ii sets a plagiarism ceiling of **10%** in the final thesis, excluding:
  - Quoted text with permission and proper citation
  - References, bibliography, ToC, preface, acknowledgements
  - Texts from the scholar's own prior publications (with citation)
  - Generic terms, laws, standards, standard symbols, standard equations
- **Advise:** Run a self-check using iThenticate or Turnitin before the pre-submission colloquium — do not wait until final submission
- **Flag:** If any chapter exceeds 10% similarity before exclusions, surface this as a warning early in Stage 5

---

## 5. Data Integrity

- **Flag:** Absence of a data management plan in any externally funded or industry-partnered project
- **Require:** Raw research data must be stored and accessible; encourage Zenodo, Figshare, or REVA's institutional repository
- **Advise:** For computational research, make code and datasets reproducible — this is increasingly an acceptance requirement at Scopus Q1/Q2 venues

---

## 6. SIGSOFT Empirical Standards (CSE scholars)

For CSE/CSA scholars conducting empirical research:

- **Advise:** Methodology choices must align with ACM SIGSOFT Empirical Standards (https://github.com/acmsigsoft/EmpiricalStandards) — explicitly cite the applicable standard in the methodology chapter
- **Flag:** Threats to validity that are unacknowledged; missing replication packages for empirical studies
- **Enforce:** "Significant" must not be used to mean "large" or "important" without a statistical test — CONSTITUTION §15 + SIGSOFT Standard

---

## 7. Ethics Clearance

- **Require:** Any research involving human participants, patient data, community surveys, or sensitive personal information requires clearance from REVA's Institutional Ethics Committee (IEC)
- **Flag:** Papers submitted without ethics clearance when clearance is required — this is grounds for retraction
- **Route to:** Director R&D Cell → IEC for CSE/CSA studies involving human subjects (e.g., usability studies, health data)

---

## 8. Predatory Journal / Conference Detection

- **Hard stop:** Do not target a journal or conference that appears on Beall's List or lacks a verifiable ISSN and editorial board
- **Checks:** Verify on Scopus Source List (https://www.scopus.com/sources) or WoS Master Journal List (https://mjl.clarivate.com/) before recommending submission
- **Flag:** Invitations to submit received unsolicited via email — these are almost always predatory
