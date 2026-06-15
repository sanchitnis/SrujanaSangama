import os
import sys
import re
import json
from pathlib import Path

# Resolve repo root
REPO_ROOT = Path(__file__).parent.parent.resolve()

def locate_srujana_memory():
    # 1. Env Var
    env_path = os.environ.get("SRUJANA_MEMORY_DIR")
    if env_path and Path(env_path).exists():
        return Path(env_path).resolve()
        
    # 2. Walk up parent directory tree from REPO_ROOT and current directory to find srujana-memory
    search_starts = [REPO_ROOT, Path.cwd()]
    for start in search_starts:
        curr = start.resolve()
        # Traverse up to the drive root
        while curr != curr.parent:
            # Check if it's a child here or a sibling
            sibling = curr / "srujana-memory"
            if sibling.exists() and sibling.is_dir():
                return sibling.resolve()
            sibling_sibling = curr.parent / "srujana-memory"
            if sibling_sibling.exists() and sibling_sibling.is_dir():
                return sibling_sibling.resolve()
            curr = curr.parent
            
    # 3. Fallbacks to Desktop/OneDrive Desktop
    fallbacks = [
        Path(os.path.expanduser("~/Desktop/srujana-memory")),
        Path(os.path.expanduser("~/OneDrive/Desktop/srujana-memory")),
        Path(os.path.expanduser("~/OneDrive - REVA University/Desktop/srujana-memory"))
    ]
    for path in fallbacks:
        if path.exists() and path.is_dir():
            return path.resolve()
            
    return None

def parse_readme_plugins():
    readme_path = REPO_ROOT / "README.md"
    plugins = []
    if not readme_path.exists():
        return plugins
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Split by "### "
    blocks = content.split("### ")
    for block in blocks[1:]:
        lines = block.splitlines()
        if not lines:
            continue
        header = lines[0]
        # Match header like: 🎓 `@reva-scholar` — Faculty Research & PhD Companion
        header_match = re.search(r"`?(@[a-zA-Z0-9_-]+)`?\s*—\s*(.+)", header)
        if not header_match:
            continue
        plugin_name = header_match.group(1).strip()
        plugin_desc = header_match.group(2).strip()
        
        commands = []
        # Parse slash commands under this block
        for line in lines[1:]:
            cmd_match = re.search(r"-\s*`(/?[a-zA-Z0-9_-]+)`\s*:\s*(.+)", line)
            if cmd_match:
                commands.append({
                    "command": cmd_match.group(1).strip(),
                    "description": cmd_match.group(2).strip()
                })
        
        if commands:
            plugins.append({
                "name": plugin_name,
                "description": plugin_desc,
                "commands": commands
            })
            
    return plugins

def read_markdown_file(path, fallback=""):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return fallback

def check_profile_completeness(scholar_path):
    completeness = {
        "score": 0,
        "nudges": [],
        "fields": {
            "name": False,
            "school": False,
            "orcid": False,
            "research_topic": False,
            "sdg_impact": False,
            "provisional_reg_date": False
        }
    }
    
    if not scholar_path.exists():
        completeness["nudges"].append("Scholar profile file not found.")
        return completeness
        
    with open(scholar_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Read name
    name_match = re.search(r"(Name):\s*(.+)", content, re.IGNORECASE)
    if name_match and name_match.group(2).strip() and "your name" not in name_match.group(2).lower() and "full name" not in name_match.group(2).lower():
        completeness["fields"]["name"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Identity: Please set your Name in your profile.")
        
    # School
    school_match = re.search(r"(School):\s*(.+)", content, re.IGNORECASE)
    if school_match and school_match.group(2).strip() and "school of" in school_match.group(2).lower():
        completeness["fields"]["school"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Identity: Declare your School affiliation in your profile.")
        
    # ORCID / ID
    orcid_match = re.search(r"(Registration ID|orcid|id):\s*(.+)", content, re.IGNORECASE)
    if orcid_match and orcid_match.group(2).strip():
        completeness["fields"]["orcid"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Registration: Please enter your Registration ID.")
        
    # Research Topic
    topic_match = re.search(r"(Research Topic|topic):\s*(.+)", content, re.IGNORECASE)
    if topic_match and topic_match.group(2).strip() and len(topic_match.group(2).strip()) > 5:
        completeness["fields"]["research_topic"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Research: Specify your Research Topic in your profile.")
        
    # SDG Impact
    sdg_match = re.search(r"(SDG|sustainable development goals):\s*(.+)", content, re.IGNORECASE)
    if sdg_match and sdg_match.group(2).strip() and re.search(r"\d+", sdg_match.group(2)):
        completeness["fields"]["sdg_impact"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Impact: Define your research's UN SDG impact mappings.")

    # Registration Date
    date_match = re.search(r"(Registration Date|date):\s*(.+)", content, re.IGNORECASE)
    if date_match and date_match.group(2).strip() and re.match(r"^\d{4}-\d{2}-\d{2}$", date_match.group(2).strip()):
        completeness["fields"]["provisional_reg_date"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Milestones: Set a valid Registration Date (YYYY-MM-DD) to run the Milestone Calculator.")

    return completeness

def build_dashboard():
    print("Building SrujanaSangama Scholar Dashboard...")
    memory_dir = locate_srujana_memory()
    if not memory_dir:
        print("[WARNING] srujana-memory directory could not be located. Dashboard generation halted.")
        return
        
    # Try to find the active scholar directory
    scholar_dir = None
    collab_dir = memory_dir / "scholar-guide"
    if collab_dir.exists():
        for item in collab_dir.iterdir():
            if item.is_dir() and item.name.startswith("scholar-"):
                scholar_dir = item
                break
                
    if not scholar_dir:
        print("[WARNING] No scholar-guide subdirectory found. Initializing with empty dashboard.")
        # Fallback to local user soul.md
        scholar_profile_path = memory_dir / "my-memory" / "soul.md"
        scholar_name = "Unknown Scholar"
        scholar_role = "PhD Candidate"
        scholar_school = "School of Computer Science and Engineering"
        scholar_id = "None"
        milestones_content = "No milestones found."
        synopsis_content = "No synopsis found."
        pipeline_content = "No publication pipeline found."
        daily_content = "No daily log found."
    else:
        # Load scholar files
        scholar_profile_path = scholar_dir / "scholar-profile.md"
        if not scholar_profile_path.exists():
            # Try my-memory soul
            scholar_profile_path = memory_dir / "my-memory" / "soul.md"
            
        with open(scholar_profile_path, "r", encoding="utf-8") as f:
            prof_content = f.read()
            
        name_match = re.search(r"Name:\s*(.+)", prof_content, re.IGNORECASE)
        scholar_name = name_match.group(1).strip() if name_match else "Ananya K. Sharma"
        
        reg_match = re.search(r"Registration ID:\s*(.+)", prof_content, re.IGNORECASE)
        scholar_id = reg_match.group(1).strip() if reg_match else "PH0223CSE04"
        
        school_match = re.search(r"School:\s*(.+)", prof_content, re.IGNORECASE)
        scholar_school = school_match.group(1).strip() if school_match else "School of CSE"
        
        stage_match = re.search(r"Current Stage:\s*(.+)", prof_content, re.IGNORECASE)
        scholar_role = stage_match.group(1).strip() if stage_match else "Stage 3 — Active Research"
        
        milestones_content = read_markdown_file(scholar_dir / "milestones.md", "No milestones tracker.")
        synopsis_content = read_markdown_file(scholar_dir / "synopsis-draft.md", "No research synopsis draft.")
        pipeline_content = read_markdown_file(scholar_dir / "publication-pipeline.md", "No publication pipeline tracker.")
        daily_content = read_markdown_file(scholar_dir / "daily-log.md", "No guide catching-up log.")
        
    completeness = check_profile_completeness(scholar_profile_path)
    
    output_data = {
        "generic": {
            "system": "SrujanaSangama",
            "plugins": parse_readme_plugins()
        },
        "personal": {
            "name": scholar_name,
            "role": scholar_role,
            "school": scholar_school,
            "orcid": scholar_id,
            "score": completeness["score"],
            "nudges": completeness["nudges"],
            "fields": completeness["fields"],
            "research_pipeline": synopsis_content,
            "milestones": milestones_content,
            "pipeline": pipeline_content,
            "daily_log": daily_content,
            "collaborations": []
        }
    }
    
    # Add collaborations scan
    if scholar_dir:
        import datetime
        for subitem in scholar_dir.glob("*.md"):
            dt = datetime.datetime.fromtimestamp(subitem.stat().st_mtime).isoformat()
            output_data["personal"]["collaborations"].append({
                "type": "scholar-guide",
                "folder": f"scholar-guide/{scholar_dir.name}",
                "latest_file": subitem.name,
                "last_update": dt
            })
            
    # 1. Write the backup JSON
    dest_json = memory_dir / "my-memory" / "scholar-data.json"
    with open(dest_json, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
        
    # 2. Read HTML template from repository
    template_file = REPO_ROOT / "web" / "scholar_index.html"
    if template_file.exists():
        with open(template_file, "r", encoding="utf-8") as f:
            template_content = f.read()
            
        # Replace the json string placeholder in the template
        embedded_str = json.dumps(output_data, indent=2)
        replaced_content = template_content.replace("/*DASHBOARD_DATA_PLACEHOLDER*/", embedded_str)
        
        dest_html = memory_dir / "my-memory" / "scholar_index.html"
        with open(dest_html, "w", encoding="utf-8") as f:
            f.write(replaced_content)
        print(f"SrujanaSangama Scholar HTML portal written to {dest_html}")
    else:
        print(f"[WARNING] Scholar HTML template not found at {template_file}")

if __name__ == "__main__":
    build_dashboard()
