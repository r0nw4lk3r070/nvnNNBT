"""workspaces.py — Workspace (skill-set) directory listing (Phase 1)."""
from __future__ import annotations

import os
from pathlib import Path

from fastapi import APIRouter

WORKSPACES_ROOT = Path(os.environ.get("WORKSPACES_ROOT", "/app/data/workspaces"))

_IDENTITY_FILES = {"SOUL.md", "AGENTS.md", "TOOLS.md", "HEARTBEAT.md", "USER.md"}

router = APIRouter(prefix="/workspaces", tags=["workspaces"])


@router.get("")
async def list_workspaces() -> dict:
    """
    List all workspace directories under WORKSPACES_ROOT.
    Returns slug, display name, which identity files are present, and skill count.
    """
    workspaces = []
    if WORKSPACES_ROOT.exists():
        for entry in sorted(WORKSPACES_ROOT.iterdir()):
            if not entry.is_dir() or entry.name.startswith("."):
                continue
            try:
                files = [f.name for f in entry.iterdir() if f.is_file()]
            except PermissionError:
                continue
            skills_dir = entry / "skills"
            skill_count = 0
            if skills_dir.exists():
                try:
                    skill_count = sum(1 for s in skills_dir.iterdir() if s.is_dir())
                except PermissionError:
                    pass
            workspaces.append({
                "slug":           entry.name,
                "name":           entry.name.replace("-", " ").title(),
                "identity_files": [f for f in files if f in _IDENTITY_FILES],
                "skill_count":    skill_count,
            })
    return {"workspaces": workspaces, "root": str(WORKSPACES_ROOT)}
