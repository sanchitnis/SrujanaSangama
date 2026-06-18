# SrujanaSangama

**An agentic human-AI collaboration platform for REVA University** — covering Teaching \& Learning, Research, Academic Administration, Consulting \& Product Development, and Kaizen \& Institutional Excellence (T.R.A.C.K.), for faculty, research scholars, administrative staff, and institutional leadership.

SrujanaSangama is not an app you install. It is, and will remain, a **shared, read-only folder of plain-markdown instructions** that you open directly in an AI coding assistant you may already have — **Claude Code**, **GitHub Copilot in VS Code**, or **Google Antigravity** — alongside a private folder of your own.

A parallel platform, **SrujanaBuddy**, serves students. This repository is for faculty, scholars, and staff.

\---

## Where Things Stand Right Now

This repository is being built incrementally. The full vision is described in `architecture.md` (what it will do) and `design.md` (how it will be built), and **both of those documents describe the complete target system regardless of how much of it exists today.**

This README only describes what you can actually do **right now**. The current build status of every planned domain is tracked in [`specification/IMPLEMENTATION-STATUS.md`](specification/IMPLEMENTATION-STATUS.md) — check it any time you want to know whether something you've read about in `architecture.md` or `design.md` is usable yet.

At the moment, the platform's domain layer (`domains/`, `skills/`, `validators/`) has not yet been built — only the governance and vision documents exist. There is nothing to set up or run yet. **This section will be replaced with real setup steps as soon as the first domain (`onboarding`) is implemented.**

If you'd like to see what's coming, `architecture.md` is the best starting point — it has no technical detail, just a plain description of what the platform is intended to do for you.

\---

## What's in This Repository Today

|File / Folder|Purpose|Status|
|-|-|-|
|`architecture.md`|What the platform does — the full T.R.A.C.K. capability vision|Complete|
|`design.md`|How the platform is built — domains, agents, skills, commands, memory architecture|Complete|
|`CONSTITUTION.md`|Conventions and guardrails governing how this repository may be changed|Complete|
|`AGENTS.md`|Roles and process for proposing and making changes to the platform|Complete|
|`CONTRIBUTING.md`|Practical steps for contributing a change|Complete|
|`specification/IMPLEMENTATION-STATUS.md`|What exists vs. what is still planned — check here for the current build status|Living document|
|`domains/`, `skills/`, `validators/`|The actual instruction files and tools an agent will use, domain by domain|Not yet built|

This repository is read-only for everyone except REVA IT and the maintainer. If something here should change, see `CONTRIBUTING.md`.

\---

## Terms of Use

By using SrujanaSangama, you agree to the terms in the [LICENSE](file:///d:/Github/SrujanaSangama/LICENSE) file:

* **Confidentiality** — the contents of this repository are confidential and proprietary to REVA University and must not be shared outside it.
* **Authorised access** — limited to current REVA University students, faculty, and staff as authorised by REVA IT.
* **Attribution** — any internal modification must retain copyright notices and credit REVA University.

\---

*REVA University — Educate to Enterprise
Maintained by Dr. Sanjay Chitnis (@sanchitnis), in collaboration with Claude.ai*

