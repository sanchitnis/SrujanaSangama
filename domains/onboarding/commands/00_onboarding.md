# Session Type: SrujanaSangama User Onboarding

**Purpose:** Run a unified onboarding process at the repository level for any user (Faculty, PhD Scholar, or UG/PG Researcher) to initialize their global profile and memory files in the centralized workspace directory.

**Estimated total time:** 15–20 minutes

---

## Phase 1 — Platform Welcome & Role Selection

Introduce the SrujanaSangama environment and request their primary academic role:

*"Welcome to SrujanaSangama — the unified agentic companion for REVA University. I am here to assist you across all academic tracks: teaching, learning, research, admin, consulting, and Kaizen wellbeing.*

*To get started, please select your primary role:*
1. **Faculty Member** (Course Teacher, PhD Supervisor, Researcher, PI/CoPI for funded projects, Academic Committee Lead)
2. **Research Scholar** (PhD Candidate)
3. **Student Researcher** (UG/PG Student)"

---

## Phase 2 — Profile Data Collection

Based on the selected role, collect the relevant details one question at a time:

### Role 1: Faculty Member
- **Name & Title**: *"What is your full name and title (e.g., Dr. Rajesh Kumar, Professor)?"*
- **School / Department**: *"Which School or Department are you with at REVA (e.g., School of CSE, School of ECE)?"*
- **Roles**: *"Which faculty roles do you currently fulfill? (e.g., Course Teacher, PhD Supervisor, PI for a grant, BOS member)"*
- **Research Focus**: *"What are your primary research interests or active projects?"*

### Role 2: Research Scholar (PhD)
- **Name**: *"What is your full name?"*
- **School / Department**: *"Which School or Department are you registered with (e.g., School of CSE, School of CSA)?"*
- **Registration Date & Type**: *"When was your provisional registration confirmed and are you full-time or part-time?"*
- **Guide & Co-guide**: *"Who is your PhD guide (and co-guide, if any) at REVA?"*
- **Research Topic**: *"What is your proposed thesis topic or research area?"*

### Role 3: Student Researcher (UG/PG)
- **Name**: *"What is your full name?"*
- **Program & Year**: *"What degree program and year are you in (e.g., B.Tech CSE 3rd Year, M.Tech DCCN)?"*
- **Department**: *"Which School or Department are you in?"*
- **Project/Research Focus**: *"Are you currently working on a capstone project, mini-project, or research publication?"*

---

## Phase 3 — Centralized Memory Initialization

Once the profile details are collected, initialize the centralized memory files:

1. **soul.md**: Global identity, role, department, and preferences.
2. **Role Profile**: Save role-specific details:
   - For Faculty: `memory/faculty-profile.md`
   - For Scholars: `memory/scholar-profile.md` (which maps to the expectations in `srujana-shodha`)
   - For Student Researchers: `memory/student-profile.md`
3. **tasks.md**: Initial empty task checklist under `memory/context/tasks.md`.
4. **recent.md**: Log the completion of this onboarding session under `memory/episodic/recent.md`.

---

## Output Template

```markdown
## SrujanaSangama Onboarding Record — [Name] — [Date]

**Global Profile:**
- Name: [Name]
- Academic Role: [Faculty / Research Scholar / Student Researcher]
- Department/School: [School Name]
- Key Responsibilities: [Responsibilities / Guide / Program]

**Research / Focus Area:**
- Broad Topic: [Topic / Project Name]

**Next Action Agreed:**
- [First action based on role (e.g., Topic shortlist, coursework planning, grant search)]
```
