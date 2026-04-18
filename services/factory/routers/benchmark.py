"""benchmark.py — Workspace versioning, task sets, LLM-as-judge benchmark runs."""
from __future__ import annotations

import json
import os
import time
import uuid
from pathlib import Path
from typing import Optional

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database import DB_PATH, get_conn
from routers.events import log_event

router = APIRouter(prefix="/benchmark", tags=["benchmark"])

WORKSPACES_ROOT = Path(os.environ.get("WORKSPACES_ROOT", "/app/data/workspaces"))
OLLAMA_URL      = os.environ.get("OLLAMA_BASE_URL", "http://host.docker.internal:11434")

# ── Models ────────────────────────────────────────────────────────────────────

class TagWorkspaceBody(BaseModel):
    workspace_slug: str
    tag: str
    notes: str = ""


class TaskItem(BaseModel):
    id: str
    input: str
    criteria: str          # what a good answer should contain/demonstrate


class SaveTaskSetBody(BaseModel):
    workspace_slug: str
    name: str              # filename slug, e.g. "basic-qa"
    tasks: list[TaskItem]


class RunBenchmarkBody(BaseModel):
    workspace_slug: str
    task_set_name: str
    model: str             # model for the agent under test
    judge_model: str       # model for LLM-as-judge
    version_tag: str = ""  # optional — records which version this run is for


# ── Workspace versioning ──────────────────────────────────────────────────────

@router.get("/versions/{workspace_slug}")
async def list_versions(workspace_slug: str) -> dict:
    with get_conn(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT id, tag, commit_hash, notes, created_at "
            "FROM workspace_versions WHERE workspace_slug=? ORDER BY id DESC",
            (workspace_slug,),
        ).fetchall()
    return {"versions": [dict(r) for r in rows]}


@router.post("/versions")
async def tag_workspace(body: TagWorkspaceBody) -> dict:
    ws_path = WORKSPACES_ROOT / body.workspace_slug
    if not ws_path.exists():
        raise HTTPException(status_code=404, detail=f"Workspace '{body.workspace_slug}' not found")

    # Try to read git hash from workspace (best-effort)
    commit_hash = ""
    try:
        import subprocess
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(ws_path), capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0:
            commit_hash = result.stdout.strip()[:12]
    except Exception:
        pass

    with get_conn(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO workspace_versions (workspace_slug, tag, commit_hash, notes, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (body.workspace_slug, body.tag, commit_hash, body.notes, int(time.time())),
        )

    log_event("workspace_tag", target_type="workspace", target_slug=body.workspace_slug,
              detail=f"Tagged '{body.workspace_slug}' as '{body.tag}'")
    return {"ok": True, "workspace_slug": body.workspace_slug, "tag": body.tag, "commit_hash": commit_hash}


# ── Task sets ─────────────────────────────────────────────────────────────────

def _task_set_path(workspace_slug: str, name: str) -> Path:
    return WORKSPACES_ROOT / workspace_slug / "benchmark" / f"{name}.json"


@router.get("/task-sets/{workspace_slug}")
async def list_task_sets(workspace_slug: str) -> dict:
    bench_dir = WORKSPACES_ROOT / workspace_slug / "benchmark"
    if not bench_dir.exists():
        return {"task_sets": []}
    sets = []
    for f in sorted(bench_dir.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            sets.append({
                "name":       f.stem,
                "task_count": len(data.get("tasks", [])),
                "updated_at": int(f.stat().st_mtime),
            })
        except Exception:
            pass
    return {"task_sets": sets}


@router.get("/task-sets/{workspace_slug}/{name}")
async def get_task_set(workspace_slug: str, name: str) -> dict:
    p = _task_set_path(workspace_slug, name)
    if not p.exists():
        raise HTTPException(status_code=404, detail=f"Task set '{name}' not found")
    return json.loads(p.read_text(encoding="utf-8"))


@router.post("/task-sets")
async def save_task_set(body: SaveTaskSetBody) -> dict:
    if not body.tasks:
        raise HTTPException(status_code=400, detail="Task set must have at least one task")
    ws_path = WORKSPACES_ROOT / body.workspace_slug
    if not ws_path.exists():
        raise HTTPException(status_code=404, detail=f"Workspace '{body.workspace_slug}' not found")

    bench_dir = ws_path / "benchmark"
    bench_dir.mkdir(exist_ok=True)
    p = bench_dir / f"{body.name}.json"
    p.write_text(
        json.dumps({
            "name": body.name,
            "workspace_slug": body.workspace_slug,
            "tasks": [t.model_dump() for t in body.tasks],
            "updated_at": int(time.time()),
        }, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return {"ok": True, "name": body.name, "task_count": len(body.tasks)}


@router.delete("/task-sets/{workspace_slug}/{name}")
async def delete_task_set(workspace_slug: str, name: str) -> dict:
    p = _task_set_path(workspace_slug, name)
    if not p.exists():
        raise HTTPException(status_code=404, detail=f"Task set '{name}' not found")
    p.unlink()
    return {"ok": True}


# ── Benchmark runs ────────────────────────────────────────────────────────────

@router.get("/runs")
async def list_runs(workspace_slug: str = "") -> dict:
    with get_conn(DB_PATH) as conn:
        if workspace_slug:
            rows = conn.execute(
                "SELECT id, workspace_slug, task_set_name, model, judge_model, "
                "workspace_version_tag, score, created_at, completed_at "
                "FROM benchmark_runs WHERE workspace_slug=? ORDER BY created_at DESC LIMIT 50",
                (workspace_slug,),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT id, workspace_slug, task_set_name, model, judge_model, "
                "workspace_version_tag, score, created_at, completed_at "
                "FROM benchmark_runs ORDER BY created_at DESC LIMIT 50",
            ).fetchall()
    return {"runs": [dict(r) for r in rows]}


@router.get("/runs/{run_id}")
async def get_run(run_id: str) -> dict:
    with get_conn(DB_PATH) as conn:
        run = conn.execute("SELECT * FROM benchmark_runs WHERE id=?", (run_id,)).fetchone()
        if not run:
            raise HTTPException(status_code=404, detail="Run not found")
        results = conn.execute(
            "SELECT task_id, input, response, score, judge_reason FROM benchmark_results WHERE run_id=?",
            (run_id,),
        ).fetchall()
    return {"run": dict(run), "results": [dict(r) for r in results]}


async def _call_ollama(model: str, prompt: str, timeout: int = 120) -> str:
    """Call Ollama chat endpoint and return the assistant response text."""
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }
    async with httpx.AsyncClient(timeout=timeout) as client:
        r = await client.post(f"{OLLAMA_URL}/api/chat", json=payload)
        r.raise_for_status()
        data = r.json()
        return data.get("message", {}).get("content", "").strip()


async def _judge_response(judge_model: str, task_input: str, criteria: str, response: str) -> tuple[float, str]:
    """Ask the judge model to score a response 0-10. Returns (score, reason)."""
    prompt = f"""You are an objective evaluator. Score the following agent response on a scale from 0 to 10.

Task given to agent:
{task_input}

Evaluation criteria:
{criteria}

Agent response:
{response}

Reply with ONLY a JSON object in this exact format (no extra text):
{{"score": <number 0-10>, "reason": "<one sentence explanation>"}}"""

    try:
        raw = await _call_ollama(judge_model, prompt, timeout=60)
        # Extract JSON even if model adds extra text
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start >= 0 and end > start:
            data = json.loads(raw[start:end])
            score = float(data.get("score", 0))
            score = max(0.0, min(10.0, score))
            reason = str(data.get("reason", ""))
            return score, reason
    except Exception as e:
        return 0.0, f"Judge error: {e}"
    return 0.0, "Could not parse judge response"


@router.post("/runs")
async def run_benchmark(body: RunBenchmarkBody) -> dict:
    """Run all tasks in a task set, score with LLM-as-judge, store results."""
    p = _task_set_path(body.workspace_slug, body.task_set_name)
    if not p.exists():
        raise HTTPException(status_code=404,
                            detail=f"Task set '{body.task_set_name}' not found for workspace '{body.workspace_slug}'")

    task_set = json.loads(p.read_text(encoding="utf-8"))
    tasks = task_set.get("tasks", [])
    if not tasks:
        raise HTTPException(status_code=400, detail="Task set is empty")

    run_id = str(uuid.uuid4())[:8]
    created_at = int(time.time())

    with get_conn(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO benchmark_runs "
            "(id, workspace_slug, workspace_version_tag, task_set_name, model, judge_model, score, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, 0, ?)",
            (run_id, body.workspace_slug, body.version_tag,
             body.task_set_name, body.model, body.judge_model, created_at),
        )

    log_event("benchmark_start", target_type="workspace", target_slug=body.workspace_slug,
              detail=f"Run {run_id}: {len(tasks)} tasks, model={body.model}, judge={body.judge_model}")

    total_score = 0.0
    results = []

    for task in tasks:
        task_input = task.get("input", "")
        criteria   = task.get("criteria", "")
        task_id    = task.get("id", "")

        # Get agent response
        try:
            response = await _call_ollama(body.model, task_input, timeout=120)
        except Exception as e:
            response = f"[ERROR: {e}]"

        # Judge the response
        score, reason = await _judge_response(body.judge_model, task_input, criteria, response)
        total_score += score

        with get_conn(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO benchmark_results (run_id, task_id, input, response, score, judge_reason) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (run_id, task_id, task_input, response, score, reason),
            )
        results.append({"task_id": task_id, "score": score, "reason": reason})

    avg_score = total_score / len(tasks) if tasks else 0.0
    completed_at = int(time.time())

    with get_conn(DB_PATH) as conn:
        conn.execute(
            "UPDATE benchmark_runs SET score=?, completed_at=? WHERE id=?",
            (round(avg_score, 2), completed_at, run_id),
        )

    log_event("benchmark_complete", target_type="workspace", target_slug=body.workspace_slug,
              detail=f"Run {run_id} complete. Avg score: {avg_score:.1f}/10")

    return {
        "ok":        True,
        "run_id":    run_id,
        "avg_score": round(avg_score, 2),
        "results":   results,
    }
