# Command: /resume-audit

**Description:** Audits the user's resume for UGC/AICTE compliance, ATS formatting, and keyword optimization in a positive-first, confidential manner. Typically used by Faculty Members and Research Scholars.

---

## 🤝 Human-AI Collaboration Boundary

* **What the Agent Drafts:** A detailed, confidential self-improvement report evaluating UGC shortlisting metrics, AICTE 360-degree feedback indicators, ATS compatibility parameters, keyword density, and a list of strengths and growth options.
* **What the Human Must Review & Approve:** The estimated percentages/categories used for grading graduation and post-graduation marks, NET/SET status, and the feasibility of the proposed self-improvement paths.

---

## 🛠️ Step-by-Step Resume Audit Workflow

When a user runs `/resume-audit`, the agent must execute the following sequential workflow:

### Step 1 — Resume Retrieval
Locate and read the user's resume file inside their workspace (e.g. `public-memory/resume.pdf`, `public-memory/resume.txt`, `public-memory/resume.docx`, or `public-memory/resume.md`).
* If no resume is found in the workspace, ask the user to provide their resume text or file path.

### Step 2 — UGC Recruitment & Shortlisting Score Assessment
Calculate the shortlisting score based on UGC Regulations 2018 (Table 3A) for Assistant Professors (Total: 100 Marks):
* **Graduation:** 80%+ = 15 Marks | 60% to 80% = 13 Marks | 55% to 60% = 10 Marks | 45% to 55% = 5 Marks.
* **Post-Graduation:** 80%+ = 25 Marks | 60% to 80% = 23 Marks | 55% to 60% (50% for SC/ST/OBC non-creamy) = 20 Marks.
* **M.Phil:** 60%+ = 7 Marks | 55% to 60% = 5 Marks.
* **Ph.D.:** 30 Marks.
* **NET with JRF:** 7 Marks | **NET only:** 5 Marks | **SLET/SET:** 3 Marks.
* **Research Publications:** 2 marks per paper published in peer-reviewed or UGC-listed journals (Max 5 papers = 10 Marks).
* **Teaching / Post-Doctoral Experience:** 2 marks per year (Max 5 years = 10 Marks).
* **Awards:** International/National = 3 Marks | State Level = 2 Marks.
* *Note combined capping constraints:* M.Phil + Ph.D. maximum is 30 Marks. NET/SLET/SET maximum is 7 Marks. Awards maximum is 3 Marks.

### Step 3 — AICTE 360-Degree Feedback Assessment
For engineering/technical domains, estimate performance points based on the 10-point scale:
* **Teaching Process (Max 2.5 pts / 25%):** Mapped Course Outcomes, ICT tool usage, course file maintenance.
* **Student Feedback (Max 2.5 pts / 25%):** Average student feedback score out of 100 or 10.
* **Department Activities (Max 2.0 pts / 20%):** Lab In-charge, timetable coordinator, NAAC/NBA criteria lead, BOS helper.
* **Institute Activity (Max 1.0 pt / 10%):** Admissions committee, exam superintendent, student club mentor.
* **ACR / Appraisal (Max 1.0 pt / 10%):** Annual Confidential Report grading (outstanding, very good, etc.).
* **Contribution to Society (Max 1.0 pt / 10%):** NSS Officer, Unnat Bharat Abhiyan, community camp organization.

### Step 4 — ATS Layout & Parsing Check
Inspect the resume formatting for parsing hurdles:
* **Layout Structure:** Single-column layout check (avoid multi-column or text box parsing failures).
* **Font and Typography:** Use of standard ATS-safe fonts (Arial, Calibri, Times New Roman, size 10-12).
* **Parsing Blockers:** Flags any tables, graphics, columns, charts, or images in the body.
* **Crucial Keywords:** Check density of academic keywords ("UGC-CARE", "Scopus Indexed", "Web of Science", "Outcome Based Education (OBE)", "Course Outcomes (CO)", "NAAC Criteria", "NBA Accreditation").
* **Verification Links:** Look for active hyperlinks to Google Scholar, ResearchGate, ORCID, or Vidwan profiles.

### Step 5 — Positive-First Strengths & Opportunities Analysis
To maintain high motivation and align with self-improvement goals, format the feedback with a positive reinforcement focus:
* **Celebrate Strengths:** Highlight all academic, research, and institutional leadership achievements first. Use encouraging phrases like *"Strong academic candidate with a UGC Shortlisting Score of X/100"* or *"Excellent research momentum with Scopus indexed publications"*. Focus more on what exists and represents a "win" than what is missing.
* **Growth Milestones & Enhancement Paths:** Frame gaps gently as positive next steps. For example:
  - Frame low publications as: *"Enhancement Path: Increasing target publications in peer-reviewed, Scopus/UGC-CARE indexed journals to unlock a +X bump in your shortlisting score."*
  - Frame lack of digital pedagogy as: *"Growth Milestone: Adding a 'Digital Pedagogy' section showcasing LMS course designs (Moodle) or NPTEL/Swayam certifications."*
  - Frame lack of PhD as: *"Future Milestone: Highlight enrollment/thesis status to map out upcoming UGC qualification points."*

---

## 📂 Output Target

This report is confidential and intended for self-improvement. The agent must write the output privately to the user's private memory space:
`srujana-memory/my-memory/resume-audit-report.md`
It should **never** be placed in the `public-memory/` directory or checked into public version control.
