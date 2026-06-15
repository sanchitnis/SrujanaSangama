# Programme Extension: B.Tech CSE / ISE / IT / AIML / AIDS / IoT / Cyber Security
## Course Design Rules, CSCore Mapping & SIG Track Definitions

> **Who this is for.** Faculty and SIG teams designing or revising any course in the 2026 B.Tech scheme for CSE, ISE, IT, AIML, AIDS, IoT, or Cyber Security programmes.
>
> **How to use this document.** This extension *adds to* the universal rules in `Course_Designer_Guidelines_Universal.md`. Read the universal guidelines first, then apply the CS-school-specific rules here. Where this document is silent, the universal rules apply.

---

## 1. Programme Core Competencies (CS School)

*(The "Programme Core competencies" referenced in universal §1 Rule 3 and §4 — the awareness floor for all CS school HC courses)*

These are the competencies every CS school graduate must demonstrate at the awareness level. They map to CSCore entrance-test topics, placement competencies, and foundational skills assumed by downstream courses.

| Competency Area | Description | Bloom's Floor Level |
|---|---|---|
| **Data Structures & Algorithms** | Standard data structures; time/space complexity analysis; pattern recognition | Apply (L3) |
| **Programming Fundamentals** | Readable, correct code in at least one language; debugging; modular design | Apply (L3) |
| **Database Concepts** | Relational model; SQL; normalisation; transaction basics | Apply (L3) |
| **Operating Systems Concepts** | Process management, memory, file systems, concurrency basics | Understand/Apply (L2–L3) |
| **Computer Networks** | OSI/TCP-IP model; protocols; addressing; security basics | Understand/Apply (L2–L3) |
| **Mathematics for CS** | Discrete maths, probability, linear algebra, calculus — as required per course | Varies |
| **System Design Thinking** | Ability to decompose a problem and propose a system architecture | Analyse (L4) |
| **Professional Readiness** | Aptitude test performance; communication; code review readiness | Apply (L3) |

---

## 2. CSCore Placement Spine

Every HC theory course (§4.2 in universal guidelines) must explicitly map its awareness floor to the CSCore placement topics it is responsible for. The AEC courses (Ability Enhancement, §4.10) form the dedicated placement readiness spine:

| Semester | AEC Focus | CSCore Competency Targeted |
|---|---|---|
| Sem 3 | Aptitude: Quantitative | Numerical reasoning, speed-accuracy |
| Sem 4 | Aptitude: Logical + Verbal | Pattern recognition, communication |
| Sem 5 | Core CS: DSA problems | Coding interviews, algorithm challenges |
| Sem 6 | Core CS: System Design + SQL | Design interviews, database rounds |

Track readiness per student at each AEC checkpoint and feed weak signals to academic mentors.

---

## 3. SIG Specialisation Tracks

*(The "School Specialisation Tracks" referenced in universal §4.6)*

CS School students choose a SIG (Specialisation Interest Group) track from Semester 5. The track shapes their SC/PEC electives, workshops, capstone brief, and internship placement. Each SIG is a faculty community of practice owning its curriculum end-to-end.

| SIG Track | Core Focus | Typical Recruiter Verticals |
|---|---|---|
| **Agentic AI / Enterprise Engineering** | LLMs, agentic systems, enterprise software architecture, AI integration | Product companies, BFSI, enterprise SaaS |
| **AI-ML / Data Engineering** | Machine learning, deep learning, MLOps, data pipelines | Analytics firms, research labs, data-intensive industries |
| **IoT / Embedded / Automation** | Embedded systems, edge computing, industrial automation, robotics | Manufacturing, automotive, energy |
| **Cybersecurity Services** | Offensive/defensive security, cloud security, compliance, forensics | IT services, BFSI, government |

**Track advice signal** (from universal §17 of Course File): Prerequisite course performance feeds academic mentor advice on track selection from Sem 3 onward. A student excelling in analysis/optimization problems in DSA is a strong candidate for AI-ML track; strong systems thinking → IoT or Cybersecurity.

---

## 4. Differentiated Learning Model — CS School Decision

*(Resolves open question from `CourseDesignWorkflow.md`)*

The CS School uses **Option C: same COs, differentiation by activities and assessment**.

- All students target the same COs.
- Awareness-level students demonstrate COs at Apply (L3).
- Advanced students demonstrate the same COs at Analyse/Evaluate/Create (L4–L6).
- Differentiation is achieved through the assessment instrument (question difficulty tiers, rubric ceiling definitions) — **not** through separate course sections or separate CO sets.
- Exception: Elective courses (SC/PEC) may have one additional "Advanced Capstone CO" visible only in the SIG track context — but the core CO set remains the same.

---

## 5. Reference Exemplar (CS School)

*(The "school reference exemplar" required by universal §0.2)*

The CS School reference exemplar for 2026 is the **Data Structures & Algorithms (1-1-1)** course:
- Awareness floor scope: defined per unit (recall + standard procedure application)
- Advanced ceiling scope: trade-off analysis + novel problem design
- Mark ratio: 70/30 (awareness/advanced)
- CGPA calibration: awareness-only → below 8 CGPA confirmed against REVA grade scale

All other CS school HC courses must produce a dual-level scope table (§3 of Course File) consistent with this calibration.

---

## 6. Workshop Offering Guidance (CS School)

*(Adds specificity to universal §4.5 for CS school context)*

Workshops (W1–W8 slots) are SIG-owned and just-in-time. For 2026, priority areas to keep fresh:
- Generative AI tooling and prompt engineering (update every semester)
- Cloud platforms and deployment (AWS/GCP/Azure — update per certification path changes)
- DevOps / MLOps pipelines
- Competitive programming (ICPC, Codeforces, LeetCode patterns)
- Cybersecurity practicals (CTF, pen-testing tools)

**Currency check**: before each semester, SIG lead must verify workshop content against current job postings for the relevant track. If tooling has shifted, re-author.

---

## 7. CS School Portfolio Artefact Examples

*(Adds specificity to universal Rule 11 for CS school context)*

| Course Type | Acceptable Portfolio Artefact |
|---|---|
| HC theory (3-0-0) | Documented solution with commentary; technical analysis report; research synthesis |
| HC integrated (1-1-1) | Working code repository with README; implemented algorithm with benchmarks; open-source contribution |
| SC/PEC Elective | Domain-specific project: ML model with evaluation report; security audit report; IoT prototype + documentation |
| Capstone | Shipped product / published paper / open-source release / deployed system |

---

## 8. Enterprise Skills — CS School Integration Examples

*(Adds CS-specific activity examples to universal §7)*

| Enterprise Skill | CS-Specific Activity |
|---|---|
| **Creativity & Value Creation** | Propose a novel application of a known algorithm to an unaddressed problem |
| **Initiative** | Identify a bug in an open-source project and submit a fix without prompting |
| **Collaboration** | Pair programming with peer review; team sprint with documented role contributions |
| **Ethical Reasoning** | Case study: *"An algorithm you built is producing biased outputs. Who is responsible? What do you do?"* |
| **Communication** | Technical blog post explaining a system design decision to a junior developer audience |
| **Adaptability** | *"Client requirements changed after Sprint 2. Refactor your design and explain the trade-offs."* |

---

## 9. IKS / Sustainability — CS School Integration Examples

*(Adds CS-specific examples to universal §8)*

| Thread | CS-Specific Integration |
|---|---|
| **IKS** | Vedic mathematics approaches to number theory; Aryabhata's positional notation in binary systems history; Indian contributions to cryptography and logic |
| **Sustainability** | Green computing (energy-efficient algorithms); data centre carbon footprint; e-waste considerations in IoT hardware design |
| **Liberal Studies** | Ethics of algorithmic decision-making; digital divide and accessibility; privacy and surveillance case studies |

---

*Extension Version*: 1.0 | *Released*: June 2026  
*Part of*: REVA University Course Design Guidelines — University Edition  
*Maintained by*: REVA School of CS Teaching-Learning Team  
*Lead Architect*: Sanjay Chitnis  
*Companion documents*: `Course_Designer_Guidelines_Universal.md` | `Course_File_Template_Universal.md`  
*Next Review*: June 2027
