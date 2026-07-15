# SrujanaSangama Development and Specifications Guide

This directory is where changes to the platform are proposed, reviewed, and staged before they are actually implemented. It contains system specifications, proposals, and task lists.

---

## Development Mode

This workspace rules and conventions apply if a `.git` folder exists at the root of `SrujanaSangama/`, indicating a development checkout.

If `.git` is present, contributors can modify `SrujanaSangama` files to add or improve domains, commands, and skills. Contributors should be added as collaborators and clone the [sanchitnis/SrujanaSangama](https://github.com/sanchitnis/SrujanaSangama) GitHub repository.

### 1. Workspace Rules in Development Mode
- **SrujanaSangama** becomes read-write. Changes are managed via Git.
- **srujana-memory** is strictly used for testing commands with synthetic or mock user data for testing purposes (never commit or use personal data here).
- **Before making any modifications**, read:
  - [CONSTITUTION.md](../CONSTITUTION.md) - Immutable rules, Mode triggers, and conventions.
  - [CONTRIBUTING.md](../CONTRIBUTING.md) - Detailed instructions on the proposal and pull request workflow.

### 2. Repository Structure
```text
SrujanaSangama/
├── AGENTS.md                 # Cross-IDE router for agents
├── GEMINI.md                 # Gemini / Antigravity shim
├── CONSTITUTION.md           # Governance, modes, and conventions
├── CONTRIBUTING.md           # Contributor mechanics
├── IMPLEMENTATION-STATUS.md  # Current status of implemented domains
├── srujana.code-workspace    # Shared multi-root workspace file
├── domains/                  # Faculty/admin modules by domain
│   └── README.md             # List of domains and commands
├── .agents/                  # Workspace customizations
│   └── skills/               # Shared reusable reference modules
├── validators/               # Quality-gate scripts for checking formats
├── scripts/                  # Helper scripts (file I/O, date math, parsing)
└── specification/            # Proposals, tasks, and system specifications
    └── README.md             # This development guide
```

For workspace usage and setup instructions, refer to the [Root README](../README.md).
For personal memory structure details, refer to the [srujana-memory README](../../srujana-memory/README.md).
