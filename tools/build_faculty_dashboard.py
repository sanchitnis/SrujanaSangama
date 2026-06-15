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

def check_profile_completeness(memory_dir):
    soul_path = memory_dir / "my-memory" / "soul.md"
    completeness = {
        "score": 0,
        "nudges": [],
        "fields": {
            "name": False,
            "school": False,
            "orcid": False,
            "research_interests": False,
            "sdg_impact": False
        }
    }
    
    if not soul_path.exists():
        completeness["nudges"].append("Create your private profile: 'my-memory/soul.md' is missing.")
        return completeness
        
    with open(soul_path, "r", encoding="utf-8") as f:
        soul_content = f.read()
        
    # Read name
    name_match = re.search(r"(Name|name):\s*(.+)", soul_content, re.IGNORECASE)
    if name_match and name_match.group(2).strip() and "your name" not in name_match.group(2).lower() and "full name" not in name_match.group(2).lower():
        completeness["fields"]["name"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Identity: Please set your Name in your soul.md profile.")
        
    # School
    school_match = re.search(r"(School|school):\s*(.+)", soul_content, re.IGNORECASE)
    if school_match and school_match.group(2).strip() and "school of" in school_match.group(2).lower():
        completeness["fields"]["school"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Identity: Declare your School affiliation in your soul.md profile.")
        
    # ORCID
    orcid_match = re.search(r"(ORCID|orcid):\s*(.+)", soul_content, re.IGNORECASE)
    if orcid_match and orcid_match.group(2).strip() and re.search(r"\d{4}-\d{4}-\d{4}-\d{3}[0-9X]", orcid_match.group(2)):
        completeness["fields"]["orcid"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Research: Link your ORCID iD in your soul.md profile.")
        
    # Research Interests / Domains
    interests_match = re.search(r"(Research Interests|interests|domain_tags):\s*(.+)", soul_content, re.IGNORECASE)
    if interests_match and interests_match.group(2).strip():
        completeness["fields"]["research_interests"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Research: Specify your primary Research Interests in your soul.md profile.")
        
    # SDG Impact
    sdg_match = re.search(r"(SDG|sustainable development goals):\s*(.+)", soul_content, re.IGNORECASE)
    if sdg_match and sdg_match.group(2).strip() and re.search(r"\d+", sdg_match.group(2)):
        completeness["fields"]["sdg_impact"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Impact: Map your faculty research areas to UN SDGs in your profile.")

    return completeness

def parse_soul_metadata(soul_path):
    metadata = {
        "name": "Unknown Faculty",
        "role": "Faculty Member",
        "school": "School of Computer Science and Engineering",
        "orcid": "None",
        "user_type": "faculty"
    }
    if not soul_path.exists():
        return metadata
        
    with open(soul_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    name_match = re.search(r"Name:\s*(.+)", content, re.IGNORECASE)
    if name_match:
        metadata["name"] = name_match.group(1).strip()
        
    title_match = re.search(r"(Academic Title|Title|role):\s*(.+)", content, re.IGNORECASE)
    if title_match:
        metadata["role"] = title_match.group(2).strip()
        
    school_match = re.search(r"School:\s*(.+)", content, re.IGNORECASE)
    if school_match:
        metadata["school"] = school_match.group(1).strip()
        
    orcid_match = re.search(r"ORCID:\s*(.+)", content, re.IGNORECASE)
    if orcid_match:
        metadata["orcid"] = orcid_match.group(1).strip()
        
    type_match = re.search(r"(User Type|type):\s*(.+)", content, re.IGNORECASE)
    if type_match:
        metadata["user_type"] = type_match.group(2).strip()
        
    return metadata

def read_markdown_file(path, fallback=""):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return fallback

def load_extra_personal_data(memory_dir):
    data = {
        "active_project": "No active projects or KRA milestones found. Start a project kickoff to populate.",
        "collaborations": []
    }
    
    # 1. Active Project
    proj_path = memory_dir / "my-memory" / "context" / "active-project.md"
    if proj_path.exists():
        with open(proj_path, "r", encoding="utf-8") as f:
            data["active_project"] = f.read()
            
    # 2. Collaborative directories
    collaborative_prefixes = ["pi-copi", "guide-team", "reva-smart-campus"]
    for prefix in collaborative_prefixes:
        collab_dir = memory_dir / prefix
        if collab_dir.exists():
            for item in collab_dir.iterdir():
                if item.is_dir():
                    latest_mtime = 0
                    latest_file = ""
                    for subitem in item.glob("*.md"):
                        mtime = subitem.stat().st_mtime
                        if mtime > latest_mtime:
                            latest_mtime = mtime
                            latest_file = subitem.name
                    if latest_file:
                        import datetime
                        dt = datetime.datetime.fromtimestamp(latest_mtime).isoformat()
                        data["collaborations"].append({
                            "type": prefix,
                            "folder": f"{prefix}/{item.name}",
                            "latest_file": latest_file,
                            "last_update": dt
                        })
                        
    return data

def build_dashboard():
    print("Building SrujanaSangama Faculty Dashboard...")
    memory_dir = locate_srujana_memory()
    if not memory_dir:
        print("[WARNING] srujana-memory directory could not be located. Dashboard generation halted.")
        return
        
    completeness = check_profile_completeness(memory_dir)
    personal_data = load_extra_personal_data(memory_dir)
    soul_meta = parse_soul_metadata(memory_dir / "my-memory" / "soul.md")
    
    # Paths for other semantic logs
    publications_path = memory_dir / "my-memory" / "semantic" / "publications.md"
    funding_path = memory_dir / "my-memory" / "semantic" / "funding-log.md"
    recent_path = memory_dir / "my-memory" / "episodic" / "recent.md"
    brand_path = memory_dir / "my-memory" / "semantic" / "brand-profile.md"
    
    output_data = {
        "generic": {
            "system": "SrujanaSangama",
            "plugins": parse_readme_plugins()
        },
        "personal": {
            "name": soul_meta["name"],
            "role": soul_meta["role"],
            "school": soul_meta["school"],
            "orcid": soul_meta["orcid"],
            "score": completeness["score"],
            "nudges": completeness["nudges"],
            "fields": completeness["fields"],
            "active_project": personal_data["active_project"],
            "collaborations": personal_data["collaborations"],
            "publications": read_markdown_file(publications_path, "No publications found."),
            "funding": read_markdown_file(funding_path, "No active funding log found."),
            "recent": read_markdown_file(recent_path, "No recent sessions logged."),
            "brand": read_markdown_file(brand_path, "No brand profile found.")
        }
    }
    
    # 1. Write the backup JSON
    dest_json = memory_dir / "my-memory" / "faculty-data.json"
    with open(dest_json, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
        
    # 2. Read HTML template from repository
    template_file = REPO_ROOT / "web" / "faculty_index.html"
    if template_file.exists():
        with open(template_file, "r", encoding="utf-8") as f:
            template_content = f.read()
            
        # Replace the json string placeholder in the template
        embedded_str = json.dumps(output_data, indent=2)
        replaced_content = template_content.replace("/*DASHBOARD_DATA_PLACEHOLDER*/", embedded_str)
        
        dest_html = memory_dir / "my-memory" / "faculty_index.html"
        with open(dest_html, "w", encoding="utf-8") as f:
            f.write(replaced_content)
        print(f"SrujanaSangama Faculty HTML portal written to {dest_html}")
    else:
        print(f"[WARNING] Faculty HTML template not found at {template_file}")

if __name__ == "__main__":
    build_dashboard()
