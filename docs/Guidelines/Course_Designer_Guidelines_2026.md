# Course Designer Guidelines — 2026 Scheme

> **Who this is for.** Faculty and SIG teams designing or revising any course in the 2026 B.Tech scheme (CSE, ISE, IT, AIML, AIDS, IoT, Cyber Security).
>
> **What it does.** It translates the curriculum strategy into concrete design rules, organized by the **course category** and **L-T-P pattern** the course carries — because a 3-0-0 theory foundation course and a 0-0-2 workshop need very different designs. Use the decision table in §2 to find your course type, then follow the rules for that type plus the universal rules in §1.
>
> **Companion document.** Every course produces a Course File using the *Course File Template — Dual-Level*. These guidelines tell you how to **design** the course; the template tells you how to **document** it.

---

## 0. Two decisions that must already be fixed before you start

These are **program-level** decisions, made once centrally — not by individual designers. Confirm they exist before designing assessment:

1. **The official awareness/advanced mark ratio.** The institution computes, against REVA's marks-to-grade-point conversion, the split that makes an awareness-only student land **below the 8-CGPA band**. Every theory/integrated course uses this single fixed ratio (illustratively ~70/30). Do **not** invent your own.
2. **A filled reference exemplar.** One fully designed course (scope table + assessment split) circulated as the calibration standard, so "advanced level" means the same thing across all courses.

If either is missing, flag it — designing assessment without them will break the cross-course consistency the CGPA signal depends on.

---

## 1. Universal rules (every course, every category)

1. **Outcome-first.** Write Course Outcomes (COs) before content. Each CO maps to PO/PSO and is tagged with a **Bloom taxonomy level** (Remember / Understand / Apply / Analyse / Evaluate / Create). Remember–Apply = awareness floor; Analyse–Create = advanced ceiling.
2. **Two levels in one course.** Never stream students into sections. Design one course delivered at an **awareness floor** (every student must clear it) and an **advanced ceiling** (depth for the strong), separated by **assessment**, anchored to Bloom verbs (floor = Remember/Understand/Apply; ceiling = Analyze/Evaluate/Create).
3. **The floor protects employability.** Awareness-level content must map to the CSCore / entrance-test / placement competencies the course is responsible for. State that mapping explicitly.
4. **Currency.** Content reflects recruiter- and future-job-aligned needs and is reviewed every cycle. Perishable tool/tech specifics belong in workshops and labs, not frozen into theory syllabi.
5. **Continuous assessment.** Favor frequent low-stakes assessment over a single high-stakes exam, especially for the at-risk majority.
6. **Honest contact-hour budgeting.** Design to the real contact hours implied by L-T-P (see §3), not to an idealized self-study assumption — most of the cohort will not self-study.
7. **Differentiated support is mandatory, not optional.** Every course design names both a remediation path (reach the floor) and an enrichment path (reach the ceiling).
8. **Academic integrity & accessibility.** Design assessments resistant to trivial AI-completion where the CO is about the student's own competence; design for the rural/biology-background intake by never assuming unstated prior exposure.

---

## 2. Find your course type

| Category code | Meaning | Typical L-T-P | Go to |
|---|---|---|---|
| FC | Foundation Course (math, science, humanities, management) | 3-0-0, 2-1-0, 1-0-0 | §4.1 |
| HC (theory) | Hard Core program theory | 3-0-0, 2-1-0 | §4.2 |
| HC (integrated) | Hard Core theory + embedded lab | 1-1-1, 2-0-1 | §4.3 |
| HC / standalone lab | Practical-only lab | 0-0-1 | §4.4 |
| W1–W8 | Workshop (just-in-time, SIG-designed) | 0-0-2 | §4.5 |
| SC / PEC | Soft Core / Professional Elective (SIG track) | 3-0-0 | §4.6 |
| OE | Open Elective (cross-discipline) | 3-0-0 | §4.7 |
| ETC | Emerging Technology Course | 1-0-0 | §4.8 |
| MC | Mandatory Course (non-credit / 0-credit: constitution, env science, IKS) | 0-0-0, 1-0-0 | §4.9 |
| AEC | Ability Enhancement (placement training) | 0-0-1 | §4.10 |
| Proj | Mini / Capstone Project | 0-0-2 to 0-0-8 | §4.11 |
| Intern | Internship | 0-0-4 | §4.12 |

---

## 3. How to read L-T-P (and what each implies)

**L = Lecture, T = Tutorial, P = Practical.** 1 credit ≈ 1 lecture hour, 1 tutorial hour, or 2 practical hours per week.

| Pattern | Reads as | Design implication |
|---|---|---|
| 3-0-0 | Pure theory | Conceptual mastery; advanced level lives in analysis/derivation questions, not lab work. |
| 2-1-0 | Theory + tutorial | Use the tutorial hour for guided problem-solving — your best lever for carrying the floor cohort. |
| 1-1-1 | Integrated theory-lab | Theory and practice interleave; the lab component is where advanced students build real artifacts. |
| 2-0-1 / 0-0-1 | Theory-light + lab / pure lab | Assessment is demonstration-based; rubric, not written exam, carries the level distinction. |
| 0-0-2 | Workshop / heavy practical | No formal lecture; entirely doing. Currency and just-in-time design dominate. |
| 0-0-4 … 0-0-8 | Project / internship | Deliverable-graded; the level distinction is contributor-grade vs owner-grade work. |

> **Golden rule:** the higher the P, the more the level distinction must live in a **rubric** rather than a **question paper**.

---

## 4. Rules by course type

### 4.1 Foundation Course (FC) — e.g. Calculus, Probability, Physics, Communicative English

- These carry the heaviest **intake-diversity** risk: the 40% biology-background and 30% rural students often arrive with the widest gaps here.
- **Awareness floor:** the foundational fluency every downstream course assumes. Make it genuinely reachable from a no-prior-exposure start — include a week-0 / bridge ramp where the gap is real.
- **Advanced ceiling:** application to engineering/CS problems, not just textbook computation.
- Use the **tutorial hour** (if T≥1) for remediation and worked examples; do not lecture into it.
- Continuous assessment essential — FCs are where Resistors disengage earliest.

### 4.2 Hard Core theory (HC, 3-0-0 / 2-1-0) — e.g. DBMS theory, Operating Systems, Computer Networks

- The backbone of CSCore and placement-readiness. Awareness floor **must** map to entrance-test topics.
- **Awareness floor:** define, explain, apply standard procedures to familiar problems.
- **Advanced ceiling:** compare/justify design choices, analyze complexity/trade-offs, solve novel problems.
- Apply the **fixed awareness/advanced mark ratio** (§0.1). Verify in the Course File that awareness-only < 8 CGPA.
- Blueprint every IA and the SEE so advanced questions are present and identifiable.

### 4.3 Hard Core integrated (HC, 1-1-1 / 2-0-1) — e.g. DSA, Design & Analysis of Algorithms, Deep Learning

- The **lab/practical credit is not decoration** — it is where advanced students demonstrate the ceiling.
- Split assessment across both modes: written (concept floor + analysis ceiling) **and** practical (implement floor + optimize/design ceiling).
- Map the practical tasks to real, current tooling; refresh tooling each cycle without changing the conceptual CO.
- Rubric for the practical component must distinguish *works* (floor) from *efficient/scalable/well-reasoned* (ceiling).

### 4.4 Standalone lab (HC, 0-0-1)

- Pure demonstration of skill. No written-exam ceiling — the **rubric is the entire level mechanism**.
- Define observable floor criteria (task completes correctly) and ceiling criteria (handles edge cases, optimizes, explains choices).
- Keep lab sheets current; this is a low-cost place to inject recent tools.

### 4.5 Workshop (W1–W8, 0-0-2) — SIG-owned, just-in-time

- **Titles in the scheme are indicative placeholders.** SIG teams design the actual content just-in-time so it reflects the technology landscape at the moment students take it.
- Students choose workshops within their SIG track, subject to management approval.
- Design for **doing**, not lecturing: a workshop with a lecture component is mis-designed.
- Currency is the whole point — tie each offering to live job postings / recruiter needs and re-author each cycle.
- Assessment is artifact + demonstration. Floor = a working deliverable; ceiling = a deliverable that shows judgment, extension, or production-readiness.
- Document the just-in-time rationale so the SIG can show why this offering, this cycle.

### 4.6 Soft Core / Professional Elective (SC/PEC, 3-0-0) — SIG track courses

- These are the **specialization tracks** (Agentic AI/Enterprise, AI-ML/Data Engineering, IoT/Blockchain/Automation, Cybersecurity services). Owned end-to-end by a SIG as a community of practice.
- Design the elective as one coherent sequence with the SIG's workshops, projects, and internship — not a standalone course.
- Recruiter/future-job aligned; expect to revise content faster than HC theory.
- Advanced ceiling here is closer to **professional contributor competence** than to exam performance — assess accordingly.
- Verticals (BFSI, Energy, etc.) should reflect REVA's actual recruiter concentration; keep broad where recruiters are diffuse.

### 4.7 Open Elective (OE, 3-0-0)

- Taken by students **from other programs** — do **not** assume CS prerequisites.
- Awareness floor must be reachable by a non-specialist; ceiling can reward those who connect it to their home discipline.
- Self-contained; no dependency on this program's HC chain.

### 4.8 Emerging Technology Course (ETC, 1-0-0) — e.g. AI Foundations for Engineers

- Light-credit, awareness-raising by nature. The goal is **literacy and motivation**, not mastery.
- Strategic role: early exposure that converts Passengers by showing where the progression path leads (e.g. a working agentic-AI demo in year 1).
- Keep it current and inspiring; assess by engagement/short artifact, not heavy exams.
- Do not over-engineer a dual-level split into a 1-credit literacy course — floor-only is acceptable here, stated explicitly.

### 4.9 Mandatory Course (MC, 0-credit) — Constitution & Cyber Law, Environmental Science, IKS

- Non-CGPA but required. Design for **completion and awareness**, not differentiation.
- No awareness/advanced split needed; a single competency floor with pass/complete grading.
- Keep assessment light and integrity-focused.

### 4.10 Ability Enhancement (AEC, 0-0-1) — Placement Training, every semester 3–6

- This **is** the CSCore placement spine made literal — steady drip, not a final-year crash.
- Align tightly and continuously to current recruiting-company entrance-test formats (which themselves shift as AI changes hiring).
- Floor = clears the entrance-test bar; track readiness per student and feed weak signals to academic mentors.
- Continuous, low-stakes, frequent.

### 4.11 Project (Proj, 0-0-2 → 0-0-8) — Mini Project 1/2, Capstone Phase I/II

- The progression ladder: Mini 1 → Mini 2 → Capstone I → Capstone II, with credits rising to make room for doing.
- **Level distinction = deliverable grade, not exam.** Define two rubric heights on the same brief:
  - **Contributor-grade** (Passenger-achievable, team-based, employment-oriented) — clears the floor.
  - **Owner-grade** (Explorer/Achiever, product-shipping) — reaches the ceiling.
- Same rubric, different ceilings — never different briefs that pre-label students.
- Capstone may **be** a venture for the ~5% entrepreneurship exit: same credits, same slot, different deliverable (shipped product / incorporated venture vs report).
- Briefs owned by the SIG and kept recruiter/future-job aligned.

### 4.12 Internship (Intern, 0-0-4)

- SIG-brokered where possible; quality of placement is the design variable.
- Assess by supervisor evaluation + reflective artifact mapped to COs.
- Floor = credible contribution and professional conduct; ceiling = ownership of a real deliverable.
- Feed internship performance back to the SIG track and to academic mentors.

---

## 5. Design checklist (run before submitting any course)

- [ ] COs written first, each tagged with a **Bloom taxonomy level** (Remember / Understand / Apply / Analyse / Evaluate / Create), mapped to PO/PSO.
- [ ] Awareness floor explicitly mapped to CSCore / placement competencies (where applicable).
- [ ] Advanced ceiling defined per unit using Bloom anchor; consistent with the reference exemplar.
- [ ] For theory/integrated: official awareness/advanced **mark ratio applied** and the *awareness-only < 8 CGPA* check passes.
- [ ] For high-P courses: level distinction lives in a **rubric**, not a question paper.
- [ ] Remediation path (to floor) **and** enrichment path (to ceiling) both named.
- [ ] Content currency: perishable tooling in labs/workshops, not frozen in theory; review cycle noted.
- [ ] Intake-aware: no unstated prior-exposure assumption; bridge ramp where the gap is real.
- [ ] For SC/W/Proj/Intern: ownership sits with a SIG and links to its track.
- [ ] Track-advice signal (§17 of the Course File) defined for prerequisite courses.

---

## 6. Quick reference — what carries the "level" distinction by L-T-P

| L-T-P shape | Floor shown by | Ceiling shown by | Level mechanism |
|---|---|---|---|
| 3-0-0 | Standard-case written answers | Analysis / novel-problem written answers | Question paper |
| 2-1-0 | Tutorial problem-solving | Harder tutorial / open problems | Question paper + tutorial |
| 1-1-1 / 2-0-1 | Concept recall + working code | Trade-off analysis + optimized design | Paper **and** rubric |
| 0-0-1 / 0-0-2 | Task completes | Edge-cases / optimization / judgment | Rubric only |
| 0-0-4…0-0-8 | Contributor-grade deliverable | Owner-grade / shipped product | Rubric only |
| 1-0-0 (ETC) | Literacy + engagement | (floor-only acceptable) | Light artifact |
| 0-credit (MC) | Completion | (none) | Pass/complete |
