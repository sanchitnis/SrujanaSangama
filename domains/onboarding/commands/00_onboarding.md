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

## Phase 2.5 — Professional & Research Identifiers

For all roles (prioritizing Faculty and Research Scholars), collect links to their professional and academic profiles, and ask if they wish to upload a resume:

- **LinkedIn URL**: *"Please provide your LinkedIn profile URL (e.g., https://linkedin.com/in/username)."*
- **Google Scholar URL**: *"Please provide your Google Scholar profile URL."*
- **IRINS URL**: *"Please provide your IRINS profile URL."*
- **VIDWAN URL**: *"Please provide your VIDWAN profile URL."*
- **ORCID iD**: *"Please provide your ORCID iD or URL (e.g., 0000-0000-0000-0000)."*
- **Web of Science (WoS) ResearcherID**: *"Please provide your Web of Science ResearcherID or URL."*
- **Resume Upload**: *"If you have a digital resume (PDF, Word, or Markdown), please provide its file path. We will copy it to your public portfolio and extract key information (publications, projects, education) to pre-populate your profile files."*

---

## Phase 3 — Centralized Memory Initialization

Once the profile details, identifiers, and resume path are collected, initialize the centralized memory files:

1. **soul.md**: Global identity, role, department, preferences, professional/research profile links, and local resume path.
2. **Role Profile**: Save role-specific details:
   - For Faculty: `my-memory/semantic/profile.md` (and optional `teaching.md` & `research.md`)
   - For Scholars: `my-memory/semantic/research.md` (and optional `scholar-profile.md` which maps to the expectations in `srujana-shodha`)
   - For Student Researchers: `my-memory/semantic/profile.md`
3. **Resume Handling**: If a resume path is provided, copy the file to `public-memory/resume.<extension>`.
4. **Information Extraction**: The agent will parse/extract the relevant details (such as top publications, active grants, past employment, and academic qualifications) from the provided profile URLs and the copied resume. These details will be structured and used to pre-populate the corresponding markdown profiles inside `my-memory/semantic/` and `public-memory/profile.md`.
5. **tasks.md**: Initial empty task checklist under `my-memory/context/tasks.md`.
6. **recent.md**: Log the completion of this onboarding session under `my-memory/episodic/recent.md`.

---

## Output Template

```markdown
## SrujanaSangama Onboarding Record — [Name] — [Date]

**Global Profile:**
- Name: [Name]
- Academic Role: [Faculty / Research Scholar / Student Researcher]
- Department/School: [School Name]
- Key Responsibilities: [Responsibilities / Guide / Program]

**Professional & Research Identifiers:**
- LinkedIn: [URL]
- Google Scholar: [URL]
- IRINS: [URL]
- VIDWAN: [URL]
- ORCID: [iD/URL]
- Web of Science: [ID/URL]
- Resume File: [Copied file path inside public-memory/]

**Research / Focus Area:**
- Broad Topic: [Topic / Project Name]
- Extracted Profile Info: [Summary of publications/experience extracted from links and resume]

**Next Action Agreed:**
- [First action based on role (e.g., Topic shortlist, coursework planning, grant search)]
```
