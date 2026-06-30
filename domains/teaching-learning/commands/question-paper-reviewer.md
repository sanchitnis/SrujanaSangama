\---

name: reva-question-paper-reviewer
description: >
Review question papers and evaluation schemes for REVA University exams before administration.
Use this skill whenever faculty members or exam center staff need to validate, audit, or improve
question papers and their associated evaluation schemes (model answers, rubrics, marking schemes).
Trigger on phrases like "review this question paper", "check my exam", "audit this evaluation
scheme", "validate my exam design", "give feedback on this question paper", "is this exam OK",
or "check this rubric". Supports multiple exam types (theory, practical, design, programming)
and mixed file formats (DOCX, PDF, Markdown). Input should include the question paper and its
evaluation scheme. Produces a prioritized feedback report (P1/P2/P3 issues) covering question
clarity, rubric fairness, Bloom's alignment to COs, difficulty/marks distribution, grading
consistency, and BTech CS-specific issues. Always trigger for any exam quality review request,
even partial ones.
compatibility: "Requires bash tool for temporary file handling. Supports DOCX, PDF, Markdown file uploads."
---

# REVA Question Paper \& Evaluation Scheme Reviewer

Reviews question papers and evaluation schemes for REVA University exams **before administration**, ensuring clarity, fairness, technical soundness, and pedagogical alignment. Produces a structured, prioritized feedback report to guide faculty improvements.

This skill focuses on **exam design quality from the assessment perspective** — complementary to reva-course-reviewer which validates the upstream course design (COs, modules, content). This skill is the quality gate BEFORE exams go live.

\---

## Step 0 — Load Context \& Parse Input

### Input Handling

Accept the following file formats:

* **DOCX**: Word documents with embedded question papers and evaluation schemes
* **PDF**: Separate or combined documents containing questions and marking schemes
* **Markdown**: Question paper + rubric as structured Markdown text

If the user uploads mixed formats or pastes content directly, consolidate them logically.

### Extract These Sections

|Section|What to identify|
|-|-|
|**Exam Metadata**|Course name/code, semester, exam type (theory/practical/design/programming), total marks, time allowed|
|**Question Paper**|All questions with marks allocation, question types (MCQ/SAQ/LAQ/coding/design), difficulty indicators|
|**Evaluation Scheme**|Model answers, rubrics, marking guidelines, CO alignment claims, total marks breakdown|
|**Assessment Context**|Which COs does this exam assess? Any stated prerequisites or assumptions?|

If any section is missing, note it as a gap — do not ask the user to fill it in. Proceed with what's available.

\---

## Step 1 — Establish Evaluation Criteria

Before reviewing, confirm the **exam type** and **assessment context**. Tailor feedback based on:

|Exam Type|Key Focus Areas|
|-|-|
|**Theory (T)**|Question clarity, conceptual depth, Bloom's progression, model answer completeness, consistency of grading rubrics|
|**Practical (P)**|Code/output evaluation clarity, edge case coverage in rubrics, fairness across different solution approaches, partial credit schemes|
|**Design/Case Study**|Rubric comprehensiveness, subjective criteria clarity, rubric consistency with CO levels, fairness across diverse approaches|
|**Programming**|Output specification clarity, edge case definition, rubric fairness to different algorithms, plagiarism detection assumptions|

\---

## Step 2 — Review Across Six Dimensions

Work through each dimension systematically. For each finding, assign:

* 🟢 **Strong** — excellent execution
* 🟡 **Adequate** — acceptable but improvable
* 🔴 **Weak** — significant issue requiring attention

Record evidence (direct quotes or paraphrases) for each rating.

### Dimension A: Question Clarity \& Technical Correctness

**What to assess:**

* Is each question **unambiguous** — would all students interpret it the same way?
* Are **technical terms used correctly** — no misspellings, incorrect definitions, or terminology mismatches?
* Does each question **clearly state the expected format** of the answer (e.g., "provide a working C program", "write 200 words max", "draw a diagram")?
* Are there **implicit assumptions** not stated (e.g., "assume the function is always called with valid input")?
* For programming/practical questions: are **input/output specifications crystal clear**?
* Are **marks proportional to question difficulty and length?**

**Red flags to catch:**

* Vague phrasing ("Briefly discuss...", "Explain..." without context boundaries)
* Typos or grammatical errors that could confuse meaning
* Inconsistent terminology across questions
* Missing edge case specifications (e.g., "What if n=0?")
* Questions requiring knowledge not covered in course modules
* Trick questions or ambiguous wording that penalizes thoughtful interpretations

**For theory exams specifically:**

* Check whether each question **targets a specific CO** (is this mapping explicit in the paper?)
* Do questions **progress in difficulty** — easier at start, harder at end?
* Are there **equal coverage of all major topics** or are some overweighted?

**For practical/programming exams:**

* Is the **test case specification complete** (normal cases, edge cases, error handling)?
* Are **input constraints stated** (e.g., "1 ≤ n ≤ 10^5")?
* Is the **expected output format explicit** (e.g., "output must be a single integer on one line")?
* Are there **ambiguous algorithm choices** (e.g., "sort the array" — ascending or descending?)?

\---

### Dimension B: Rubric Fairness \& Clarity

**What to assess:**

* Is the **marking scheme complete** — every question has a clear rubric?
* Are **rubric criteria explicit** — not subjective phrases like "good understanding"?
* Is **partial credit clearly defined** — when does a student get 50% vs. 75% vs. 100% of marks?
* For rubrics with multiple criteria: are they **mutually exclusive and collectively exhaustive**?
* Is the **rubric proportional to question difficulty?** (A 2-mark question shouldn't have an elaborate 10-level rubric.)
* For subjective questions (design, essays): are there **objective anchors** for grading (e.g., "Full marks: solution handles all 3 constraints + explains trade-off; Half marks: handles 2 constraints, no trade-off discussion")?

**Red flags:**

* Rubrics that say "at teacher's discretion" without further guidance
* Inconsistent point distributions (e.g., some 2-mark questions have 5 levels of partial credit, others have 0)
* Rubrics that favour specific solution approaches over correct alternatives
* Model answers that don't align with the rubric structure
* Missing rubrics for any question
* Overly lenient rubrics that don't differentiate between weak and strong answers

**For programming/practical exams:**

* Are there **clear deductions for common mistakes** (off-by-one errors, wrong output format, missing edge cases)?
* Does the rubric **accept alternative correct solutions** (different algorithms, different data structures)?
* Is **code style/documentation weighted appropriately** (if at all)?

**For theory exams:**

* Do model answers **match the Bloom's level of the question?** (A Bloom's 5 "Analyse" question shouldn't have a Bloom's 2 "Recall" model answer.)
* Are **alternative correct answers acknowledged** in the rubric?

\---

### Dimension C: Bloom's Taxonomy Alignment to COs

**What to assess:**

* **Does this exam collectively assess all stated COs?** (Is there a CO coverage heatmap or gap?)
* For each question: **what Bloom's level does it target?** (Remember: Bloom's 1=Recall, 2=Understand, 3=Apply, 4=Analyse, 5=Evaluate, 6=Create)
* Does the **question verb match the Bloom's level?**

  * "Define" = Bloom's 1-2 (Recall/Understand)
  * "Solve" / "Implement" = Bloom's 3 (Apply)
  * "Analyze" / "Compare" = Bloom's 4 (Analyse)
  * "Evaluate" / "Justify" = Bloom's 5 (Evaluate)
  * "Design" / "Create" = Bloom's 6 (Create)
* **Is the Bloom's progression appropriate for the semester level?**

  * Semester 1-2: Mostly Bloom's 1-3 (Recall → Apply)
  * Semester 3-4: Bloom's 3-5 (Apply → Evaluate)
  * Semester 5-8: Bloom's 4-6 (Analyse → Create)
* **Do the questions actually engage students at the stated Bloom's level**, or does the rubric only test recall?

  * Example red flag: A question states "Analyse the algorithm" (Bloom's 4) but the rubric only asks students to trace execution and list steps (Bloom's 2-3).

**BTech CS-specific checks:**

* For programming questions: is the CO **"Implement" (Bloom's 3)** or **"Analyse" (Bloom's 4)**? A question asking students to write code is Bloom's 3; a question asking them to compare two algorithms is Bloom's 4.
* For theory questions: are CS concepts assessed at the **right level of abstraction**? (e.g., compiler design should ask students to "Design" or "Analyse", not just "Define".)

\---

### Dimension D: Difficulty \& Marks Distribution

**What to assess:**

* Does the **difficulty level of the exam match the course level** (Semester 1 exam should be more basic than Semester 8 exam)?
* Are **questions roughly evenly distributed by difficulty?** (Avoid a paper where 80% of questions are easy and 20% are hard, or vice versa.)
* **Is marks allocation proportional to question difficulty and time to solve?**

  * Example: A 2-mark question should take \~4-5 minutes; a 10-mark question should take \~20-25 minutes.
* **Is the total time allocation realistic?** (If the exam is 3 hours = 180 minutes, and you've allocated 50 minutes for questions worth only 30 marks, that's unbalanced.)
* For mixed exam types (theory + practical): **is the balance appropriate?** (e.g., should a "Algorithms" course be 50% theory, 50% practical? Or 30% theory, 70% practical?)

**Red flags:**

* All easy questions (marks bunching at the bottom)
* All hard questions (students can't finish)
* Marks/time mismatch (e.g., a 5-mark question that requires 20 minutes to code)
* Misalignment with course level expectations
* Time allocation that doesn't match marks (e.g., 10 marks in 15 minutes with tricky questions)

**For practical exams specifically:**

* Does the difficulty **progress logically** across problems/test cases?
* Is there a **mix of straightforward and tricky edge cases** or are all cases equally hard/easy?

\---

### Dimension E: Consistency of Grading Standards

**What to assess:**

* **Are rubrics consistent across similar questions?**

  * Example: If two questions both ask students to "Implement an algorithm," do they have equivalent rubric detail and partial credit structure?
* **Do all rubrics use the same grading philosophy?**

  * Red flag: Question 1 uses absolute criteria ("handles all 5 edge cases = full marks"), Question 2 uses relative criteria ("similar to model answer = full marks"). Inconsistent philosophies.
* **Is the language in rubrics consistent?**

  * Red flag: Q1 rubric uses "demonstrates understanding of X"; Q2 uses "shows competence in Y"; Q3 uses "correctly implements Z" — these aren't parallel.
* **Are deductions applied consistently across questions?**

  * Red flag: Off-by-one error deducts 1 mark in Q1 but 2 marks in Q5.
* **Is the grading philosophy aligned with the exam's stated purpose?**

  * E.g., if this is a diagnostic exam, the rubric should give detailed partial credit to identify learning gaps. If it's a summative exam, rubrics can be more binary.

\---

### Dimension F: BTech CS-Specific Issues

This dimension flags issues unique to computer science exams at BTech level.

**For programming/coding questions:**

* **Language specification**: Is the programming language explicitly stated? ("Write in C" vs. "Write in Python"?)
* **Compiler/environment**: Are there compiler flag assumptions (e.g., "using g++ -std=c++17")?
* **Plagiarism risk**: Is this question similar to textbook examples or online problems? (High similarity can make plagiarism detection harder.)
* **Algorithm fairness**: Does the rubric accept multiple correct algorithms or favour one approach?

**For theory/data structures/algorithms:**

* **Notation clarity**: Is mathematical notation consistent (e.g., don't use both O(n) and T(n) for time complexity without clarification)?
* **Concept prerequisite**: Does the question assume knowledge from earlier courses? (If yes, is this documented?)
* **Practical relevance**: Does the question feel detached from real applications or is it grounded? (Nice-to-have, not critical.)

**For systems/databases/networking exams:**

* **Real-world context**: Are questions tied to actual systems or are they overly abstract?
* **Edge case completeness**: For system design questions, are fault tolerance and scalability edge cases covered?

**For security-related exams:**

* **Ethical tone**: Do questions avoid promoting insecure practices? (e.g., "Implement a weak encryption" should be framed as "Explain why this is weak" not "Design this".)

\---

## Step 3 — Generate Prioritized Feedback Report

Consolidate findings into a structured report with the following sections:

### Report Header

* Exam metadata (course, semester, exam type, total marks, time)
* Date of review
* Reviewer note: "This is an AI-assisted review of exam design quality. It supplements, but does not replace, expert human review."

### Section 1: Executive Summary

* **Overall Assessment**: In 2–3 sentences, state the exam's current state. Example: "The exam is well-structured overall with clear questions and fair rubrics. A few improvements recommended (below) would strengthen clarity and reduce grading ambiguity."
* **Key Strengths**: 2–3 bullet points of what the exam does well.
* **Main Areas for Improvement**: 2–3 bullet points of highest-priority issues.

### Section 2: Findings by Dimension

For each of the six dimensions (A–F), present findings as:

**\[Dimension Name]**

* **Status**: 🟢 Strong | 🟡 Adequate | 🔴 Weak (overall)
* **Key Findings**: 2–4 concrete observations with evidence
* **Impact**: Why this matters (e.g., "Affects fairness of grading", "May confuse students")

### Section 3: Prioritized Recommendations

**P1 — Critical (Must fix before exam)**

* List all P1 issues in order of impact/effort to fix.
* Each P1 issue includes:

  * What's the problem? (1 sentence)
  * Which dimension? (A–F)
  * Suggested fix? (1–2 sentences)
  * Example if helpful

**P2 — Important (Should fix if time allows)**

* Medium-priority improvements that enhance clarity/fairness but aren't blockers.
* Same format as P1.

**P3 — Nice-to-Have (Consider for next iteration)**

* Low-priority polish (e.g., minor wording improvements, consistency tweaks).
* Same format as P1/P2.

### Section 4: CO Coverage Heatmap (if applicable)

If the exam includes CO-to-question mapping, produce a simple table:

|CO|Q1|Q2|Q3|Q4|...|Coverage|
|-|-|-|-|-|-|-|
|CO1|✓||✓||...|2 questions|
|CO2||✓||✓|...|2 questions|
|...|||||...|...|

Highlight any CO with zero coverage (gap) or excessive coverage (overemphasis).

### Section 5: Rubric Quality Snapshot

Provide a quick table showing rubric completeness:

|Question|Marks|Rubric Completeness|Partial Credit Clarity|Notes|
|-|-|-|-|-|
|Q1|5|Complete|Clear (3 levels)|—|
|Q2|10|Partial (missing edge cases)|Unclear|See P1.1|
|...|...|...|...|...|

### Section 6: Additional Context (if provided)

* If the user provided course design docs, course COs, or curriculum context, briefly note alignment/misalignment.
* If the user mentioned specific concerns or constraints, address them explicitly.

\---

## Step 4 — Tailor to Exam Type

Adjust report tone and emphasis based on exam type:

### Theory Exam

* Emphasize Bloom's alignment and CO coverage.
* Focus on model answer clarity and consistency.
* Include rubric analysis for subjective questions.

### Practical/Programming Exam

* Emphasize test case completeness, input/output clarity, and edge case coverage.
* Focus on rubric fairness across solution approaches.
* Flag implicit assumptions (e.g., "no negative inputs allowed").

### Design/Case Study Exam

* Emphasize rubric comprehensiveness and objective anchors.
* Check for bias toward specific solution approaches.
* Assess rubric clarity for subjective evaluation.

\---

## Step 5 — Provide Actionable Examples

For each P1/P2 issue, provide:

1. **Current state** (quote or paraphrase from paper/rubric)
2. **Revised version** (concrete rewrite)
3. **Why this helps** (1 sentence)

\---

## Output Format

**Primary output**: A well-structured Markdown or HTML report saved to `/home/claude/` with filename `\\\\\\\[Course-Code]\\\\\\\_exam\\\\\\\_review\\\\\\\_\\\\\\\[Date].md` (or `.html` if preferred for readability).

**Optional secondary output**: If the user prefers, package recommendations as a DOCX document (REVA-branded) using `reva-branding` guidelines.

\---

## Appendix A: BTech CS Exam Checklist (Reference)

This checklist can evolve based on feedback from faculty and exam center staff. Items are organized by dimension.

### Dimension A: Question Clarity

* \[ ] All questions are unambiguous — no terms that could be interpreted two ways
* \[ ] Technical terms are used correctly — no misspellings or incorrect definitions
* \[ ] Each question explicitly states expected answer format (e.g., "provide a C program", "write 100 words max", "draw a diagram with labels")
* \[ ] No implicit assumptions — all constraints are stated (e.g., "assume n ≥ 1", "assume no negative inputs")
* \[ ] For programming Qs: Input/output specifications are complete and unambiguous
* \[ ] For all Qs: Marks are proportional to difficulty and time to solve
* \[ ] No questions that require knowledge outside course scope

### Dimension B: Rubric Fairness

* \[ ] Every question has an explicit rubric (no "at teacher's discretion")
* \[ ] Rubric criteria are objective, not subjective ("lists all 3 trade-offs" not "shows understanding")
* \[ ] Partial credit is clearly defined (e.g., when is it 50%? 75%? 100%?)
* \[ ] Rubric structure is consistent across similar questions
* \[ ] Model answer aligns with rubric structure
* \[ ] Rubric proportionality: simple questions have simple rubrics; complex questions have detailed rubrics

### Dimension C: Bloom's Alignment

* \[ ] Exam collectively assesses all stated COs (no gaps or orphan Qs)
* \[ ] Each question's Bloom's level is identified
* \[ ] Question verbs match Bloom's levels (Recall uses "Define"; Apply uses "Solve"; Analyse uses "Compare", etc.)
* \[ ] Bloom's progression is appropriate for semester level
* \[ ] Rubric tests at the stated Bloom's level (not just recall for a Bloom's 4 question)

### Dimension D: Difficulty \& Marks

* \[ ] Exam difficulty matches course level
* \[ ] Questions are roughly evenly distributed by difficulty (not all easy or all hard)
* \[ ] Marks are proportional to difficulty and time (e.g., 2-mark Qs take \~5 min; 10-mark Qs take \~20 min)
* \[ ] Total time allocation is realistic (180 min exam ≠ 200+ minutes of questions)
* \[ ] Topic coverage is balanced (no excessive weighting of one unit)

### Dimension E: Grading Consistency

* \[ ] Similar questions have similar rubric detail and partial credit structure
* \[ ] Rubric language is consistent across all questions (parallel phrasing)
* \[ ] Deductions are applied consistently (same error type gets same deduction across all Qs)
* \[ ] Grading philosophy is aligned with exam purpose (diagnostic vs. summative)

### Dimension F: BTech CS-Specific

* \[ ] Programming language is explicitly stated (C, C++, Java, Python, etc.)
* \[ ] For code Qs: Compiler/environment assumptions are stated (gcc, g++, Python 3.x, etc.)
* \[ ] For code Qs: Rubric accepts multiple correct algorithms/approaches (not biased to one solution)
* \[ ] Mathematical notation is consistent and clear
* \[ ] Question relevance: concepts are tied to real applications (where appropriate)
* \[ ] For security/ethics topics: questions promote secure/ethical practices

\---

## How to Use This Skill

**As an exam center administrator or course faculty:**

1. **Prepare materials**: Gather the question paper and evaluation scheme (DOCX, PDF, or Markdown).
2. **Provide context** (optional): Share course code, course COs, or exam purpose if available.
3. **Request review**: "Review my exam" / "Check this question paper" / "Audit this rubric" / etc.
4. **Receive feedback**: Get a prioritized report (P1/P2/P3) with actionable recommendations.
5. **Iterate**: Update the paper/rubric based on P1 suggestions, then request a quick re-review if desired.

\---

