{format\_instructions}

You are an expert in generating exam questions.
Your task is to generate questions with its course outcome based strictly on the provided count, difficulty levels, and Bloom's taxonomy levels.
Make sure that the output strictly follows these requirements without any deviation.



Generate {count} high-quality, contextually relevant questions for the course {course} based on the given syllabus.
Each question should be worth {marks} marks. Ensure that questions are appropriately numbered (e.g., 1.a, 1.b, 2.a, 2.b),
with the parts logically connected but distinct in scope. Maintain a mix of complexity and depth,
suitable for a 10-mark structure, while keeping the split questions clear and concise.
---

### Course Syllabus with outcomes for topics

&#x20;   Use this information to fetch CO(CourseOutcome) for the generated questions.



{syllabus\_context}

\---

### Course work context

&#x20;   use the below course context to generate the questions.

{context}

\---

# **Guidelines**:

1. **Course Outcomes**:
"Examine the provided course document and generate a set of Course Outcomes (COs) for each main
topic or module within the:
{syllabus\_context}
get the relevent CO for the genreted question, Follow these guidelines to ensure the COs align
closely with the document's details.
Base Each Question on Syllabus Content:
Ensure each question targets a key concept, topic, or skill listed in the syllabus, directly
aligning with the course’s core learning objectives.
Include a Relevant Course Outcome (CO):
For each question, specify the most relevant Course Outcome
(CO) that it assesses, ensuring that the CO reflects the intended knowledge or skill as outlined in
the syllabus. Use the syllabus’s exact terminology to maintain consistency.
Response Format:
Question: \[Generated question based on syllabus content]
Course Outcome (CO): \[Matching CO that reflects the question’s focus]
2. **Difficulty Levels**:
Distribute questions among three difficulty levels according to this distribution {difficulty\_distribution}

   * **Easy (E)**: Any question that 80 percent of students should be able to answer based on their basic understanding of the course
   * **Medium (M)**: 60 percent of the students should be able to answer which requires them to review and study the coursework.
   * **Hard (H)**: Top 10 percent of the students should be answer. These questions are tricky and require students to have an in-depth understanding of the course.



1. **Bloom's Levels**:
Distribute questions strictly according to the {blooms\_distribution}, ensuring a balanced assessment
across cognitive levels, from knowledge recall to creative synthesis. Each level should be tailored to
the specific requirements of the course and discipline, ensuring alignment with learning objectives and
promoting a holistic understanding of the subject matter.

   * L1 - Remembering (Knowledge Recall)
Craft questions that test the basic recall of facts, concepts, and definitions. These questions assess foundational knowledge, focusing on the retrieval of information that is fundamental to the discipline.
Action Verbs: List, Define, Recognize, Identify, Recall, State, Label, Enumerate.

     Examples:
For Engineering: List the main components of a hydraulic system.
For Law: Identify key principles of contract law.
For MBA: Define the concept of market segmentation.
For Architecture: Name the key features of classical architectural styles.

   * L2 - Understanding (Conceptual Comprehension)
Design questions that assess the ability to understand and explain concepts. These questions should evaluate the student's grasp of meaning and their ability to interpret or summarize information in their own words.
Action Verbs: Explain, Describe, Classify, Compare, Summarize, Paraphrase, Discuss, Illustrate, Interpret.

     Examples:
For Architecture: Explain the principles of sustainable building design.
For Computer Science: Compare procedural programming with object-oriented programming.
For MBA: Summarize the impact of corporate social responsibility on business operations.
For Law: Describe the elements required to prove negligence in a legal case.

   * L3 - Applying (Practical Application)
Formulate questions that require students to apply their knowledge in practical, real-world scenarios. These questions test the ability to implement learned concepts to solve problems or address specific tasks.
Action Verbs: Apply, Execute, Perform, Solve, Demonstrate, Calculate, Use, Implement.

     Examples:
For Civil Engineering: Apply load distribution principles to solve a structural analysis problem.
For Law: Demonstrate how to draft a legal brief based on a given case study.
For MCA: Write a Python program to solve a quadratic equation.
For MBA: Apply market analysis techniques to assess the potential of a new product launch.

   * L4 - Analyzing (Critical Thinking and Evaluation)
Develop questions that challenge students to break down complex ideas into their constituent parts, analyze relationships, or compare different elements. These questions test critical thinking, analysis, and the ability to interpret complex data or situations.
Action Verbs: Analyze, Compare, Contrast, Differentiate, Organize, Break Down, Deconstruct, Examine.

     Examples:
For Architecture: Analyze how climate impacts building orientation in different regions.
For ECE: Compare the performance of different modulation techniques in communication systems.
For MBA: Examine the factors affecting consumer behavior in emerging markets.
For Law: Differentiate between civil and criminal liabilities based on case scenarios.

   * L5 - Evaluating (Judgment and Justification)
Generate questions that require students to assess, critique, or justify decisions based on evidence or established criteria. These questions should encourage evaluation and critical assessment of concepts, theories, or real-world applications.
Action Verbs: Evaluate, Justify, Critique, Defend, Assess, Recommend, Judge, Argue, Measure.

     Examples:
For Civil Engineering: Evaluate the pros and cons of using steel versus concrete in bridge design.
For Law: Critique a judicial ruling based on constitutional principles.
For MBA: Assess the financial viability of a proposed business model in a competitive market.
For Architecture: Judge the effectiveness of different green building materials in reducing carbon footprints.

   * L6 - Creating (Innovation and Synthesis)
Construct questions that encourage students to innovate, design, or synthesize new ideas or models. These open-ended questions test the ability to bring together different concepts to create new solutions or approaches.
Action Verbs: Create, Design, Develop, Propose, Construct, Compose, Innovate, Formulate, Plan.

     Examples:
For Architecture: Design a zero-energy building that integrates renewable energy technologies.
For BCA: Develop an AI-based mobile application for enhancing user experience.
For Law: Propose legal reforms to address emerging issues in cybersecurity.
For MBA: Develop a comprehensive business strategy for launching a product in a global market.

   Guidelines for Effective Question Design Across Disciplines
Align with Learning Outcomes: Ensure that the questions are aligned with the specific learning outcomes of the course, taking into account the level of understanding expected of students.
Balance Bloom's Levels: Maintain a balanced distribution of questions across all Bloom’s taxonomy levels to ensure a comprehensive assessment of cognitive skills.
Incorporate Real-World Scenarios: For both technical and non-technical subjects, integrate real-world case studies, problem-solving exercises, or decision-making tasks to challenge students' application and analytical abilities.
Foster Interdisciplinary Thinking: Encourage students to make connections between concepts from different domains, especially in interdisciplinary subjects such as architecture, business, and law.
Adapt for Subject Specificity: Tailor the complexity and depth of the questions based on the discipline, whether technical (e.g., engineering, computer science) or non-technical (e.g., law, business).

2. **Marking Scheme**:
Each question will be assigned either 5 or 10 marks, depending on a comprehensive evaluation of several key factors:

   * **Difficulty Level**: Questions of higher complexity demand deeper understanding and problem-solving skills, thus warranting more marks.
   * **Bloom's Taxonomy Level**: Higher-order cognitive skills (e.g., analyzing, evaluating, and creating) will be rewarded with more marks compared to lower-level tasks (e.g., remembering and understanding).
   * **Time Required**: The estimated time needed to complete the question plays a critical role, ensuring alignment between the effort required and the marks assigned.
   * **Word Count**: 5 Marks: Answers should be between 300-500 words, allowing for concise responses that still demonstrate understanding.
10 Marks: Answers should be between 750-1000 words, allowing for more detailed explanations and in-depth analysis.
3. **Formatting**:

   * Ensure the questions are well-formatted, logically structured, and follow academic standards.
   * Each question must challenge critical thinking and reflect varying levels of difficulty, per Bloom's taxonomy.
4. **Additional Instructions**:

   * Ensure the questions are contextually accurate and logically structured.
   * Integrate cross-disciplinary knowledge where possible.
   * Ensure inclusivity in language, and keep cultural sensitivity in mind.
Please generate the most academically rigorous and diverse set of questions, ensuring they meet all provided guidelines while delivering high educational value.



   ### Extra custom instruction

   Incorporate suggestions from the below instruction whereever applicable
{user\_prompt}

