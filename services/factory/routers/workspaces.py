"""workspaces.py — Workspace (skill-set) CRUD, file editor, skills, git versioning."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from routers.events import log_event

# ── Config ────────────────────────────────────────────────────────────────────
WORKSPACES_ROOT = Path(os.environ.get("WORKSPACES_ROOT", "/app/data/workspaces"))

_IDENTITY_FILES = ["SOUL.md", "AGENTS.md", "TOOLS.md", "HEARTBEAT.md", "USER.md"]
_SLUG_RE        = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")

router = APIRouter(prefix="/workspaces", tags=["workspaces"])


# ── Helpers ───────────────────────────────────────────────────────────────────

def _ws_path(slug: str) -> Path:
    p = WORKSPACES_ROOT / slug
    if not p.exists():
        raise HTTPException(status_code=404, detail=f"Workspace '{slug}' not found")
    return p


def _git(ws: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=ws,
        capture_output=True, text=True,
    )


def _git_init(ws: Path) -> None:
    _git(ws, "init")
    _git(ws, "config", "user.email", "factory@nvnnnbt")
    _git(ws, "config", "user.name", "Agent Factory")
    (ws / ".gitignore").write_text(
        "knowledge/vectors.db\nmemory/MEMORY.md\nsessions/\ncron/jobs.json\n",
        encoding="utf-8",
    )
    _git(ws, "add", "-A")
    _git(ws, "commit", "-m", "init: workspace created")


def _git_commit(ws: Path, msg: str) -> None:
    _git(ws, "add", "-A")
    _git(ws, "commit", "-m", msg)


def _workspace_summary(entry: Path) -> dict:
    try:
        files = [f.name for f in entry.iterdir() if f.is_file()]
    except PermissionError:
        files = []
    skills_dir = entry / "skills"
    skill_count = 0
    if skills_dir.exists():
        try:
            skill_count = sum(1 for s in skills_dir.iterdir() if s.is_dir())
        except PermissionError:
            pass
    return {
        "slug":           entry.name,
        "name":           entry.name.replace("-", " ").title(),
        "identity_files": [f for f in files if f in _IDENTITY_FILES],
        "skill_count":    skill_count,
    }


# ── List workspaces ───────────────────────────────────────────────────────────

@router.get("")
async def list_workspaces() -> dict:
    workspaces = []
    if WORKSPACES_ROOT.exists():
        for entry in sorted(WORKSPACES_ROOT.iterdir()):
            if not entry.is_dir() or entry.name.startswith("."):
                continue
            workspaces.append(_workspace_summary(entry))
    return {"workspaces": workspaces, "root": str(WORKSPACES_ROOT)}


# ── Get workspace detail ──────────────────────────────────────────────────────

@router.get("/{slug}")
async def get_workspace(slug: str) -> dict:
    ws = _ws_path(slug)
    summary = _workspace_summary(ws)
    files = {}
    for fname in _IDENTITY_FILES:
        fp = ws / fname
        files[fname] = fp.read_text(encoding="utf-8") if fp.exists() else ""
    summary["files"] = files
    return summary


# ── Create workspace ──────────────────────────────────────────────────────────

class CreateWorkspaceBody(BaseModel):
    slug: str
    name: Optional[str] = None


@router.post("")
async def create_workspace(body: CreateWorkspaceBody) -> dict:
    if not _SLUG_RE.match(body.slug):
        raise HTTPException(status_code=400, detail="Invalid slug — lowercase letters, numbers, hyphens, underscores only")
    ws = WORKSPACES_ROOT / body.slug
    if ws.exists():
        raise HTTPException(status_code=409, detail=f"Workspace '{body.slug}' already exists")

    template = WORKSPACES_ROOT / "_template"
    if template.exists():
        shutil.copytree(template, ws, dirs_exist_ok=False,
                        ignore=shutil.ignore_patterns(".git", "*.db", "sessions", "memory"))
    else:
        ws.mkdir(parents=True)
        for fname in _IDENTITY_FILES:
            (ws / fname).write_text(f"# {fname}\n", encoding="utf-8")

    for subdir in ("skills", "knowledge/inbox", "knowledge/library",
                   "memory", "sessions", "benchmarks", "cron"):
        (ws / subdir).mkdir(parents=True, exist_ok=True)
    (ws / "memory" / "MEMORY.md").touch(exist_ok=True)

    _git_init(ws)
    log_event("workspace_save", target_type="workspace", target_slug=body.slug,
              detail=f"Workspace '{body.slug}' created")
    return {"ok": True, "slug": body.slug}


# ── Delete workspace ──────────────────────────────────────────────────────────

@router.delete("/{slug}")
async def delete_workspace(slug: str) -> dict:
    if slug == "_template":
        raise HTTPException(status_code=403, detail="Cannot delete _template")
    ws = _ws_path(slug)
    shutil.rmtree(ws)
    log_event("workspace_save", target_type="workspace", target_slug=slug,
              detail=f"Workspace '{slug}' deleted")
    return {"ok": True}


# ── Save identity file ────────────────────────────────────────────────────────

class SaveFileBody(BaseModel):
    content: str


@router.put("/{slug}/files/{filename}")
async def save_file(slug: str, filename: str, body: SaveFileBody) -> dict:
    ws = _ws_path(slug)
    if filename not in _IDENTITY_FILES:
        raise HTTPException(status_code=400, detail=f"'{filename}' is not an editable identity file")
    (ws / filename).write_text(body.content, encoding="utf-8")
    _git_commit(ws, f"save: {filename}")
    log_event("workspace_save", target_type="workspace", target_slug=slug,
              detail=f"Saved {filename}")
    return {"ok": True}


# ── Skills ────────────────────────────────────────────────────────────────────

@router.get("/{slug}/skills")
async def list_skills(slug: str) -> dict:
    ws = _ws_path(slug)
    skills_dir = ws / "skills"
    skills = []
    if skills_dir.exists():
        for entry in sorted(skills_dir.iterdir()):
            if entry.is_dir():
                skill_file = entry / "SKILL.md"
                skills.append({
                    "name":    entry.name,
                    "content": skill_file.read_text(encoding="utf-8") if skill_file.exists() else "",
                })
    return {"skills": skills}


class SaveSkillBody(BaseModel):
    content: str


@router.put("/{slug}/skills/{skill_name}")
async def save_skill(slug: str, skill_name: str, body: SaveSkillBody) -> dict:
    ws = _ws_path(slug)
    if not re.match(r"^[a-z0-9][a-z0-9_-]{0,63}$", skill_name):
        raise HTTPException(status_code=400, detail="Invalid skill name")
    skill_dir = ws / "skills" / skill_name
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(body.content, encoding="utf-8")
    _git_commit(ws, f"save: skills/{skill_name}/SKILL.md")
    log_event("workspace_save", target_type="workspace", target_slug=slug,
              detail=f"Saved skill '{skill_name}'")
    return {"ok": True}


@router.delete("/{slug}/skills/{skill_name}")
async def delete_skill(slug: str, skill_name: str) -> dict:
    ws = _ws_path(slug)
    skill_dir = ws / "skills" / skill_name
    if not skill_dir.exists():
        raise HTTPException(status_code=404, detail=f"Skill '{skill_name}' not found")
    shutil.rmtree(skill_dir)
    _git_commit(ws, f"delete: skills/{skill_name}")
    return {"ok": True}


# ── Version control ───────────────────────────────────────────────────────────

@router.get("/{slug}/versions")
async def list_versions(slug: str) -> dict:
    ws = _ws_path(slug)
    result = _git(ws, "tag", "--sort=-creatordate",
                  "--format=%(refname:short)|%(subject)|%(creatordate:short)")
    tags = []
    for line in result.stdout.strip().splitlines():
        if "|" in line:
            parts = line.split("|", 2)
            tags.append({"tag": parts[0], "notes": parts[1],
                         "date": parts[2] if len(parts) > 2 else ""})
    return {"versions": tags}


class TagVersionBody(BaseModel):
    tag: str
    notes: Optional[str] = ""


@router.post("/{slug}/versions")
async def tag_version(slug: str, body: TagVersionBody) -> dict:
    ws = _ws_path(slug)
    if not re.match(r"^v\d+\.\d+(\.\d+)?$", body.tag):
        raise HTTPException(status_code=400, detail="Tag must match vX.Y or vX.Y.Z")
    _git_commit(ws, f"pre-tag: {body.tag}")
    result = _git(ws, "tag", body.tag, "-m", body.notes or body.tag)
    if result.returncode != 0:
        raise HTTPException(status_code=400, detail=result.stderr.strip())
    log_event("workspace_version_tag", target_type="workspace", target_slug=slug,
              detail=f"Tagged {body.tag}: {body.notes}")
    return {"ok": True, "tag": body.tag}


class RestoreVersionBody(BaseModel):
    tag: str


@router.post("/{slug}/restore")
async def restore_version(slug: str, body: RestoreVersionBody) -> dict:
    ws = _ws_path(slug)
    result = _git(ws, "checkout", body.tag, "--", ".")
    if result.returncode != 0:
        raise HTTPException(status_code=400, detail=result.stderr.strip())
    _git_commit(ws, f"restore: {body.tag}")
    log_event("workspace_restore", target_type="workspace", target_slug=slug,
              detail=f"Restored to {body.tag}")
    return {"ok": True}
