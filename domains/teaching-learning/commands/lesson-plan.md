# Command: /lesson-plan

**Description:** Creates an interactive, highly engaging lesson plan based on the "Five Magic Questions" framework. Typically used by Faculty Members and Course Teachers.

---

## 🤝 Human-AI Collaboration Boundary

* **What the Agent Drafts:** A detailed lesson timeline divided by activity segments, specific provocation hooks, peer-collaboration challenges, and real-world mastery evaluations.
* **What the Human Must Review & Approve:** The academic accuracy of the concepts, duration allocation based on actual class pacing, select active learning strategies, and feasibility of real-world mastery tasks within local guidelines.

---

## 🛠️ Step-by-Step Lesson Planner Workflow

When a user requests `/lesson-plan` for a specific topic, target audience, and duration, the agent must execute the following sequential steps:

### Step 1 — Intake & Context Parsing
Parse the input constraints and target details:
* **Target Audience/Stakeholder:** (e.g., 8th Grade BTech CSE, 3rd Year Chemistry)
* **Core Topic:** (e.g., Data Analysis & Graphs, Chromatography)
* **Time Duration:** (e.g., 40 minutes, 1 hour, 2 hours)

### Step 2 — Core Matrix Mapping
Map out the conceptual foundations of the **Five Magic Questions** framework:
1. **PURPOSE (The "Why" for the Learner):** Define the intrinsic value of the topic for the learner. Why should they care? What immediate or long-term problem does this solve for them?
2. **INTEGRATION (Self / Others / India):** Connect the learning material to the learner's personal identity, their community, or broader national/global contexts (e.g., historical achievements, civic relevance, Indian contributions, or structural realities).
3. **METHODS (Fun, Fast, & Effective):** Design an inductive hook or a "provocation corner." Use storytelling, sensory puzzles, or cognitive dissonance to spike curiosity and avoid passive lecturing.
4. **PARTNERSHIP (Collaborative Learning):** Design structured peer-to-peer interactions, debates, or team challenges where participants actively teach and learn from each other. Keep direct lecture time low.
5. **MASTERY (Real-World Application):** Define exactly how learners will visibly demonstrate, apply, or practice this skill within and outside the learning space.

### Step 3 — Scripting the Learning Timeline
Construct a structured timeline for the session, explicitly tagging which of the 5 Magic Questions is being activated during each block:
* **`[Methods]`** and **`[Purpose]`** during hook activities.
* **`[Integration]`** during contextual segments.
* **`[Partnership]`** during peer learning activities.
* **`[Mastery]`** during application/practice checks.

### Step 4 — Blindspot Diagnostic Checklist
Conclude the lesson plan with a quality audit check block:
* **Teacher Talk Time:** Verify that direct lecture time is limited to under 30% of the session.
* **Collaboration Check:** Ensure peer partnership is active.
* **Application Integrity:** Confirm that the mastery check evaluates functional understanding rather than rote memorization.

---

## 📂 Output Target

The generated lesson plan should be written to:
`srujana-memory/my-memory/wiki/courses/[course-name]/lesson-plans/` or `srujana-memory/my-memory/wiki/courses/[course-name]/[topic].md`.
