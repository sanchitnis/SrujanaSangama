#!/usr/bin/env python3
import unittest
import sys
import os
import shutil
import tempfile
from pathlib import Path

# Resolve paths
REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.append(str(REPO_ROOT / "tools"))

import task_manager

class TestTaskManager(unittest.TestCase):

    def test_parse_markdown_table(self):
        table_str = """
| Task ID | Task | Project | Assignee | Status | Priority | Scheduled Date | Est. | Tag | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| pers-001 | Test task 1 | Personal | @test | in progress | 🔴 P1 | 2026-07-10 | 2 hrs | #deep-work | Test desc |
| pers-002 | Test task 2 | Personal |  | done | 🟡 P2 | 2026-07-15 | 1 hr | | Another desc |
"""
        tasks = task_manager.parse_markdown_table(table_str)
        self.assertEqual(len(tasks), 2)
        
        self.assertEqual(tasks[0]["id"], "pers-001")
        self.assertEqual(tasks[0]["task"], "Test task 1")
        self.assertEqual(tasks[0]["status"], "In Progress")
        self.assertEqual(tasks[0]["priority"], "🔴 P1")
        self.assertEqual(tasks[0]["tag"], "#deep-work")
        
        self.assertEqual(tasks[1]["id"], "pers-002")
        self.assertEqual(tasks[1]["status"], "Done")
        self.assertEqual(tasks[1]["priority"], "🟡 P2")
        self.assertEqual(tasks[1]["assignee"], "")

    def test_resilience(self):
        # Test uneven spacing, missing trailing pipe, loose status mapping
        table_str = """
| Task ID | Task | Project | Assignee | Status | Priority | Scheduled Date | Est. | Tag | Description |
|---|---|---|---|---|---|---|---|---|---|
| sdd-101 | Spaced Task | Project | @member |   in-progress   | P1 | 2026-07-20 | 4h | #deep | Desc with trailing spaces   |
| sdd-102 | Short Row | Proj | | todo |
"""
        tasks = task_manager.parse_markdown_table(table_str)
        self.assertEqual(len(tasks), 2)
        
        self.assertEqual(tasks[0]["status"], "In Progress")
        self.assertEqual(tasks[0]["priority"], "🔴 P1")
        self.assertEqual(tasks[0]["description"], "Desc with trailing spaces")
        
        self.assertEqual(tasks[1]["id"], "sdd-102")
        self.assertEqual(tasks[1]["status"], "To Do")
        self.assertEqual(tasks[1]["priority"], "🟡 P2") # Default priority
        self.assertEqual(tasks[1]["scheduled_date"], "")

    def test_serialize_table(self):
        tasks = [
            {
                "id": "pers-001",
                "task": "Test serialization",
                "project": "Personal",
                "assignee": "@user",
                "status": "In Progress",
                "priority": "🔴 P1",
                "scheduled_date": "2026-07-10",
                "est": "2 hrs",
                "tag": "#deep-work",
                "description": "Test description"
            }
        ]
        table_str = task_manager.serialize_to_markdown_table(tasks)
        self.assertIn("| Task ID | Task |", table_str)
        self.assertIn("| pers-001 | Test serialization | Personal | @user | In Progress | 🔴 P1 | 2026-07-10 | 2 hrs | #deep-work | Test description |", table_str)

    def test_file_operations(self):
        # Create a temp file
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_path = Path(tmpdir) / "tasks.md"
            initial_content = """# Active Tasks List
Please read this file.

| Task ID | Task | Project | Assignee | Status | Priority | Scheduled Date | Est. | Tag | Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| pers-001 | Initial task | Personal | | To Do | 🟡 P2 | 2026-07-10 | 1 hr | | Initial |

Some other text below.
"""
            temp_path.write_text(initial_content, encoding="utf-8")
            
            # Read tasks
            tasks = task_manager.read_tasks_from_file(temp_path)
            self.assertEqual(len(tasks), 1)
            self.assertEqual(tasks[0]["id"], "pers-001")
            
            # Modify and update
            tasks[0]["status"] = "Done"
            task_manager.update_table_in_file(temp_path, tasks)
            
            # Read again
            updated_content = temp_path.read_text(encoding="utf-8")
            self.assertIn("| pers-001 | Initial task | Personal |  | Done | 🟡 P2 | 2026-07-10 | 1 hr |  | Initial |", updated_content)
            self.assertIn("# Active Tasks List", updated_content)
            self.assertIn("Some other text below.", updated_content)

    def test_migration(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_path = Path(tmpdir) / "old_tasks.md"
            checklist_content = """# My Tasks
## 🔴 P1 — Critical
- [ ] Tasks validation run
- [/] Guideline checks #deep-work

## 🟡 P2 — Important
- [x] Onboard completed
"""
            temp_path.write_text(checklist_content, encoding="utf-8")
            
            # Migrate
            success = task_manager.migrate_checklist_file(temp_path)
            self.assertTrue(success)
            
            # Read migrated tasks
            tasks = task_manager.read_tasks_from_file(temp_path)
            self.assertEqual(len(tasks), 3)
            
            self.assertEqual(tasks[0]["id"], "pers-001")
            self.assertEqual(tasks[0]["status"], "To Do")
            self.assertEqual(tasks[0]["priority"], "🔴 P1")
            
            self.assertEqual(tasks[1]["id"], "pers-002")
            self.assertEqual(tasks[1]["status"], "In Progress")
            self.assertEqual(tasks[1]["tag"], "#deep-work")
            
            self.assertEqual(tasks[2]["id"], "pers-003")
            self.assertEqual(tasks[2]["status"], "Done")
            self.assertEqual(tasks[2]["priority"], "🟡 P2")

    def test_backlog_operations(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Mock locate_memory_dir to return this temp dir
            original_locate = task_manager.locate_memory_dir
            task_manager.locate_memory_dir = lambda: Path(tmpdir)
            
            try:
                backlog_dir = Path(tmpdir) / "my-memory" / "context" / "backlog"
                backlog_dir.mkdir(parents=True, exist_ok=True)
                
                # Write mock files
                (backlog_dir / "meeting-minutes.txt").write_text("Mock meeting minutes", encoding="utf-8")
                (backlog_dir / "email.txt").write_text("Mock email task", encoding="utf-8")
                
                # Verify listing
                files = task_manager.list_backlog_files()
                self.assertEqual(len(files), 2)
                self.assertIn("meeting-minutes.txt", files)
                self.assertIn("email.txt", files)
                
                # Verify archiving
                success = task_manager.archive_backlog_file("email.txt")
                self.assertTrue(success)
                
                # Check file moved
                self.assertFalse((backlog_dir / "email.txt").exists())
                self.assertTrue((backlog_dir / "task-created" / "email.txt").exists())
                
                # Verify listing again (should only have 1 file)
                files_after = task_manager.list_backlog_files()
                self.assertEqual(len(files_after), 1)
                self.assertIn("meeting-minutes.txt", files_after)
                
            finally:
                # Restore original function
                task_manager.locate_memory_dir = original_locate

if __name__ == "__main__":
    unittest.main()
