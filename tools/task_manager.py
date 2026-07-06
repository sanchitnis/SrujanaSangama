#!/usr/bin/env python3
"""
SrujanaSangama Kanban Task Manager Backend Engine
Description: Parses, adds, updates, and aggregates tasks stored in Markdown tables.
             Integrates with SrujanaSangama's path resolution and CEE commands.
"""

import os
import sys
import re
import datetime
import json
from pathlib import Path

# Resolve repository root
REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.append(str(REPO_ROOT / "scripts" / "local"))

try:
    import path_resolver
except ImportError:
    # Fallback path resolver if not run from repo context
    class DummyPathResolver:
        @staticmethod
        def get_srujana_memory_dir():
            return REPO_ROOT.parent / "srujana-memory"
        @staticmethod
        def resolve_path(rel):
            return DummyPathResolver.get_srujana_memory_dir() / rel
    path_resolver = DummyPathResolver

HEADERS = ["Task ID", "Task", "Project", "Assignee", "Status", "Priority", "Scheduled Date", "Est.", "Tag", "Description"]

def locate_memory_dir():
    try:
        return path_resolver.get_srujana_memory_dir()
    except Exception:
        # standard sibling fallback
        return REPO_ROOT.parent / "srujana-memory"

# Parse Markdown table into list of dictionaries
def parse_markdown_table(content):
    lines = content.strip().split("\n")
    if len(lines) < 2:
        return []
    
    # Extract headers
    header_line = lines[0]
    headers = [col.strip() for col in header_line.split("|")[1:-1]]
    
    # Map header names to standard keys
    header_mapping = {
        "Task ID": "id",
        "Task": "task",
        "Project": "project",
        "Assignee": "assignee",
        "Status": "status",
        "Priority": "priority",
        "Scheduled Date": "scheduled_date",
        "Est.": "est",
        "Tag": "tag",
        "Description": "description"
    }
    
    tasks = []
    # Skip header and separator line
    for line in lines[2:]:
        if not line.strip() or not line.strip().startswith("|"):
            continue
        cols = [col.strip() for col in line.split("|")[1:-1]]
        # Pad columns if row is shorter than header
        if len(cols) < len(headers):
            cols += [""] * (len(headers) - len(cols))
            
        task = {}
        for h_idx, h in enumerate(headers):
            key = header_mapping.get(h)
            if key:
                task[key] = cols[h_idx] if h_idx < len(cols) else ""
        
        # Ensure status, priority, and ID exist
        if "id" in task and task["id"]:
            # Normalize status
            status_map = {
                "backlog": "Backlog",
                "todo": "To Do",
                "to do": "To Do",
                "in progress": "In Progress",
                "in-progress": "In Progress",
                "in review": "In Review",
                "in-review": "In Review",
                "done": "Done"
            }
            task["status"] = status_map.get(task.get("status", "").lower(), task.get("status", "To Do"))
            
            # Normalize priority
            prio = task.get("priority", "")
            if "P1" in prio or "🔴" in prio:
                task["priority"] = "🔴 P1"
            elif "P2" in prio or "🟡" in prio:
                task["priority"] = "🟡 P2"
            elif "P3" in prio or "🟢" in prio:
                task["priority"] = "🟢 P3"
            else:
                task["priority"] = prio or "🟡 P2"
                
            tasks.append(task)
            
    return tasks

# Convert list of task dicts to Markdown table string
def serialize_to_markdown_table(tasks):
    if not tasks:
        # Return empty table structure
        lines = [
            "| " + " | ".join(HEADERS) + " |",
            "| " + " | ".join([":---"] * len(HEADERS)) + " |"
        ]
        return "\n".join(lines)
        
    lines = []
    # Header
    lines.append("| " + " | ".join(HEADERS) + " |")
    # Separator
    lines.append("| " + " | ".join([":---"] * len(HEADERS)) + " |")
    
    # Rows
    for t in tasks:
        row = [
            t.get("id", ""),
            t.get("task", ""),
            t.get("project", ""),
            t.get("assignee", ""),
            t.get("status", "To Do"),
            t.get("priority", "🟡 P2"),
            t.get("scheduled_date", ""),
            t.get("est", ""),
            t.get("tag", ""),
            t.get("description", "")
        ]
        # Escape pipe characters in columns to avoid breaking markdown tables
        row = [str(cell).replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(row) + " |")
        
    return "\n".join(lines)

# Find and replace the task table inside a file
def update_table_in_file(file_path, tasks):
    file_path = Path(file_path)
    if not file_path.exists():
        # Create new file with header and table
        new_content = f"# Tasks\n\n{serialize_to_markdown_table(tasks)}\n"
        file_path.write_text(new_content, encoding="utf-8")
        return True
        
    content = file_path.read_text(encoding="utf-8")
    
    # Regex to find Markdown table with Task ID header
    table_pattern = re.compile(
        r"(^\|[^\n]*Task ID[^\n]*\|\s*\n"   # Header row
        r"^\|[\s:\-|\u2500-\u257F]+\|\s*\n" # Separator row
        r"(?:^\|[^\n]*\|\s*\n*)*)",         # Body rows
        re.MULTILINE
    )
    
    match = table_pattern.search(content)
    new_table_str = serialize_to_markdown_table(tasks)
    
    if match:
        # Replace the matched table block
        start_idx, end_idx = match.span()
        new_content = content[:start_idx] + new_table_str + "\n" + content[end_idx:].lstrip()
    else:
        # Append the table to the end of the file
        new_content = content.rstrip() + "\n\n" + new_table_str + "\n"
        
    file_path.write_text(new_content, encoding="utf-8")
    return True

# Read tasks from a file
def read_tasks_from_file(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        return []
    content = file_path.read_text(encoding="utf-8")
    
    table_pattern = re.compile(
        r"(^\|[^\n]*Task ID[^\n]*\|\s*\n"
        r"^\|[\s:\-|\u2500-\u257F]+\|\s*\n"
        r"(?:^\|[^\n]*\|\s*\n*)*)",
        re.MULTILINE
    )
    
    match = table_pattern.search(content)
    if match:
        return parse_markdown_table(match.group(1))
    return []

# Migrate old checklist file to tabular tasks
def migrate_checklist_file(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        return False
        
    content = file_path.read_text(encoding="utf-8")
    
    # Check if table already exists
    if "| Task ID |" in content:
        return False
        
    # Parse checklist items
    lines = content.split("\n")
    tasks = []
    current_category = "Personal"
    task_counter = 1
    
    for line in lines:
        stripped = line.strip()
        # Heading match
        if stripped.startswith("#"):
            h_text = stripped.lstrip("#").strip()
            h_text = re.sub(r"[^\w\s\-]", "", h_text).strip()
            if h_text and not h_text.lower().startswith("task"):
                current_category = h_text
            continue
            
        # Checklist match
        match = re.match(r"^-\s*\[([ xX/])\]\s*(.+)$", stripped)
        if match:
            chk = match.group(1)
            task_text = match.group(2).strip()
            
            # Map status
            status = "To Do"
            if chk == "/" or chk == "\\":
                status = "In Progress"
            elif chk.lower() == "x":
                status = "Done"
                
            # Map priority based on category text or tags
            priority = "🟡 P2"
            if "P1" in current_category or "Critical" in current_category or "🔴" in current_category:
                priority = "🔴 P1"
            elif "P2" in current_category or "Important" in current_category or "🟡" in current_category:
                priority = "🟡 P2"
            elif "P3" in current_category or "Nice to Have" in current_category or "🟢" in current_category:
                priority = "🟢 P3"
                
            # Extract tags if any
            tags = []
            if "#" in task_text:
                found_tags = re.findall(r"(#[a-zA-Z0-9_-]+)", task_text)
                tags.extend(found_tags)
                task_text = re.sub(r"(#[a-zA-Z0-9_-]+)", "", task_text).strip()
                
            tag_str = ", ".join(tags) if tags else ""
            if priority == "🔴 P1" and not tag_str:
                tag_str = "#deep-work"
                
            tasks.append({
                "id": f"pers-{task_counter:03d}",
                "task": task_text,
                "project": "Personal",
                "assignee": "",
                "status": status,
                "priority": priority,
                "scheduled_date": (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d"),
                "est": "2 hrs",
                "tag": tag_str,
                "description": f"Migrated from checklist: {current_category}"
            })
            task_counter += 1
            
    if tasks:
        # Write back as table
        header_part = []
        for line in lines:
            if line.strip().startswith("- [") or line.strip().startswith("##"):
                break
            header_part.append(line)
            
        header_text = "\n".join(header_part).rstrip()
        new_content = header_text + "\n\n" + serialize_to_markdown_table(tasks) + "\n"
        file_path.write_text(new_content, encoding="utf-8")
        return True
        
    return False

# Aggregate all tasks across personal and project directories
def aggregate_all_tasks():
    mem_dir = locate_memory_dir()
    all_tasks = []
    
    # 1. Personal Tasks
    pers_path = mem_dir / "my-memory" / "context" / "tasks.md"
    if pers_path.exists():
        pers_tasks = read_tasks_from_file(pers_path)
        for t in pers_tasks:
            t["source_file"] = "my-memory/context/tasks.md"
            t["project_name"] = "Personal"
            all_tasks.append(t)
            
    # 2. Collaborative Projects
    collabs_dir = mem_dir / "collaborations"
    if collabs_dir.exists():
        for proj_folder in collabs_dir.iterdir():
            if proj_folder.is_dir():
                proj_tasks_path = proj_folder / "tasks.md"
                if proj_tasks_path.exists():
                    proj_tasks = read_tasks_from_file(proj_tasks_path)
                    for t in proj_tasks:
                        t["source_file"] = f"collaborations/{proj_folder.name}/tasks.md"
                        t["project_name"] = proj_folder.name.replace("-", " ").title()
                        all_tasks.append(t)
                        
    return all_tasks

# Trigger rebuilds of the HTML portals
def rebuild_dashboards():
    print("Rebuilding user dashboards...")
    for script_name in ["build_faculty_dashboard.py", "build_scholar_dashboard.py"]:
        script_path = REPO_ROOT / "tools" / script_name
        if script_path.exists():
            # Run the builder script in python
            os.system(f"python \"{script_path}\"")

# Update a single task in its corresponding source file
def update_task_field(task_id, fields_to_update):
    tasks = aggregate_all_tasks()
    target_task = None
    for t in tasks:
        if t["id"] == task_id:
            target_task = t
            break
            
    if not target_task:
        print(f"[ERROR] Task ID '{task_id}' not found.")
        return False
        
    source_file_rel = target_task["source_file"]
    mem_dir = locate_memory_dir()
    file_path = mem_dir / source_file_rel
    
    # Read tasks in that file
    file_tasks = read_tasks_from_file(file_path)
    updated = False
    for t in file_tasks:
        if t["id"] == task_id:
            for k, v in fields_to_update.items():
                if v is not None:
                    # Normalize Status updates
                    if k == "status":
                        status_map = {
                            "backlog": "Backlog",
                            "todo": "To Do",
                            "to do": "To Do",
                            "in progress": "In Progress",
                            "in-progress": "In Progress",
                            "in review": "In Review",
                            "in-review": "In Review",
                            "done": "Done"
                        }
                        t[k] = status_map.get(v.lower(), v)
                    else:
                        t[k] = v
            updated = True
            break
            
    if updated:
        update_table_in_file(file_path, file_tasks)
        print(f"[SUCCESS] Task '{task_id}' updated in {source_file_rel}.")
        rebuild_dashboards()
        return True
        
    return False

# Add a task to personal list or project list
def add_task(project_slug, task_name, assignee=None, status="To Do", priority="🟡 P2", scheduled_date=None, est=None, tag=None, description=None):
    mem_dir = locate_memory_dir()
    
    if not scheduled_date:
        scheduled_date = datetime.date.today().strftime("%Y-%m-%d")
        
    # Determine file path
    if project_slug.lower() == "personal":
        file_path = mem_dir / "my-memory" / "context" / "tasks.md"
        prefix = "pers"
        proj_name = "Personal"
    else:
        proj_dir = mem_dir / "collaborations" / project_slug
        proj_dir.mkdir(parents=True, exist_ok=True)
        file_path = proj_dir / "tasks.md"
        prefix = project_slug[:4].lower().replace("-", "")
        proj_name = project_slug.replace("-", " ").title()
        
    # Read existing tasks to determine next ID counter
    existing = read_tasks_from_file(file_path)
    counter = len(existing) + 1
    new_id = f"{prefix}-{counter:03d}"
    while any(t["id"] == new_id for t in existing):
        counter += 1
        new_id = f"{prefix}-{counter:03d}"
        
    new_task = {
        "id": new_id,
        "task": task_name,
        "project": proj_name,
        "assignee": assignee or "",
        "status": status,
        "priority": priority,
        "scheduled_date": scheduled_date,
        "est": est or "2 hrs",
        "tag": tag or "",
        "description": description or ""
    }
    
    existing.append(new_task)
    update_table_in_file(file_path, existing)
    print(f"[SUCCESS] Added task '{new_id}' to {file_path.name}.")
    rebuild_dashboards()
    return new_id

# List backlog files
def list_backlog_files():
    mem_dir = locate_memory_dir()
    backlog_dir = mem_dir / "my-memory" / "context" / "backlog"
    if not backlog_dir.exists():
        return []
    
    files = []
    for item in backlog_dir.iterdir():
        if item.is_file():
            files.append(item.name)
    return files

# Archive backlog file to task-created subfolder
def archive_backlog_file(filename):
    mem_dir = locate_memory_dir()
    src = mem_dir / "my-memory" / "context" / "backlog" / filename
    dest_dir = mem_dir / "my-memory" / "context" / "backlog" / "task-created"
    dest = dest_dir / filename
    
    if not src.exists():
        print(f"[ERROR] Backlog file '{filename}' does not exist.")
        return False
        
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Resolve conflict if file already exists in archive
    if dest.exists():
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        name_parts = filename.rsplit(".", 1)
        if len(name_parts) == 2:
            dest = dest_dir / f"{name_parts[0]}_{timestamp}.{name_parts[1]}"
        else:
            dest = dest_dir / f"{filename}_{timestamp}"
            
    try:
        import shutil
        shutil.move(str(src), str(dest))
        print(f"[SUCCESS] Moved '{filename}' to backlog/task-created/.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to move '{filename}': {e}")
        return False

# Command line parsing
def main():
    import argparse
    parser = argparse.ArgumentParser(description="SrujanaSangama Kanban Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")
    
    # 1. Aggregate / List
    list_p = subparsers.add_parser("list", help="List and aggregate tasks")
    list_p.add_argument("--json", action="store_true", help="Output as structured JSON")
    
    # 2. Add
    add_p = subparsers.add_parser("add", help="Add a new task")
    add_p.add_argument("--project", required=True, help="Project folder slug (e.g. book-sdd, or 'personal')")
    add_p.add_argument("--task", required=True, help="Task name / title")
    add_p.add_argument("--assignee", help="Task assignee handle (e.g. @akhil)")
    add_p.add_argument("--status", default="To Do", help="Task Status")
    add_p.add_argument("--priority", default="🟡 P2", help="Priority (🔴 P1, 🟡 P2, 🟢 P3)")
    add_p.add_argument("--scheduled", help="Scheduled date (YYYY-MM-DD)")
    add_p.add_argument("--est", help="Time estimate (e.g. 2 hrs)")
    add_p.add_argument("--tag", help="Task tag/focus (e.g. #deep-work)")
    add_p.add_argument("--desc", help="Detailed description")
    
    # 3. Update
    update_p = subparsers.add_parser("update", help="Update an existing task")
    update_p.add_argument("task_id", help="Task ID (e.g. pers-001, sdd-002)")
    update_p.add_argument("--status", help="New status")
    update_p.add_argument("--assignee", help="New assignee")
    update_p.add_argument("--priority", help="New priority")
    update_p.add_argument("--scheduled", help="New scheduled date (YYYY-MM-DD)")
    update_p.add_argument("--est", help="New time estimate")
    update_p.add_argument("--tag", help="New tag")
    update_p.add_argument("--desc", help="New description")
    
    # 4. Migrate
    migrate_p = subparsers.add_parser("migrate", help="Migrate old checklist tasks.md to tabular tasks.md")
    migrate_p.add_argument("file_path", help="Absolute path to target tasks.md file")
    
    # 5. List Backlog
    subparsers.add_parser("list-backlog", help="List all pending files in the backlog folder")
    
    # 6. Archive Backlog
    archive_p = subparsers.add_parser("archive-backlog", help="Move a backlog file to the task-created directory")
    archive_p.add_argument("filename", help="Name of the file to archive")
    
    args = parser.parse_args()
    
    if args.command == "list":
        tasks = aggregate_all_tasks()
        if args.json:
            print(json.dumps(tasks, indent=2))
        else:
            print(f"\nAggregated Tasks ({len(tasks)} found):\n")
            print(f"{'ID':<10} | {'Task':<40} | {'Project':<15} | {'Status':<12} | {'Priority':<8} | {'Date':<10}")
            print("-" * 105)
            for t in tasks:
                print(f"{t['id']:<10} | {t['task'][:40]:<40} | {t['project']:<15} | {t['status']:<12} | {t['priority']:<8} | {t['scheduled_date']:<10}")
            print()
            
    elif args.command == "add":
        new_id = add_task(
            project_slug=args.project,
            task_name=args.task,
            assignee=args.assignee,
            status=args.status,
            priority=args.priority,
            scheduled_date=args.scheduled,
            est=args.est,
            tag=args.tag,
            description=args.desc
        )
        print(f"Task created successfully. ID: {new_id}")
        
    elif args.command == "update":
        fields = {
            "status": args.status,
            "assignee": args.assignee,
            "priority": args.priority,
            "scheduled_date": args.scheduled,
            "est": args.est,
            "tag": args.tag,
            "description": args.desc
        }
        fields = {k: v for k, v in fields.items() if v is not None}
        if not fields:
            print("No fields specified for update.")
            sys.exit(1)
        success = update_task_field(args.task_id, fields)
        if not success:
            sys.exit(1)
            
    elif args.command == "migrate":
        success = migrate_checklist_file(args.file_path)
        if success:
            print(f"Successfully migrated {args.file_path} to tabular format.")
            rebuild_dashboards()
        else:
            print(f"File {args.file_path} already contains tabular data or has no migration targets.")
            
    elif args.command == "list-backlog":
        files = list_backlog_files()
        print(json.dumps(files))
        
    elif args.command == "archive-backlog":
        success = archive_backlog_file(args.filename)
        if not success:
            sys.exit(1)
            
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
