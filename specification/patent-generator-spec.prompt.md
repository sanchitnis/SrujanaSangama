# Specification: `patent-generator` Plugin

## 1. Goal Description
Detailed specification for the `patent-generator` plugin under the SrujanaSangama private marketplace, driving intellectual property claim extraction and Indian patent drafting workflows.

## 2. Scope Boundaries
- **In scope**: Claim trees, specification generation, prior art scans matching Indian Patent Office requirements, querying Google Patents database for novelty checks, and agent-guided brainstorming to modify user ideas based on overlapping prior art.
- **Out of scope**: Direct IP registration portal filings.

## 3. Verification Criteria
1. Manifest files (`plugin.json`, `package.json`) resolve correctly inside the marketplace environments.
2. The `patent-prior-art` workflow executes queries against the Google Patents database via web searches.
3. The agent provides specific recommendations to modify or pivot the user's idea based on matching prior art to improve novelty.

## 4. Decisions (Confirmed)
- Google Patents queries will be performed using agent search capabilities (e.g. web search queries targeting `site:patents.google.com`) during the `patent-prior-art` workflow.

