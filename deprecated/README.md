# Deprecated Agent Systems

This directory contains deprecated agent plugins and systems that have been superceded or integrated into newer components. They are kept here for historical reference, backward compatibility audits, and manual migration checks.

---

## Deprecated Components

### 1. `AcademicianClaw`
- **Status**: Deprecated.
- **Replacement**: Migrated to `plugins/academician-claw/` as a proper, structured Copilot plugin.
- **Reference**: See the migration guide in [`AcademicianClaw/DEPRECATED.md`](./AcademicianClaw/DEPRECATED.md) for details.

### 2. `research-reva` (Faculty Research Advisor)
- **Status**: Deprecated.
- **Replacement**: Merged with the PhD Scholar system into the unified [`plugins/srujana-shodha/`](../plugins/srujana-shodha/) plugin. All faculty advisor specialist agents, rules, and workflows are now loaded and orchestrated there.
