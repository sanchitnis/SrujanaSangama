# User Onboarding Domain (Srujana Onboarding Pack)

> **Domain Path:** `domains/onboarding` | **Agent Handle:** `@claw` (Personal Productivity & Onboarding) | **Version:** 2.0.0

The entry point and initialization gateway for all SrujanaSangama users (Faculty, PhD Scholars, and Student Researchers). This domain is responsible for onboarding the user, asking for their role, credentials, professional profiles, and resume, and scaffolding their local read-write `srujana-memory/` workspace parent folder.

---

## 🎓 Core Capabilities

### 1. Workspace Scaffolding
- Creates the local three-tier storage directory architecture (`srujana-memory/` workspace, `my-memory/`, `public-memory/`, `collaborations/`).
- Binds `SrujanaSangama`, `srujana-memory`, and `reva-information` siblings into a unified multi-root `.code-workspace` file.

### 2. Profile Generation & Mapping
- **Identity Anchor**: Generates `soul.md` containing core roles, school designation, and teaching/study topics.
- **Academic Standing**: Formulates `my-memory/semantic/profile.md` and CV profile inside `public-memory/profile.md`.
- **Goals & Sankalpas**: Sets up the Goal-Plan-Sankalpa (GPS) structure inside `my-memory/gps/sankalpa-current.md` and `goals-current.md`.

### 3. Professional Links & Resume Upload
- **Academic Identifiers**: Integrates user profile links for LinkedIn, Google Scholar, IRINS, VIDWAN, ORCID iD, and Web of Science ID.
- **Portfolio Seed**: Uploads and copies the user's digital resume file to `public-memory/resume.<extension>`.
- **Profile Extraction**: Extracts past publications, grants, academic tenures, and expertise from the provided links and resume to pre-populate semantic profile files.

---

## 🛠️ Slash Commands & Scripts

- **`/onboard`**: Triggers the interactive onboarding interview to capture roles, responsibilities, research identifiers, and resume uploads.
- **`/resume-audit`**: Audits the copied resume file (inside `public-memory/`) against UGC recruitment/shortlisting criteria, AICTE 360-degree feedback criteria, and standard ATS formatting rules. It outputs a positive-first, private improvement report inside `my-memory/resume-audit-report.md`.
- **`scripts/local/init.py`**: The local CLI-based python script that performs the identical onboarding workflow offline, creating directories and copying files without requiring active LLM API calls.

---

## 📂 Directory Layout

```plaintext
domains/onboarding/
├── README.md           # This file
├── commands/
│   ├── 00_onboarding.md  # Onboarding command prompt specification
│   └── resume-audit.md   # Resume audit command prompt specification
└── rules/              # Optional domain boundary policies
```
