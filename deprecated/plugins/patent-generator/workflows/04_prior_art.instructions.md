# Agent Skill Instructions: patent-prior-art

## Purpose
Guide the user through an active search of the Google Patents database using search capabilities, perform deep novelty analysis, and brainstorm concrete modifications to the user's idea to improve its patentability.

## Agent Actions
1. **Query Construction**:
   - Extract primary technical keywords, structural elements, and the target application field from the invention writeup.
   - Formulate target search strings. Example: `site:patents.google.com "autonomous irrigation" "soil moisture sensor"`.
2. **Google Patent Querying**:
   - Execute the web search queries targeting `patents.google.com` to find relevant published patent applications or granted patents.
   - Collect details of the closest 2-3 prior art matches (Patent ID, Title, publication year, key features).
3. **Overlap Mapping**:
   - Critically evaluate overlaps between the user's idea and the identified prior art.
   - Detail which features are structurally or procedurally identical, and which ones remain unique.
4. **Idea Modification Guidelines**:
   - Provide concrete suggestions for modifying the user's idea:
     - If core components overlap: Recommend adding specific steps, unique hardware combinations, or novel sensor placement.
     - If application overlaps: Advise on narrowing the claim to a specific, non-obvious context or environment.
     - Section 3 Exclusions (Indian Patent Act): If the idea is software-heavy, suggest adding a physical, tangible apparatus configuration to bypass Section 3(k) exclusions.
5. **Interactive Brainstorming**:
   - Discuss options with the user and log their decisions for the next workflow step (scoring).

## Output
- Populate the output using the template defined in `04_prior_art.md`.

