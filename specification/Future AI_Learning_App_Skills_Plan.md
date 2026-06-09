# AI-Powered Interactive Learning Web Application
## Skills Audit & Development Plan

**Project Owner:** Sanjay (Faculty, REVA University)  
**Project Purpose:** Interactive web application for AI-era student learning  
**Source Content:** AI ready Assignments.pptx  
**Target Users:** REVA BTech CS Students  
**Status:** Requirements gathering phase (content file not yet uploaded)

---

## 1. REQUIRED AGENT SKILLS (SKILL.md Modules)

Based on the project scope, the following agent skills are required:

### **Tier 1: Core Project Skills** (Critical Path)

| Skill Name | SKILL.md Location | Purpose | Trigger Conditions |
|---|---|---|---|
| **reva-session-designer** | `/mnt/skills/user/reva-session-designer/SKILL.md` | Design pedagogically rich session material, lecture slides, interactive activities, quizzes, pre-reading, assignments | When faculty uploads course design or fills intake form; requests session material generation for BTech CS courses |
| **reva-branding** | `/mnt/skills/user/reva-branding/SKILL.md` | Apply REVA University brand guidelines to all visual/document outputs | Before creating any CSS, choosing fonts/colours, placing logos, or designing HTML/PPTX/DOCX for REVA content |
| **frontend-design** | `/mnt/skills/public/frontend-design/SKILL.md` | Build production-grade, visually distinctive web interfaces and interactive components | When creating web components, pages, dashboards, React/HTML layouts, or styling interactive UIs |

### **Tier 2: Supporting Content Skills** (Highly Recommended)

| Skill Name | SKILL.md Location | Purpose | Trigger Conditions |
|---|---|---|---|
| **pptx** | `/mnt/skills/public/pptx/SKILL.md` | Create, edit, parse PowerPoint presentations with pedagogical quality control | When generating lecture slides, extracting content from PowerPoint files, ensuring visual polish |
| **docx** | `/mnt/skills/public/docx/SKILL.md` | Create, edit, manage Word documents with REVA branding | When producing assignment briefs, study guides, supplementary handouts in Word format |
| **pdf-reading** | `/mnt/skills/public/pdf-reading/SKILL.md` | Extract, inspect, rasterize PDF content (especially if assignments are PDF-based) | When parsing PDF assignment files, extracting text/tables/images for content inventory |
| **file-reading** | `/mnt/skills/public/file-reading/SKILL.md` | Route file processing based on file type (pdf, docx, xlsx, csv, json, images, etc.) | When user uploads mixed file types; serves as router to determine correct extraction tool |

### **Tier 3: Knowledge & Quality Assurance Skills** (Recommended for Later Phases)

| Skill Name | SKILL.md Location | Purpose | Trigger Conditions |
|---|---|---|---|
| **reva-course-reviewer** | `/mnt/skills/user/reva-course-reviewer/SKILL.md` | Review course design documents for pedagogical quality, Bloom's alignment, technical correctness | When auditing or validating the course design before or after material generation |

---

## 2. SKILL DEPENDENCIES & INTEGRATION MAP

```
┌─────────────────────────────────────────────────────────────┐
│ INPUT: AI ready Assignments.pptx (uploaded by faculty)      │
└────────────────────────┬────────────────────────────────────┘
                         │
                    ┌────▼─────────────┐
                    │ file-reading     │ (router)
                    │ pdf-reading      │ (if PDF-embedded)
                    └────┬─────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
    ┌───▼──────┐    ┌───▼──────┐    ┌───▼──────┐
    │Extract   │    │Extract   │    │Extract   │
    │Text/TOC  │    │Images    │    │Metadata  │
    └───┬──────┘    └───┬──────┘    └───┬──────┘
        │                │                │
        └────────────────┼────────────────┘
                         │
              ┌──────────▼────────────┐
              │ reva-session-designer │ (CORE)
              │ - Intake form flow    │
              │ - Pedagogical planning│
              │ - Blueprint approval  │
              └──────────┬────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼──────┐  ┌────▼──────┐  ┌────▼──────┐
    │ pptx       │  │ html/React │  │ docx       │
    │ (slides)   │  │ (interactive)  │ (briefs)   │
    └────┬───────┘  └────┬────────┘  └────┬──────┘
         │               │                │
    ┌────▼──────┐  ┌────▼──────┐  ┌────▼──────┐
    │reva-       │  │frontend-  │  │reva-      │
    │branding    │  │design     │  │branding   │
    │(orange/    │  │(visual UX)│  │(colours/  │
    │grey/logo)  │  │(animations)   │fonts/logo)│
    └────┬───────┘  └────┬────────┘  └────┬──────┘
         │               │                │
         └───────────────┼────────────────┘
                         │
              ┌──────────▼────────────┐
              │ OUTPUT FILES:         │
              │ - PPTX slide deck     │
              │ - HTML interactive   │
              │ - DOCX assignment    │
              │ - Pre-reading guides  │
              └───────────────────────┘
```

---

## 3. SKILL CAPABILITIES ALIGNED TO PROJECT REQUIREMENTS

### **Session Design & Content Generation**
**Skill:** `reva-session-designer`
- ✅ Extracts course metadata from uploaded course design documents
- ✅ Provides structured intake form if document unavailable
- ✅ Creates pedagogically sound 8-step session arc (Hook → Debrief)
- ✅ Generates Session Blueprint (internal doc, faculty-approved before slide generation)
- ✅ Applies Cognitive Load Theory, Dual Coding, Retrieval Practice, Socratic Questioning
- ✅ Outputs PPTX + HTML combo

### **Visual Design & Branding**
**Skills:** `reva-branding` + `frontend-design`
- ✅ REVA brand consistency (Orange #F7A35B, Grey #4A4C55)
- ✅ Typography: Plus Jakarta Sans (headings), Glacial Indifference (body)
- ✅ Logo placement & clear space rules
- ✅ Responsive, mobile-friendly HTML layouts
- ✅ Production-grade aesthetics (no generic AI design)
- ✅ Dual-coding visuals (diagrams, animations, graphics alongside text)

### **Content Formats**
**Skills:** `pptx`, `docx`, `pdf-reading`
- ✅ PPTX: 20–30 slides for 60-minute session; Cognitive Load Theory chunking
- ✅ HTML: Single self-contained file; Kahoot-style quizzes; drag-and-drop activities
- ✅ DOCX: Assignment briefs, rubrics, study guides
- ✅ PDF extraction: Parse uploaded assignments to inform activity design

### **Interactive Features**
**Skills:** `frontend-design` + `reva-session-designer` HTML component specs
- ✅ MCQ quizzes with instant feedback & score tracking
- ✅ Kahoot-style rapid-fire quiz (timed, leaderboard simulation)
- ✅ Drag-and-drop matching/classification
- ✅ Scenario branching for case studies
- ✅ Animated process/algorithm diagrams
- ✅ Socratic question reveal sequences
- ✅ Practice problems with hints & solutions

### **Pedagogical Quality Assurance**
**Skill:** `reva-course-reviewer` (optional, post-generation)
- ✅ Validates Bloom's taxonomy alignment
- ✅ Checks CO (Course Outcome) mapping
- ✅ Assesses learning effectiveness
- ✅ Reviews pedagogical soundness of activities

---

## 4. DEPLOYMENT ROADMAP

### **Phase 1: Foundation Setup** (Week 1–2)
**Goal:** Prepare environment & intake process

**Deliverables:**
- [ ] Confirm source file upload: `AI ready Assignments.pptx`
- [ ] Extract course metadata (course code, module structure, session count, CO list)
- [ ] Prepare REVA Session Intake Form (from reva-session-designer references)
- [ ] Set up brand asset folder (logos, fonts, colour swatches)

**Skills Activated:**
- `file-reading` (route uploaded file)
- `pdf-reading` (if PDF-based assignments)
- `pptx` (extract content from AI ready Assignments.pptx)

**Deliverable Artifact:**
- Course metadata spreadsheet (sessions, topics, COs, Bloom's levels)

---

### **Phase 2: Single-Session Prototype** (Week 3–4)
**Goal:** Generate complete material for one representative session (Session 1 or 2)

**Workflow:**
1. Select one session from the course
2. Collect intake data (Section Step 1 of reva-session-designer)
3. Run research phase (web search for pre-reading, videos, activities) — Step 2
4. Generate Session Blueprint — Step 3
5. Faculty reviews & approves blueprint
6. Generate PPTX slides (20–30 slides) — Step 4 + pptx skill
7. Generate interactive HTML companion — Step 5 + frontend-design skill
8. Generate assignment brief (DOCX) — docx skill
9. QA loop (text extraction, visual inspection, URL verification) — Step 6
10. Deliver files to `/mnt/user-data/outputs/` — Step 7

**Skills Activated:**
- `reva-session-designer` (full pipeline: intake → research → blueprint → planning)
- `pptx` (slide deck generation + QA)
- `frontend-design` (HTML/interactive component design)
- `docx` (assignment brief generation)
- `reva-branding` (consistent styling across all outputs)
- `web_search` (pre-reading resources, videos, activity ideas)

**Quality Gates:**
- [ ] Blueprint approved by faculty
- [ ] PPTX extracted & visually inspected (no overlaps, proper contrast)
- [ ] HTML opens in browser & quizzes function correctly
- [ ] All web links verified (curl check)
- [ ] REVA branding applied consistently

**Deliverable Artifacts:**
```
outputs/
├── CS_AI_Module1_Session1_Slides.pptx
├── CS_AI_Module1_Session1_Interactive.html
├── CS_AI_Module1_Session1_Assignment.docx
└── Session1_Blueprint.md (internal document, reference only)
```

---

### **Phase 3: Full Course Rollout** (Week 5–8)
**Goal:** Generate material for all remaining sessions

**Workflow:**
- Repeat Phase 2 workflow for each session (parallelizable)
- Intake form → Research → Blueprint → Approval → Generation → QA
- Incremental testing & faculty feedback integration

**Optimization:**
- Batch session blueprints (Step 3) for concurrent review
- Parallel web searches across sessions
- Reuse activity templates & code patterns

**Skills Activated:**
- All Phase 2 skills (repeated across sessions)

**Deliverable Artifacts:**
```
outputs/
├── CS_AI_Module1_Session1_Slides.pptx
├── CS_AI_Module1_Session1_Interactive.html
├── CS_AI_Module1_Session1_Assignment.docx
├── CS_AI_Module2_Session1_Slides.pptx
├── CS_AI_Module2_Session1_Interactive.html
├── CS_AI_Module2_Session1_Assignment.docx
├── ...
└── CS_AI_Module{N}_Session{M}_Slides.pptx
```

---

### **Phase 4: Integration & Deployment** (Week 9–10)
**Goal:** Bundle materials into self-study web app

**Workflow:**
1. Create course landing page (HTML + React if needed)
2. Build session navigator (sidebar / card grid)
3. Embed all HTML interactive companions into main app
4. Add progress tracking (optional: localStorage or backend)
5. Add assignment submission form (optional: email/LMS integration)
6. Package as single-page app or static site

**Optional Skills:**
- `frontend-design` (landing page, navigation UI)
- `reva-branding` (global theme/header/footer)

**Deliverable Artifacts:**
```
outputs/
├── index.html (course landing page)
├── sessions/
│   ├── module1-session1.html
│   ├── module1-session2.html
│   ├── module2-session1.html
│   └── ...
├── assets/
│   ├── styles.css (shared branding)
│   ├── logo.png
│   └── fonts/
└── README.md (deployment guide)
```

---

### **Phase 5: Validation & Iteration** (Week 11–12)
**Goal:** Student testing & refinement

**Workflow:**
1. Pilot with small student cohort (5–10 students)
2. Collect feedback on:
   - Content clarity & pacing
   - Interactive activity engagement
   - Assignment relevance
   - UI usability (mobile, desktop)
3. Iterate based on feedback
4. Use `reva-course-reviewer` to validate pedagogical quality

**Skills Activated:**
- `reva-course-reviewer` (post-generation validation)
- `frontend-design` (UX refinements)

**Deliverable:** Refined course material + feedback report

---

## 5. TECHNICAL STACK & CONSTRAINTS

### **Backend / Infrastructure**
- No backend required initially (static HTML/PPTX)
- Optional: LMS integration (Canvas, Moodle, Blackboard)
- Optional: Firebase/Supabase for progress tracking

### **Frontend Stack (Phase 4+)**
- **HTML**: Single self-contained files (no build step)
- **CSS**: Tailwind CDN (no build required) + custom CSS for REVA branding
- **JavaScript**: Vanilla JS for quizzes & interactions
- **React** (optional): If interactive activities require state management
- **Animations**: CSS-only for performance; Motion library if React is used

### **Content Formats**
- **PPTX**: python-pptx library (via pptx skill)
- **DOCX**: python-docx library (via docx skill)
- **HTML**: Hand-coded or generated via Claude API (see anthropic_api_in_artifacts)
- **PDFs**: pypdf / pdf2image (via pdf skill)

### **Branding Assets**
- REVA logo: Wikimedia Commons URL (provided in reva-branding skill)
- Fonts: Google Fonts (Plus Jakarta Sans, Glacial Indifference)
- Colours: HEX codes in CSS variables

### **Content Source**
- Primary: `AI ready Assignments.pptx` (faculty-provided)
- Secondary: Web search (pre-reading, videos, activity ideas)
- Tertiary: NPTEL, GeeksForGeeks, MIT OCW, Programiz (curated sources)

---

## 6. SKILL ACTIVATION CHECKLIST

Use this checklist to ensure all required skills are referenced during development:

### **Phase 1: Foundation**
- [ ] `file-reading` — route uploaded files correctly
- [ ] `pptx` — extract content from AI ready Assignments.pptx
- [ ] `pdf-reading` — if assignments are PDF-based

### **Phase 2: Single-Session Prototype**
- [ ] `reva-session-designer` — full intake → blueprint → generation pipeline
  - [ ] Step 0: Confirm file upload & read pptx skill
  - [ ] Step 1: Complete intake (course metadata, session CO, Bloom's)
  - [ ] Step 2: Run web searches (pre-reading, videos, activities)
  - [ ] Step 3: Generate Session Blueprint
  - [ ] Step 4: Generate PPTX slides
  - [ ] Step 5: Generate interactive HTML
  - [ ] Step 6: QA (text extraction, visual inspection)
  - [ ] Step 7: Deliver to /outputs/
- [ ] `pptx` — slide deck generation + format validation
- [ ] `docx` — assignment brief generation
- [ ] `frontend-design` — HTML interactive component design
- [ ] `reva-branding` — consistent brand application (colors, fonts, logos)
- [ ] `web_search` — pre-reading resources, videos, curated sources

### **Phase 3: Full Course Rollout**
- [ ] `reva-session-designer` — repeat for all remaining sessions
- [ ] `pptx`, `docx`, `frontend-design`, `reva-branding` — apply consistently

### **Phase 4: Integration & Deployment**
- [ ] `frontend-design` — landing page, navigation, global UI
- [ ] `reva-branding` — apply at application level

### **Phase 5: Validation & Iteration**
- [ ] `reva-course-reviewer` — pedagogical quality assurance (optional but recommended)
- [ ] `frontend-design` — UX refinements based on feedback

---

## 7. RISK MITIGATION & SUCCESS CRITERIA

### **Key Risks**

| Risk | Mitigation | Owner |
|---|---|---|
| Source file (AI ready Assignments.pptx) not uploaded or incomplete | Set deadline for file upload; provide template if missing | Sanjay |
| Pedagogical quality compromised by rushed content | Use reva-course-reviewer for post-generation audit | Claude (reva-session-designer) |
| REVA branding inconsistency across outputs | Always trigger reva-branding before CSS/design decisions | Claude (all visual skills) |
| Interactive activities too complex or fail in browser | Test all HTML/JS in Phase 2 prototype; simplify if needed | Claude (frontend-design) |
| Student engagement low due to poor activity design | Pilot with cohort in Phase 5; iterate based on feedback | Sanjay + Claude |
| Timeline slippage due to scope creep | Stick to Phase 2 prototype; defer Phase 4 integration to Phase 5+ | Project PM |

### **Success Criteria**

- [ ] **Phase 1:** Course metadata extracted & validated ✓
- [ ] **Phase 2:** Single session generates PPTX + HTML + DOCX; all files render correctly ✓
- [ ] **Phase 3:** All sessions generated; no content gaps or broken links ✓
- [ ] **Phase 4:** Standalone web app launches; all pages navigate & load smoothly ✓
- [ ] **Phase 5:** Pilot cohort achieves >80% task completion; >4/5 satisfaction rating ✓

---

## 8. NEXT STEPS (Immediate Actions)

1. **Upload `AI ready Assignments.pptx`** to Claude chat
2. **Confirm course metadata:**
   - Course code & name
   - Module structure (# of modules)
   - Session count per module
   - Course Outcomes (COs) list
   - Target Bloom's levels
3. **Schedule intake discussion:**
   - Select Session 1 for prototype
   - Fill REVA Session Intake Form
   - Confirm pre-reading preferences & activity types
4. **Agree on Phase 2 timeline:**
   - Intake: Day 1
   - Blueprint review & approval: Day 2–3
   - Material generation: Day 4–5
   - QA & refinement: Day 6–7

---

## Appendix: Skills Quick Reference

**reva-session-designer** — `/mnt/skills/user/reva-session-designer/SKILL.md`
- 7-step pipeline: Intake → Research → Blueprint → Slides (PPTX) → Interactive (HTML) → QA → Deliver
- Mandatory output: 8-step session arc with Cognitive Load Theory, Dual Coding, Socratic Q
- Pedagogy: Bloom's alignment, CO mapping, retrieval practice, spaced learning

**reva-branding** — `/mnt/skills/user/reva-branding/SKILL.md`
- Colours: Orange #F7A35B, Grey #4A4C55, White #FFFFFF
- Fonts: Plus Jakarta Sans (headings), Glacial Indifference (body)
- Logo: Primary or reverse (white) only; clear space rules
- Output-specific rules for HTML, PPTX, DOCX, social media

**frontend-design** — `/mnt/skills/public/frontend-design/SKILL.md`
- Production-grade, visually distinctive web interfaces
- Bold aesthetic choices; avoid generic AI design
- Typography, colour, motion, spatial composition, visual details
- HTML/CSS/JS + React; Tailwind CDN

**pptx, docx, pdf-reading, file-reading** — see skill locations for mechanics

