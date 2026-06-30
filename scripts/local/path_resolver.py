import os
import sys
from pathlib import Path

# Resolve base directories
# This script is located in SrujanaSangama/scripts/local/path_resolver.py
BASE = Path(__file__).parent.parent.parent.resolve()  # Repository root: SrujanaSangama
WORKSPACE_ROOT = BASE

def get_srujana_memory_dir():
    # 1. Check environment variable
    env_dir = os.environ.get("SRUJANA_MEMORY_DIR")
    if env_dir:
        p = Path(env_dir)
        if p.exists():
            return p.resolve()
            
    # 2. Check sibling path in workspace (standard local checkout)
    sibling_dir = WORKSPACE_ROOT.parent / "srujana-memory"
    if sibling_dir.exists():
        return sibling_dir.resolve()
        
    # 3. Check desktop paths
    desktop = Path(os.path.expanduser("~/Desktop"))
    desktop_dir = desktop / "srujana-memory"
    if desktop_dir.exists():
        return desktop_dir.resolve()
        
    # OneDrive Desktop
    onedrive_desktop = Path(os.path.expanduser("~/OneDrive/Desktop"))
    onedrive_desktop_dir = onedrive_desktop / "srujana-memory"
    if onedrive_desktop_dir.exists():
        return onedrive_desktop_dir.resolve()
        
    # No fallback! Exit with error.
    print("\n[ERROR] Srujana Memory Folder ('srujana-memory') not found!")
    print("Each user must create 'srujana-memory' outside the Git repository.")
    print("Please create the folder in one of the following locations:")
    print(f"  1. As a sibling folder:  {sibling_dir}")
    print(f"  2. On your Desktop:      {desktop_dir}")
    print("  3. Set environment var:  SRUJANA_MEMORY_DIR=<path_to_folder>")
    print("\nRefer to the README.md for workspace configuration details.\n")
    sys.exit(1)

def get_private_dir():
    d = get_srujana_memory_dir() / "my-memory"
    d.mkdir(parents=True, exist_ok=True)
    return d

def get_public_dir():
    d = get_srujana_memory_dir() / "public-memory"
    d.mkdir(parents=True, exist_ok=True)
    return d

def get_collaborative_dir(sub=None):
    d = get_srujana_memory_dir()
    if sub:
        d = d / sub
        d.mkdir(parents=True, exist_ok=True)
    return d

def get_reva_info_dir():
    sibling_info = WORKSPACE_ROOT.parent / "reva-information"
    if not sibling_info.exists():
        print(f"\n[ERROR] REVA Information Folder ('reva-information') not found!")
        print(f"Please create the folder at: {sibling_info}")
        print("This folder should contain public REVA University information in markdown format.\n")
        sys.exit(1)
    return sibling_info.resolve()

def resolve_path(rel):
    """
    Resolves relative path inside the centralized memory structure.
    If the relative path starts with 'memory/', strip and place it inside 'my-memory/'.
    If the relative path starts with 'context/', place it inside 'my-memory/context/'.
    If it starts with 'my-memory/', 'public-memory/', or 'collaborations/', resolve directly in the memory folder.
    Otherwise, resolve relative to the repository root (BASE).
    """
    memory_dir = get_srujana_memory_dir()
    private_dir = get_private_dir()
    
    if rel.startswith("memory/"):
        subpath = Path(rel).relative_to("memory")
        return private_dir / subpath
    elif rel.startswith("context/"):
        return private_dir / rel
    elif rel.startswith("my-memory/") or rel.startswith("public-memory/") or rel.startswith("collaborations/"):
        return memory_dir / rel
    else:
        return BASE / rel
