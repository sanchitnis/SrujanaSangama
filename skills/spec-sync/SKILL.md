---
name: spec-sync
description: >
  Audits the sync state between specification/ files (*-spec.prompt.md, *-tasks.md),
  plugins/ directories, and eval/ coverage. Produces a Markdown drift report.
  Run manually on demand or automatically via the weekly GitHub Actions cron.
version: 1.0.0
tags: [governance, quality, spec-sync, weekly]
---

# Skill: spec-sync — Specification Sync Audit

## Purpose

This skill checks that every plugin's **specification contract**, **task checklist**, **plugin implementation directory**, and **evaluation coverage** are all present and aligned. It catches drift that accumulates when:

- A new plugin directory is created in `plugins/` without a spec file.
- A spec is written but no eval dataset is created.
- Files are added directly to a plugin without updating the matching `*-tasks.md`.

The skill **reports drift only**. It does not fix anything. Fixing drift requires a new Coordinator + Implementor sprint per `AGENTS.md`.

---

## When to Use

- On demand: any time you suspect specs and plugins are out of sync.
- Automatically: every Monday at 09:00 UTC via `.github/workflows/spec-sync-weekly.yml`.

> [!IMPORTANT]
> This skill requires **development mode** to run against spec files.
> Check `context/mode.md` before invoking. If `mode: production`, this skill should not be run.

---

## Trigger Conditions

Invoke this skill when any of the following are true:

- A new directory appears in `plugins/` that does not have a paired spec.
- An `eval/` report references a plugin that no longer exists.
- A `*-tasks.md` references files not yet present in the plugin directory.
- A weekly Monday cron fires (automated via GitHub Actions).

---

## What the Script Checks

The Python script `scripts/spec_sync.py` performs **mechanical file-presence checks only** — it does not read or semantically interpret spec content.

| Check | Pass Condition |
|---|---|
| Spec ↔ Tasks pairing | Every `specification/*-spec.prompt.md` has a matching `specification/*-tasks.md` |
| Spec ↔ Plugin dir | Every spec has a matching `plugins/<plugin-name>/` directory |
| Plugin ↔ Eval script | Every plugin has a matching `eval/eval_<plugin_name>.py` |
| Plugin ↔ Eval dataset | Every plugin has a matching `eval/data/<plugin_name>_eval_dataset.json` |
| Orphan plugin dirs | Every `plugins/<name>/` directory has a spec file |
| Tasks ↔ Eval report | Every `*-tasks.md` has a matching `eval/*_eval_report.md` |

---

## How to Run (Manual / On-Demand)

### Prerequisites

- Python 3.x installed
- Run from the repository root (`d:\Github\SrujanaSangama\` or equivalent)

### Command

```powershell
# Windows PowerShell
python skills/spec-sync/scripts/spec_sync.py

# With explicit output directory
python skills/spec-sync/scripts/spec_sync.py --output-dir eval/logs
```

### Output

The script writes a Markdown report to:
```
eval/logs/spec_sync_YYYY-MM-DD.md
```

It also prints a summary table to stdout.

---

## How to Read the Report

The report uses a ✅ / ❌ / ⚠️ system:

| Symbol | Meaning |
|---|---|
| ✅ | All checks pass — no drift detected |
| ❌ | A required file is missing — drift detected |
| ⚠️ | A partial match (e.g., spec exists but no eval coverage) — investigate |

---

## After Running

1. Open the generated `eval/logs/spec_sync_<date>.md` report.
2. For each ❌ or ⚠️ row, decide:
   - **Create a backlog entry** in `specification/BACKLOG.md` if no spec exists yet.
   - **Start a Coordinator sprint** if a spec exists but implementation is missing.
   - **Author an eval dataset** if a plugin has no eval coverage.
3. Do not attempt to fix drift in the same session as the audit — record it first.

---

## GitHub Actions (Automated Weekly)

The workflow `.github/workflows/spec-sync-weekly.yml` runs this script automatically every Monday at 09:00 UTC and uploads the report as a workflow artifact.

To view weekly reports:
1. Go to the repository → **Actions** tab.
2. Select the **Spec-Sync Weekly Audit** workflow.
3. Open the latest run → download the `spec-sync-report` artifact.
