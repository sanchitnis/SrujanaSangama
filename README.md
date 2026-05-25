# SrujanaSangama — Private AI Agent & Skill Plugin Marketplace

Welcome to the **SrujanaSangama Private AI Agent & Skill Plugin Marketplace** for REVA University. This platform serves as a centralized private hub for academic and professional agents and capabilities across the REVA campus ecosystem.

To achieve complete multi-platform compatibility for REVA University, the repository utilizes a **dual-engine architecture**. This approach allows a single, unified codebase to share core prompt logic and external tools (using the Model Context Protocol standard) while loading dynamically into separate AI hosts: **Google Antigravity** and **GitHub Copilot**.

---

## 1. Unified Directory Layout

A single plugin directory contains the manifests for both hosts alongside shared system guidelines (prompts), rules, and execution workflows:

```plaintext
SrujanaSangama/
├── .antigravity-marketplace/
│   └── marketplace.json         # Google Antigravity Central Index
├── .github/
│   └── copilot-marketplace.json # GitHub Copilot Private Registry Map
├── plugins/                     # Private Plugin Directory
│   ├── teaching-learning-reva/  # T - Educator Hat: Course, session, content, assessment integrity
│   ├── research-reva/           # R - Scholar Hat: Projects, grant proposals, manuscript writing
│   ├── academic-admin-reva/     # A - Administrator Hat: Programs, BOS, compliance, CO attainments
│   ├── consulting-product-reva/ # C - Consultant Hat: Experiential labs, patents, MOU reviews
│   └── kaizen-wellbeing-reva/   # K - Self-Improver Hat: Kaizen coach, wellbeing reflection (Hitaishin)
├── specification/               # System Specifications and Abstractions
│   ├── architecture.md          # Platform Dual-Engine Architecture
│   ├── track_scope.md           # Scope and Platform Capabilities
│   ├── ADDIE.md                 # ADDIE Instructional Design flow
│   ├── Hitaishin/               # Personal Wellbeing Coaching Subsystem (Read-Only)
│   └── SrujanaBuddy/            # Student Action/Productivity Buddy (Read-Only)
└── docs/                        # Guidelines and Reference Documentation
    ├── AISkills and Technologies.md
    └── Guidelines/
        ├── CourseProjects.md
        ├── MiniProject.md
        └── FinalYearProject.md
```

---

## 2. Core Plugin Logic (Shared Codebase)

By placing AI core guidelines and prompt chains in independent markdown files, both platforms read the exact same instructions:
- **Shared System Boundary (`rules/`)**: Instructs the agent to guide students through problems without exposing final code answers, enforcing the official REVA formatting style guide.
- **Shared Slash Commands (`workflows/`)**: Shared prompt templates mapped to custom slash commands (e.g., `/audit`, `/grant`, `/attainment`, `/patent`, `/gps`).

---

## 3. Dual-Engine Manifests & Tooling

Each plugin is package-compliant with both runtime hosts:
1. **Google Antigravity (`plugin.json`)**: Configures local Gemini execution layers, system guidelines, and MCP configurations.
2. **GitHub Copilot (`package.json`)**: Integrates configurations via the Node.js/VS Code extension framework, registering the agent under a dedicated sidebar handle (e.g. `@reva-educator`, `@reva-scholar`, `@reva-admin`, `@reva-innovator`, `@reva-kaizen`).
3. **Model Context Protocol (`mcp.json`)**: Connects plugins securely to university databases, APIs, or local file parsers across both AI hosts using a standard RPC interface.

---

## 4. How Deployment Works on Campus Workstations

### For Google Antigravity Users
Workstations configure their CLI tool to map to the central repository index:
```bash
antigravity-cli marketplace add srujanasangama <registry-endpoint-url>
```
The client fetches and loads plugins directly into the IDE context based on the `.antigravity-marketplace/marketplace.json` index.

### For GitHub Copilot Users
Campus developers log into their VS Code environment using their official `@reva.edu.in` single sign-on credentials. Because the repository's `.github/copilot-marketplace.json` associates allowed teams, the Copilot engine maps the agent contributions, and the agents activate automatically in their sidebar.

---

## 5. Campus Project Guidelines

Refer to the official guides below for detailed instructions on campus project standards:
1. [Course Projects](docs/Guidelines/CourseProjects.md)
2. [Miniprojects](docs/Guidelines/MiniProject.md)
3. [Final Year Projects](docs/Guidelines/FinalYearProject.md)
