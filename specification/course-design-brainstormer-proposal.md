# Course Design Brainstormer Proposal

## Problem

The teaching-learning domain does not have a command to critically evaluate a course design document from an Outcome-Based Education (OBE) and pedagogy perspective, specifically focusing on REVA University's strategy to prepare students for AI Era careers, hands-on knowledge, inspiring students to learn, and acting in brainstorming mode to collaboratively improve course designs using the ADDIE instructional design process.

## Proposed Change

1. **New Command File**: Create `domains/teaching-learning/commands/course-design-brainstormer.md` to define the `/course-design-brainstormer` command.
2. **Pedagogical and AI-Era Focus**: The command instructions will prompt the agent to assume the persona of an AI Era educationalist and instructional design expert.
3. **Core Evaluation & Brainstorming Dimensions**: The command will define three evaluation dimensions:
   - **Dimension 1: Outcome-Based Education (OBE) Rigor**: Bloom's Level mapping, measurable COs, HOTS dominance ($\ge 60\%$).
   - **Dimension 2: Pedagogy & Student Motivation**: Active learning, experiential learning, and inspiring hooks/framing to motivate students to learn.
   - **Dimension 3: AI-Era Career Preparedness & Hands-on Knowledge**: AI co-working integration, AI-resistant/proof assessment strategies, hands-on application, and portfolio-first deliverables.
4. **ADDIE Process Workflow**: The command will guide the faculty member through a sequential ADDIE workflow where each phase takes inputs from the evaluation/outcomes of the previous phase:
   - **Analysis**: Diagnose the existing course design against learner needs, AI-era job demands, and prerequisite concepts.
   - **Design**: Develop/refine measurable Course Outcomes (COs) and target Bloom's levels, incorporating feedback from the Analysis phase.
   - **Development**: Structure units, specify learning materials, choose AI tools, and map portfolio requirements, building on the approved design.
   - **Implementation**: Formulate active learning facilitation steps, delivery plans, and student motivation strategies.
   - **Evaluation**: Define rubrics for CIA, end-semester exams, and continuous improvement loops based on student performance.
5. **Integrated Brainstorming Mode**: Across all phases of the ADDIE workflow, the brainstorming session integrates all three core evaluation dimensions (OBE, Pedagogy/Motivation, and AI-Era Strategy).
6. **Domain Router Update**: Modify `domains/teaching-learning/AGENTS.md` to include `/course-design-brainstormer` under the local commands.
7. **Status Update**: Update `IMPLEMENTATION-STATUS.md` to register the new command.

## Scope Boundaries

### In Scope
- Creating `domains/teaching-learning/commands/course-design-brainstormer.md`.
- Updating `domains/teaching-learning/AGENTS.md` to list the command.
- Updating `IMPLEMENTATION-STATUS.md` domain/command status.

### Out of Scope
- Modifying other existing commands or rule files in the `teaching-learning` domain.
- Creating or editing any files outside the `teaching-learning` domain and the root files (`IMPLEMENTATION-STATUS.md`, `specification/`).

## Verification

The change is complete and verified when:
1. `domains/teaching-learning/commands/course-design-brainstormer.md` exists and satisfies the command formatting rules of `CONSTITUTION.md` (has a one-line description, human-AI boundary statement, and specified output location).
2. The domain router `domains/teaching-learning/AGENTS.md` is updated.
3. `IMPLEMENTATION-STATUS.md` is updated.
