# Plan — SrujanaSangama Master Plan & Active Roadmap

This document outlines the high-level plan and active sprint focus for the SrujanaSangama private marketplace platform.

## Active Sprint Scope
We are currently in Phase 1: restructuring the repository layout to support a clean, unified specifications folder (`specification/`) and executing the CSE/CSA school active roadmap for the `reva.srujana-shodha` plugin.

## Directory Structure Design
To keep repository maintenance clean, all specifications (`*-spec.md`) and atomic tasks (`*-tasks.md`) are consolidated in the `specification/` directory:
- `spec.prompt.md` (Top-level specs)
- `tasks.md` (Top-level backlog tasks)
- `architecture.prompt.md` (Platform architecture specs)
- `plan.prompt.md` (Master plan/sprint plan)
- `<plugin>-spec.prompt.md` (Plugin-specific details)
- `<plugin>-tasks.md` (Plugin-specific task checkpoints)

## High-Level Verification Criteria
1. **Directory Consolidation**: `plan/` directory is deleted, and all specs reside under `specification/`.
2. **Constitutional Alignment**: `CONSTITUTION.md` maps exactly to the new directory layout and naming conventions.
3. **Dual-Engine Deployments**: Manifests (`plugin.json`, `package.json`) within each plugin remain completely synchronized with their folders and index registries.
