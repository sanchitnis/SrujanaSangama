# Skill: Patent Generator (Indian Patents)

## Purpose
Extracts invention details from a Markdown document, guides brainstorming for novelty, checks for patentability, and generates a draft Indian patent application. No JS or API calls; all logic is agent-driven and human-in-the-loop.

## Workflow
1. **Input**: Accept a Markdown (.md) file containing the invention writeup.
2. **Extraction**: Parse the Markdown to extract:
   - Title
   - Abstract
   - Problem statement
   - Objectives
   - Technical field
   - Background
   - Key features
   - Advantages
   - Experimental data/results
   - Drawings (if described)
3. **Patentability Check**: Prompt the user to:
   - Confirm novelty, inventive step, and industrial applicability
   - Identify missing or weak sections
4. **Prior Art Brainstorm**: Query the Google Patents database via agent web searches based on extracted keywords, present closest prior art matches and overlaps, and guide the user through brainstorming pivots/modifications to improve novelty.
5. **Scoring**: Ask the user to rate (out of 10) the likelihood of patent grant and publication, based on novelty and completeness.
6. **Draft Generation**: Generate a Markdown template for the user to fill in missing details:
   - Detailed description
   - Claims (independent/dependent)
   - Drawings/diagrams (descriptions)
   - Applicant/inventor details
7. **Patent Application Draft**: Assemble all sections into a draft Indian patent application in Markdown format.
8. **Export**: Instruct the user on how to convert the Markdown to DOCX/PDF for filing.

## Notes
- All steps are interactive and agent-guided.
- Queries to Google Patents database are performed using agent web search capabilities.
- Designed for human-in-the-loop patent coaching and drafting.


---

**Author:** AI Innovation Coach
**Version:** 0.1.0
**License:** MIT
