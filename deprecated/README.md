# Deprecated Agent Systems

This directory contains deprecated agent plugins and systems that have been superceded or integrated into newer components. They are kept here for historical reference, backward compatibility audits, and manual migration checks.

---

## Deprecated Components

### 1. `AcademicianClaw`
- **Status**: Deprecated.
- **Replacement**: Migrated to `domains/personal-productivity/` as a proper, structured integrated module (referenced as `@claw`).
- **Reference**: See the historical files in [`deprecated/plugins/academician-claw/`](./plugins/academician-claw/) and the guide in [`AcademicianClaw/DEPRECATED.md`](./AcademicianClaw/DEPRECATED.md).

### 2. `research-reva` (Faculty Research Advisor)
- **Status**: Deprecated.
- **Replacement**: Merged with the PhD Scholar system into the unified [`domains/srujana-shodha/`](../domains/srujana-shodha/) domain module (referenced as `@reva-scholar`). All faculty advisor specialist agents, rules, and workflows are now loaded and orchestrated there.
- **Reference**: See the historical files in [`deprecated/plugins/srujana-shodha/`](./plugins/srujana-shodha/).

### 3. `memory/` (Centralized User Memory Folder in Repo)
- **Status**: Deprecated.
- **Reason/Replacement**: Active user memory files must exist strictly outside the repository boundary in the user's local/personal `srujana-memory/` workspace (per `CONSTITUTION.md` §8 and `design.md` §3). Any reusable memory structure templates are now shipped exclusively in [`domains/personal-productivity/memory-templates/`](../domains/personal-productivity/memory-templates/) and [`domains/onboarding/memory-templates/`](../domains/onboarding/memory-templates/).

### 4. `plugins/` (Legacy Plugin Implementations)
- **Status**: Deprecated.
- **Reason/Replacement**: All standalone plugins have transitioned into integrated **Modules** located directly within the core [`domains/`](../domains/) and [`skills/`](../skills/) folders. No standalone plugins remain in active use.

