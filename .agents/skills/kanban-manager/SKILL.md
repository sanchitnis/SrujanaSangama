---
name: kanban-manager
description: Manage user tasks in Markdown tables and Kanban boards. Helps users add, update, list, and move tasks across projects.
---

# Skill: Kanban Task Manager

You are a specialized agent capable of managing user tasks inside Markdown tables within the SrujanaSangama workspace. 

## Task Storage Format
Tasks are stored in Markdown tables in:
1. Personal Tasks: `srujana-memory/my-memory/context/tasks.md`
2. Collaborative Projects: `srujana-memory/collaborations/<project_slug>/tasks.md`

The table format must strictly follow:
`| Task ID | Task | Project | Assignee | Status | Priority | Scheduled Date | Est. | Tag | Description |`

## Core Script Operations
Always use the CLI helper `tools/task_manager.py` to read, write, or modify tasks. Do not write complex regex modifications directly to the tables manually.

### 1. List / Read Tasks
To list tasks or check existing task IDs, execute:
```powershell
python tools/task_manager.py list --json
```

### 2. Add a Task
To create a task in a personal or project folder, execute:
```powershell
python tools/task_manager.py add --project <project_slug_or_personal> --task "Task description" --assignee "@username" --status "To Do" --priority "🟡 P2" --scheduled "YYYY-MM-DD" --est "2 hrs" --tag "#deep-work" --desc "Detailed description"
```
*Note*: Personal tasks should use `--project personal`.

### 3. Update a Task
To update fields (e.g., status, assignee, priority, scheduled date, tags) of an existing task:
```powershell
python tools/task_manager.py update <task_id> --status "In Progress" --assignee "@username"
```
This automatically updates the corresponding Markdown table and rebuilds the HTML dashboard portals.

### 4. Migrate checklist tasks to table
If a task file is in checkbox list format, migrate it to the tabular format:
```powershell
python tools/task_manager.py migrate <absolute_path_to_tasks.md>
```

### 5. Backlog Processing
To discover pending raw task files (emails, meeting notes, etc.) placed by the user:
```powershell
python tools/task_manager.py list-backlog
```
This returns a JSON list of files inside the `my-memory/context/backlog/` directory.

To move/archive a processed backlog file to the archive:
```powershell
python tools/task_manager.py archive-backlog <filename>
```
This moves `<filename>` to `my-memory/context/backlog/task-created/`.

## Agent Workflows

### Scenario A: User wants to add a task
- Ask for missing details if necessary (Project, Assignee, Scheduled Date, Priority).
- Call `tools/task_manager.py add` with the appropriate parameters.
- Rebuild dashboards (automatically handled by the script) and notify the user of the new Task ID.

### Scenario B: User wants to move/update a task
- When the user says "Move task pers-001 to Done" or "Assign sdd-003 to Radhika":
- Execute `tools/task_manager.py update <task_id> --status <status>` or `--assignee <assignee>`.
- Rebuild dashboards (automatically handled by the script) and confirm the success status.

### Scenario C: Processing the raw task backlog folder
- If the user says "process backlog", "check backlog", or triggers a periodic review:
  1. Call `python tools/task_manager.py list-backlog` to get any pending files.
  2. If files are found:
     - For each file, read its raw text content using the file viewing tool.
     - Analyze the content (e.g., email text, meeting minutes) and extract individual task items.
     - For each task, extract/infer: Task name, Project, Assignee, Status, Priority, Scheduled Date, Est., Tag, and Description.
     - Add each task by executing `python tools/task_manager.py add --project <project> --task "<task>" ...`
     - Once all tasks in a file are processed, call `python tools/task_manager.py archive-backlog <filename>` to archive the raw file.
  3. Inform the user of the newly created tasks and their corresponding IDs.
