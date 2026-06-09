# Skills Audit & Development Plan — Executive Summary

**Project:** AI-Powered Interactive Web Application for Student Learning  
**Institution:** REVA University, Bengaluru  
**Faculty:** Sanjay  
**Status:** Requirements gathering phase  
**Document Date:** April 2026

---

## 📋 Quick Reference: Required Skills

### **Tier 1: Critical Path** (Must use for core project)

| Skill | File Location | Primary Use | Phase Activated |
|-------|---|---|---|
| **reva-session-designer** | `/mnt/skills/user/reva-session-designer/SKILL.md` | Pedagogical content design, slide generation, interactive activities, 7-step session pipeline | Phase 2 onwards |
| **reva-branding** | `/mnt/skills/user/reva-branding/SKILL.md` | REVA-compliant styling (colors, fonts, logos) — applied to all visual outputs | All phases |
| **frontend-design** | `/mnt/skills/public/frontend-design/SKILL.md` | Production-grade web UI, interactive widgets, HTML/CSS/JS | Phase 2 onwards |

### **Tier 2: Highly Recommended** (Support content creation)

| Skill | File Location | Primary Use | Phase Activated |
|-------|---|---|---|
| **pptx** | `/mnt/skills/public/pptx/SKILL.md` | PowerPoint slide deck generation, text extraction, QA | Phase 1 onwards |
| **docx** | `/mnt/skills/public/docx/SKILL.md` | Word document creation (assignment briefs, study guides) | Phase 2 onwards |
| **pdf-reading** | `/mnt/skills/public/pdf-reading/SKILL.md` | Extract text/images/tables from PDF assignments | Phase 1 (if applicable) |
| **file-reading** | `/mnt/skills/public/file-reading/SKILL.md` | Route uploaded files to correct processing tool | Phase 1 onwards |
| **web_search** | Built-in tool | Find pre-reading resources, videos, activity ideas | Phase 2 onwards |

### **Tier 3: Optional (Quality Assurance)** 

| Skill | File Location | Primary Use | Phase Activated |
|-------|---|---|---|
| **reva-course-reviewer** | `/mnt/skills/user/reva-course-reviewer/SKILL.md` | Post-generation pedagogical audit (Bloom's alignment, CO mapping, learning effectiveness) | Phase 5 (optional but recommended) |

---

## 🎯 High-Level Workflow

```
Upload AI ready Assignments.pptx
        ↓
   [file-reading / pptx]
        ↓
Extract course metadata, sessions, COs, Bloom's levels
        ↓
   [reva-session-designer STEP 1: Intake]
        ↓
Select one session for prototype (Phase 2)
        ↓
   [reva-session-designer STEP 2-5: Research → Blueprint → Generation]
   ├─ [pptx] → Slide deck (20–30 slides)
   ├─ [frontend-design] → Interactive HTML
   ├─ [docx] → Assignment brief
   └─ [reva-branding] → Applied to all three ↑
        ↓
   [reva-session-designer STEP 6-7: QA → Deliver]
        ↓
OUTPUTS: .pptx + .html + .docx for Session 1
        ↓
Repeat for all remaining sessions (Phase 3)
        ↓
Integration & deployment (Phase 4)
        ↓
Pilot testing & iteration (Phase 5)
```

---

## 📅 Project Timeline

| Phase | Duration | Goal | Key Deliverables |
|-------|----------|------|---|
| **1: Foundation** | Week 1–2 | Upload file, extract metadata, prepare intake form | Metadata spreadsheet, intake form |
| **2: Prototype** | Week 3–4 | Generate complete materials for one session | 1× PPTX + HTML + DOCX package |
| **3: Rollout** | Week 5–8 | Generate all remaining sessions | N× session packages (parallel) |
| **4: Integration** | Week 9–10 | Build standalone web app with navigation | Course landing page + embedded sessions |
| **5: Validation** | Week 11–12 | Pilot with students, iterate | Refined materials + feedback report |

**Total duration:** 12 weeks (assuming file upload by start of Week 1)

---

## ⚡ Critical Success Factors

1. **Source file upload (BLOCKER):**  
   File `AI ready Assignments.pptx` must be uploaded to Claude chat before Phase 1 work begins. Without it, no content extraction is possible.

2. **Intake form completion (GATE):**  
   All Phase 2 work is blocked until intake data is collected (course metadata, session CO, Bloom's level, duration, learning outcomes, activity preferences).

3. **Blueprint approval (GATE):**  
   Session Blueprint (internal pedagogical document) must be reviewed and approved by faculty before slide/interactive generation begins. This prevents rework.

4. **Consistent branding (QUALITY):**  
   Always trigger `reva-branding` skill BEFORE writing CSS or choosing fonts/colors. Branding inconsistency compounds across N sessions.

5. **QA discipline (QUALITY):**  
   Phase 2 prototype must complete the full QA loop (text extraction, visual inspection, URL checks) before Phase 3 begins. Early issues inform process improvements.

---

## 🛠️ Skill Activation Checklist

Use this during development to ensure all required skills are properly triggered:

### **Phase 1: Foundation**
- [ ] `file-reading` called to route uploaded file
- [ ] `pptx` called to extract course structure from AI ready Assignments.pptx
- [ ] `pdf-reading` called (if any PDF content in the file)
- [ ] Metadata spreadsheet generated with all sessions, topics, COs, Bloom's levels

### **Phase 2: Single-Session Prototype**
**CORE PIPELINE:**
- [ ] `reva-session-designer` Step 0: File reading complete, `pptx` skill read
- [ ] `reva-session-designer` Step 1: Intake data collected & confirmed
- [ ] `reva-session-designer` Step 2: Web searches run for pre-reading, videos, activity ideas
- [ ] `reva-session-designer` Step 3: Session Blueprint generated & faculty-approved
- [ ] `reva-session-designer` Step 4: PPTX slides generated with `pptx` skill
- [ ] `reva-session-designer` Step 5: Interactive HTML generated with `frontend-design` skill
- [ ] `reva-branding` applied to PPTX (colors, fonts, logo placement)
- [ ] `reva-branding` applied to HTML (colors, fonts, logo placement)
- [ ] `docx` skill used to generate assignment brief
- [ ] `reva-branding` applied to DOCX (header/footer, colors, fonts)
- [ ] `reva-session-designer` Step 6: Full QA loop executed (text extraction, visual check, URLs verified)
- [ ] `reva-session-designer` Step 7: Deliverables moved to `/mnt/user-data/outputs/`

**QUALITY GATES:**
- [ ] Blueprint approved by faculty
- [ ] PPTX extracted and visually inspected (no overlaps, contrast OK)
- [ ] HTML opens in browser, all quizzes/interactions functional
- [ ] All external URLs verified (curl or manual check)
- [ ] REVA branding consistent across all 3 file types

### **Phase 3: Full Course Rollout**
- [ ] All Phase 2 skills triggered for each additional session
- [ ] Parallel session intake & blueprints for efficiency
- [ ] Incremental faculty feedback incorporated

### **Phase 4: Integration & Deployment**
- [ ] `frontend-design` called for course landing page
- [ ] `reva-branding` applied at application-level (global header, footer, theme)
- [ ] All HTML interactive companions embedded into main app

### **Phase 5: Validation & Iteration**
- [ ] `reva-course-reviewer` called to audit pedagogical quality (optional but recommended)
- [ ] Pilot cohort feedback collected
- [ ] Materials refined based on feedback

---

## 💡 Skill Usage Highlights

### **reva-session-designer (Tier 1 — CRITICAL)**
This skill is the core of the entire project. It orchestrates 7 sequential steps:
1. **Intake**: Collect course metadata, CO, Bloom's level, learning outcomes, activity preferences
2. **Research**: Web search for curated pre-reading, videos, activity analogies
3. **Blueprint**: Generate 8-step session arc with pedagogical principles (Cognitive Load Theory, Dual Coding, Socratic Q, Retrieval Practice)
4. **PPTX Generation**: 20–30 slides using `pptx` skill, mandatory 8-step arc
5. **HTML Companion**: Single self-contained interactive file with quizzes, activities, scenario branching
6. **QA**: Full validation loop (text extraction, visual inspection, link verification)
7. **Deliver**: Move files to `/mnt/user-data/outputs/`

**Do not skip or combine steps.** The pipeline is sequential; skipping Step 3 (Blueprint approval) leads to rework.

### **reva-branding (Tier 1 — MANDATORY)**
Apply this skill **before** making any visual design decisions:
- **Colors**: Always use REVA Orange (#F7A35B) + REVA Grey (#4A4C55) + White (#FFFFFF). No other colors permitted.
- **Fonts**: Plus Jakarta Sans (headings), Glacial Indifference (body). Google Fonts import required for HTML.
- **Logos**: REVA logo (primary or white reverse) only. Clear space 2× top/bottom, 4× sides. Top-right placement on slides.
- **Output rules**: Different for PPTX, DOCX, HTML, and social media. Skill specifies each.

### **frontend-design (Tier 1 — CRITICAL FOR INTERACTIVITY)**
Creates the interactive HTML companion with:
- **Responsive design** (mobile + desktop)
- **Visual distinctiveness** (bold aesthetic, not generic AI design)
- **Interactive widgets**: Kahoot-style quizzes, drag-and-drop, scenario branching, animated diagrams
- **REVA branding** applied (uses CSS variables from reva-branding)
- **Accessibility**: ARIA labels, keyboard navigation, contrast compliance

**Key output requirement**: Single self-contained HTML file (no external dependencies except CDN). Can be opened offline.

### **pptx (Tier 2)**
Generates PowerPoint slides with:
- Text extraction & validation (check for overflow, missing content)
- QA loop (extract to markdown, convert to images, verify visually)
- REVA-branded styling (colors, fonts, logo placement)

### **docx (Tier 2)**
Creates assignment briefs & study guides with:
- REVA header (orange bar + logo)
- Structured content (task, rubric table, Bloom's level, submission format)
- REVA-branded styling (colors, fonts, footer with university name)

### **reva-course-reviewer (Tier 3 — OPTIONAL)**
Used after all materials are generated to audit:
- Bloom's taxonomy alignment (each LO tagged with verb)
- Course Outcome (CO) coverage (all course COs addressed across sessions)
- Learning effectiveness (pedagogical soundness, activity relevance)
- Technical correctness (no errors in code examples, formulas, references)

**Not required for Phase 2–4, but recommended for Phase 5 (pilot validation).**

---

## 🚀 Next Steps (Immediate)

### **Week 1, Day 1:**
1. **Upload `AI ready Assignments.pptx`** to Claude chat.
2. **Confirm with Sanjay:**
   - Course code, semester, year
   - Module structure (# of modules, # of sessions per module)
   - List of all Course Outcomes (COs)
   - Target Bloom's levels (Remember, Understand, Apply, Analyse, Evaluate, Create)

### **Week 1, Day 2–3:**
3. **Extract metadata** using `pptx` skill.
4. **Create course metadata spreadsheet** with columns:
   - Module #, Session #, Topic, CO(s), Bloom's level, Duration, Key concepts, Prerequisite knowledge

### **Week 1, Day 4–5:**
5. **Prepare REVA Session Intake Form** (template from reva-session-designer references).
6. **Select Session 1 (or most representative session) for Phase 2 prototype.**
7. **Schedule intake meeting** to fill form and confirm pedagogical details.

### **Week 2–3:**
8. **Begin Phase 2: Single-Session Prototype** following the full reva-session-designer 7-step pipeline.

---

## 📊 Skill Dependency Matrix

| Input | Skill 1 | Skill 2 | Skill 3 | Output |
|-------|---------|---------|---------|--------|
| .pptx file | `pptx` | file-reading | — | Course structure |
| Course structure | `reva-session-designer` | `web_search` | — | Session blueprint |
| Session blueprint | `pptx` | `reva-branding` | — | PPTX slides |
| Session blueprint | `frontend-design` | `reva-branding` | — | Interactive HTML |
| Session blueprint | `docx` | `reva-branding` | — | Assignment brief |
| All outputs | `reva-session-designer` (QA) | — | — | Validated files |

---

## 🎓 Pedagogical Principles Embedded in reva-session-designer

The skill implements these evidence-based principles automatically:

- **Cognitive Load Theory**: Content chunked into ≤3 concepts per slide; worked examples before problems
- **Dual Coding**: Text + visual (diagram, animation, illustration) on every concept slide
- **Retrieval Practice**: Unannounced recall quiz before main activity segment
- **Socratic Questioning**: 3–5 escalating questions for analytical topics instead of direct explanation
- **Spaced Learning**: Resources provided for pre-reading; reinforcement in assignment
- **Interleaving**: Mix of concept, application, and practice within single session arc

No manual implementation needed — triggered automatically by reva-session-designer pipeline.

---

## ⚠️ Risk Mitigation

| Risk | Mitigation | Owner |
|------|-----------|-------|
| Source file never uploaded | Set Week 1, Day 1 deadline; provide file template if missing | Sanjay |
| Pedagogical quality issues | Use `reva-course-reviewer` in Phase 5; iterate early | Claude + Sanjay |
| REVA branding inconsistency | Always call `reva-branding` before design decisions | Claude (all visual skills) |
| Interactive activities too complex or break in browser | Test all HTML in Phase 2 prototype; simplify if needed | Claude (frontend-design) |
| Student engagement low | Pilot with cohort in Phase 5; adjust activity types based on feedback | Sanjay + Claude |
| Timeline slippage | Stick to Phase 2 prototype scope; defer Phase 4 integration to later if needed | Project PM (Sanjay) |

---

## 📚 Reference Documents

- **Full Skills Plan**: `AI_Learning_App_Skills_Plan.md` (12-section comprehensive guide)
- **reva-session-designer references**: `references/intake-form.md` (to present if no course design doc), `references/pedagogy.md` (teaching principles guide)
- **reva-branding logo**: https://upload.wikimedia.org/wikipedia/commons/5/5f/REVA_University_Bangalore.png
- **Fonts**: Plus Jakarta Sans (Google Fonts), Glacial Indifference (fallback to sans-serif in HTML)
- **Curated content sources**: GeeksForGeeks, MIT OpenCourseWare, NPTEL, Programiz (preferred in web_search queries)

---

## ✅ Definition of Done (Phase 2 Prototype)

A single-session package is complete when:

- [ ] Session Blueprint reviewed and approved by faculty
- [ ] PPTX deck (20–30 slides) generated with REVA branding
  - [ ] Title, pre-reading, videos, learning outcomes, hook, concept build, retrieval check, activity, practice, debrief, assignment
  - [ ] Every slide has a visual element (diagram, animation, screenshot)
  - [ ] Colours, fonts, logo placement follow REVA branding
  - [ ] No text overflow, proper contrast on light/dark backgrounds
- [ ] Interactive HTML companion generated
  - [ ] Session header, pre-reading panel, video panel, concept check quiz, activity widget, practice problem, assignment card
  - [ ] All MCQs with instant feedback + score tracking
  - [ ] Kahoot-style rapid quiz (if applicable)
  - [ ] Mobile responsive, print-friendly
  - [ ] All URLs verified and working
- [ ] Assignment brief (DOCX) generated
  - [ ] Task description, rubric table (criteria + marks), Bloom's level tag, submission format
  - [ ] REVA header and footer applied
- [ ] All files QA'd:
  - [ ] PPTX: Text extracted, visually inspected, no errors
  - [ ] HTML: Opened in browser, all interactions tested
  - [ ] DOCX: Formatted correctly, REVA branding applied
- [ ] All files copied to `/mnt/user-data/outputs/`
- [ ] Session arc verified:
  - [ ] 8-step structure (Hook → Debrief) present
  - [ ] Cognitive Load Theory chunking visible
  - [ ] At least one retrieval practice quiz present
  - [ ] Activity type justified for Bloom's level
  - [ ] All COs addressed

**Once Phase 2 is complete, Phase 3 (full rollout) can proceed in parallel for remaining sessions.**

---

## 📞 Escalation Path

If any issue arises during development:

1. **Content gaps or unclear CO mapping** → Consult with Sanjay for clarification
2. **Pedagogical concerns** → Use `reva-course-reviewer` skill (Tier 3) for audit
3. **REVA branding questions** → Always reference `/mnt/skills/user/reva-branding/SKILL.md` — it is the source of truth
4. **Interactive widget failures** → Simplify complexity; test in browser; refer to `frontend-design` skill
5. **Timeline pressure** → Cut scope (defer Phase 4 integration, focus on pedagogical quality in Phase 2–3)

---

**Document prepared for:** Sanjay, Faculty Member, REVA University  
**Prepared by:** Claude (AI Assistant)  
**Date:** April 16, 2026

