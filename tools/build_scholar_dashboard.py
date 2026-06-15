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
        
    # 2. Sibling Path (one level up from repo root)
    sibling_path = REPO_ROOT.parent / "srujana-memory"
    if sibling_path.exists():
        return sibling_path.resolve()
        
    # 3. Desktop
    desktop = Path(os.path.expanduser("~/Desktop/srujana-memory"))
    if desktop.exists():
        return desktop.resolve()
        
    # 4. OneDrive Desktop
    onedrive_desktop = Path(os.path.expanduser("~/OneDrive/Desktop/srujana-memory"))
    if onedrive_desktop.exists():
        return onedrive_desktop.resolve()
        
    return None

def parse_readme_commands():
    readme_path = REPO_ROOT / "README.md"
    commands = []
    if not readme_path.exists():
        return commands
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all commands lines matching - `/command` or - `cmd`
    # Let's search using regex
    matches = re.findall(r"-\s*(`/[a-zA-Z0-9_-]+`)\s*:\s*(.+)", content)
    for cmd, desc in matches:
        commands.append({
            "command": cmd.replace("`", ""),
            "description": desc.strip()
        })
        
    # Let's also look for slash command listings
    matches_alt = re.findall(r"-\s*(`gtd`|`gps`|`weekly-review`|`session-close`|`new-skill`|`/onboard`|`/weekly-review`|`/project-kickoff`|`/deep-research`|`/session-close`|`/new-skill`|`/audit`|`/course-check`|`/assessment-check`|`/build-course-buddy`|`/cold-start-interview`|`/socratic-drill`|`/case-brief`|`/outline-builder`|`/aibe-prep`|`/flashcards`|`/study-plan`|`/irac-practice`|`/moot-court-trainer`|`/legal-writing`|`/exam-forecast`|`/session`)\s*:\s*(.+)", content, re.IGNORECASE)
    for cmd, desc in matches_alt:
        commands.append({
            "command": cmd.replace("`", ""),
            "description": desc.strip()
        })
        
    # Remove duplicates
    seen = set()
    unique_commands = []
    for c in commands:
        if c["command"] not in seen:
            seen.add(c["command"])
            unique_commands.append(c)
            
    return unique_commands

def check_profile_completeness(memory_dir):
    soul_path = memory_dir / "my-memory" / "soul.md"
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
    
    if not soul_path.exists():
        completeness["nudges"].append("Create your private profile: 'my-memory/soul.md' is missing.")
        return completeness
        
    with open(soul_path, "r", encoding="utf-8") as f:
        soul_content = f.read()
        
    # Read name
    name_match = re.search(r"(Name|name):\s*(.+)", soul_content, re.IGNORECASE)
    if name_match and name_match.group(2).strip() and "your name" not in name_match.group(2).lower() and "full name" not in name_match.group(2).lower():
        completeness["fields"]["name"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Identity: Please set your Name in your soul.md profile.")
        
    # School
    school_match = re.search(r"(School|school):\s*(.+)", soul_content, re.IGNORECASE)
    if school_match and school_match.group(2).strip() and "school of" in school_match.group(2).lower():
        completeness["fields"]["school"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Identity: Declare your School affiliation in your soul.md profile (e.g. School of Computer Science).")
        
    # ORCID
    orcid_match = re.search(r"(ORCID|orcid):\s*(.+)", soul_content, re.IGNORECASE)
    if orcid_match and orcid_match.group(2).strip() and re.search(r"\d{4}-\d{4}-\d{4}-\d{3}[0-9X]", orcid_match.group(2)):
        completeness["fields"]["orcid"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Research: Link your ORCID iD in your soul.md profile to connect your publications.")
        
    # Research Topic
    topic_match = re.search(r"(Research Topic|topic):\s*(.+)", soul_content, re.IGNORECASE)
    if topic_match and topic_match.group(2).strip() and len(topic_match.group(2).strip()) > 5:
        completeness["fields"]["research_topic"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Research: Specify your Research Topic in your soul.md profile.")
        
    # SDG Impact
    sdg_match = re.search(r"(SDG|sustainable development goals):\s*(.+)", soul_content, re.IGNORECASE)
    if sdg_match and sdg_match.group(2).strip() and re.search(r"\d+", sdg_match.group(2)):
        completeness["fields"]["sdg_impact"] = True
        completeness["score"] += 20
    else:
        completeness["nudges"].append("Impact: Define your research's UN SDG impact mappings in your profile.")

    # Provisional Registration Date
    date_match = re.search(r"(provisional_registration_date|provisional registration date):\s*(.+)", soul_content, re.IGNORECASE)
    if date_match and date_match.group(2).strip() and re.match(r"^\d{4}-\d{2}-\d{2}$", date_match.group(2).strip()):
        completeness["fields"]["provisional_reg_date"] = True
        completeness["score"] += 15
    else:
        completeness["nudges"].append("Milestones: Set a valid Provisional Registration Date (YYYY-MM-DD) in your profile to run the PhD Milestone Calculator.")

    return completeness

def load_extra_personal_data(memory_dir):
    data = {
        "research_pipeline": "No active research objectives or pipeline found. Start research planning to populate.",
        "collaborations": []
    }
    
    # 1. Research Pipeline
    pipeline_path = memory_dir / "my-memory" / "semantic" / "research-pipeline.md"
    if pipeline_path.exists():
        with open(pipeline_path, "r", encoding="utf-8") as f:
            data["research_pipeline"] = f.read()
            
    # 2. Collaborative directories
    collaborative_prefixes = ["scholar-guide", "pi-copi", "guide-team", "reva-smart-campus"]
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
    print("Building SrujanaSangama Dashboard...")
    memory_dir = locate_srujana_memory()
    if not memory_dir:
        print("[WARNING] srujana-memory directory could not be located. Dashboard will show empty profile placeholders.")
        output_data = {
            "generic": {
                "system": "SrujanaSangama",
                "commands": parse_readme_commands()
            },
            "personal": {
                "score": 0,
                "nudges": ["Create the 'srujana-memory' folder on your Desktop or parent directory to initialize profile tracking."],
                "fields": {},
                "research_pipeline": "Please set up srujana-memory to see your active Research Pipeline.",
                "collaborations": []
            }
        }
    else:
        completeness = check_profile_completeness(memory_dir)
        personal_data = load_extra_personal_data(memory_dir)
        
        output_data = {
            "generic": {
                "system": "SrujanaSangama",
                "commands": parse_readme_commands()
            },
            "personal": {
                "score": completeness["score"],
                "nudges": completeness["nudges"],
                "fields": completeness["fields"],
                "research_pipeline": personal_data["research_pipeline"],
                "collaborations": personal_data["collaborations"]
            }
        }
        
    web_dir = REPO_ROOT / "web"
    web_dir.mkdir(exist_ok=True)
    
    with open(web_dir / "scholar-data.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
        
    print(f"SrujanaSangama dashboard data successfully written to {web_dir / 'scholar-data.json'}")

if __name__ == "__main__":
    build_dashboard()
