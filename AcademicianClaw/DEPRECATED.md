# AcademicianClaw — Deprecated Root

> ⚠️ **This directory is deprecated.**
>
> The OpenClaw system has been migrated to the SrujanaSangama plugin at:
> **[`plugins/academician-claw/`](../plugins/academician-claw/)**
>
> All agent skills, prompts, workflows, and scripts now live there.
> The memory files from `openclaw-system/openclaw-system/memory/` remain here on your local machine only (gitignored) — they are not affected by the migration.

## What moved where

| Old location | New location |
|---|---|
| `openclaw-system/openclaw-system/agents/` | `plugins/academician-claw/agents/` |
| `openclaw-system/openclaw-system/prompts/session/ORCHESTRATOR.md` | `plugins/academician-claw/rules/ORCHESTRATOR.md` |
| `openclaw-system/openclaw-system/prompts/agents/` | *(prompts are now loaded from rules/ and workflows/)* |
| `openclaw-system/openclaw-system/prompts/workflows/` | `plugins/academician-claw/workflows/` |
| `openclaw-system/openclaw-system/scripts/local/` | `plugins/academician-claw/scripts/` |
| `ORCHESTRATOR.md` (root duplicate) | deleted |
| `SESSION_CLOSER.md` (root duplicate) | deleted |
| `context_builder.py` (root duplicate) | deleted |
| `update_memory.py` (root duplicate) | deleted |

## Next steps for existing users

1. Go to `plugins/academician-claw/`
2. Run `python scripts/init.py` to set up the new `memory/` directory location
3. Copy your existing `openclaw-system/openclaw-system/memory/` contents into `plugins/academician-claw/memory/`
4. Update any shortcuts/aliases that pointed to the old script paths
