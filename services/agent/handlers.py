"""handlers.py — All HTTP request handlers for Art."""
from __future__ import annotations

import asyncio
import datetime
import json
import re
import time
import uuid

import aiohttp
from aiohttp import web
from loguru import logger

import state
import agent as _agent_mod
from html_art import _build_art_html
from html_lab import _build_lab_html
from html_agent import _build_agent_html


# ── Small utilities ──────────────────────────────────────────────────────────

def _new_id() -> str:
    return uuid.uuid4().hex[:12]


def _auto_title(messages: list) -> str:
    for m in messages:
        if m.get("role") == "user":
            text = re.sub(r"\[Attached file:[^\]]*\]", "", str(m.get("content", ""))).strip()
            return (text[:45] + "\u2026") if len(text) > 45 else (text or "Untitled")
    return "Untitled"


# ── Core page handlers ───────────────────────────────────────────────────────

async def handle_index(_: web.Request) -> web.Response:
    if state.AGENT_MODE == "production":
        html = _build_agent_html()
    else:
        html = _build_art_html()
    return web.Response(text=html, content_type="text/html")


async def handle_health(_: web.Request) -> web.Response:
    return web.Response(text="ok")


async def handle_chat(request: web.Request) -> web.StreamResponse:
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")

    messages = body.get("messages") or []
    last_user = next(
        (m["content"] for m in reversed(messages) if m.get("role") == "user"),
        None,
    )
    if not last_user:
        return web.Response(status=400, text="no user message")

    resp = web.StreamResponse(headers={
        "Content-Type":  "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection":    "keep-alive",
        "Access-Control-Allow-Origin": "*",
    })
    await resp.prepare(request)

    async def on_stream(delta: str) -> None:
        try:
            payload = json.dumps({"choices": [{"delta": {"content": delta}}]})
            await resp.write(f"data: {payload}\n\n".encode())
        except (ConnectionResetError, Exception) as _e:
            if "closing transport" in str(_e) or "ConnectionReset" in type(_e).__name__:
                return
            raise

    if state._agent is None:
        err = json.dumps({"error": "Agent not ready yet, try again in a moment."})
        await resp.write(f"data: {err}\n\n".encode())
        await resp.write(b"data: [DONE]\n\n")
        return resp

    try:
        state._chat_task = asyncio.ensure_future(state._agent.process_direct(
            last_user,
            session_key = state.SESSION_KEY,
            channel     = state.CHANNEL,
            chat_id     = state.CHAT_ID,
            on_stream   = on_stream,
        ))
        await state._chat_task
    except asyncio.CancelledError:
        await resp.write(b"data: [DONE]\n\n")
    except Exception as e:
        logger.error("chat error: {}", e)
        err = json.dumps({"error": str(e)})
        try:
            await resp.write(f"data: {err}\n\n".encode())
        except Exception:
            pass
    finally:
        state._chat_task = None

    try:
        await resp.write(b"data: [DONE]\n\n")
        await resp.write_eof()
    except Exception:
        pass
    return resp


async def handle_stop(_: web.Request) -> web.Response:
    if state._chat_task and not state._chat_task.done():
        state._chat_task.cancel()
    return web.json_response({"ok": True})


async def handle_lab_stop(_: web.Request) -> web.Response:
    if state._lab_task and not state._lab_task.done():
        state._lab_task.cancel()
    return web.json_response({"ok": True})


async def handle_lab_index(_: web.Request) -> web.Response:
    html = _build_lab_html()
    return web.Response(text=html, content_type="text/html")


async def handle_lab_chat(request: web.Request) -> web.StreamResponse:
    if state._lab_agent is None:
        return web.Response(status=400, text="no skill-set loaded")

    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")

    messages = body.get("messages") or []
    last_user = next(
        (m["content"] for m in reversed(messages) if m.get("role") == "user"),
        None,
    )
    if not last_user:
        return web.Response(status=400, text="no user message")

    resp = web.StreamResponse(headers={
        "Content-Type":  "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection":    "keep-alive",
        "Access-Control-Allow-Origin": "*",
    })
    await resp.prepare(request)

    async def on_stream(delta: str) -> None:
        try:
            payload = json.dumps({"choices": [{"delta": {"content": delta}}]})
            await resp.write(f"data: {payload}\n\n".encode())
        except (ConnectionResetError, Exception) as _e:
            if "closing transport" in str(_e) or "ConnectionReset" in type(_e).__name__:
                return
            raise

    try:
        state._lab_task = asyncio.ensure_future(state._lab_agent.process_direct(
            last_user,
            session_key = f"lab:{state._lab_name}",
            channel     = "web",
            chat_id     = state._lab_name,
            on_stream   = on_stream,
        ))
        await state._lab_task
    except asyncio.CancelledError:
        await resp.write(b"data: [DONE]\n\n")
    except Exception as e:
        logger.error("lab chat error: {}", e)
        err = json.dumps({"error": str(e)})
        try:
            await resp.write(f"data: {err}\n\n".encode())
        except Exception:
            pass
    finally:
        state._lab_task = None

    try:
        await resp.write(b"data: [DONE]\n\n")
        await resp.write_eof()
    except Exception:
        pass
    return resp


async def handle_skillsets(_: web.Request) -> web.Response:
    """List available skill-sets with their files."""
    sets = []
    if state.SKILLSETS_DIR.exists():
        for folder in sorted(state.SKILLSETS_DIR.iterdir()):
            if not folder.is_dir():
                continue
            files = []
            for f in sorted(folder.rglob("*.md")):
                files.append(str(f.relative_to(folder)))
            sets.append({"name": folder.name, "files": files})
    return web.json_response({"skillsets": sets})


async def handle_lab_load(request: web.Request) -> web.Response:
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")

    name  = (body.get("name")  or "").strip()
    model = (body.get("model") or "").strip()
    if not name or not model:
        return web.Response(status=400, text="name and model required")

    workspace = state.SKILLSETS_DIR / name
    if not workspace.exists():
        return web.Response(status=404, text=f"skill-set '{name}' not found")

    # Teardown existing
    if state._lab_cron:
        try: state._lab_cron.stop()
        except Exception: pass
    if state._lab_agent:
        try: state._lab_agent.stop()
        except Exception: pass

    try:
        state._lab_agent, state._lab_cron = await _agent_mod._build_skillset_agent(workspace, model)
        state._lab_name  = name
        state._lab_model = model
        state._save_lab_state(name, model)
        logger.info("lab: loaded skill-set '{}' with model {}", name, model)
    except Exception as e:
        state._lab_agent = state._lab_cron = state._lab_name = state._lab_model = None
        state._save_lab_state(None, None)
        logger.error("lab load failed: {}", e)
        return web.Response(status=500, text=str(e))

    return web.json_response({"ok": True, "name": name, "model": model})


async def handle_lab_unload(_: web.Request) -> web.Response:
    if state._lab_cron:
        try: state._lab_cron.stop()
        except Exception: pass
    if state._lab_agent:
        try: state._lab_agent.stop()
        except Exception: pass

    state._lab_agent = state._lab_cron = state._lab_name = state._lab_model = None
    state._save_lab_state(None, None)
    logger.info("lab: unloaded skill-set")
    return web.json_response({"ok": True})


async def handle_lab_status(_: web.Request) -> web.Response:
    return web.json_response({
        "loaded": state._lab_name is not None,
        "name":   state._lab_name,
        "model":  state._lab_model,
    })


async def handle_models(_: web.Request) -> web.Response:
    """Return models grouped by provider, read from config.json."""
    import os
    cfg = state._read_config_raw()
    raw_providers = cfg.get("providers", {})

    providers = []
    for pname, pc in raw_providers.items():
        api_base  = pc.get("apiBase") or pc.get("api_base", "")
        label     = pc.get("label", pname.capitalize())
        key_env   = pc.get("apiKeyEnv", "")
        api_key   = os.environ.get(key_env, "") if key_env else (pc.get("apiKey") or pc.get("api_key") or "")
        static    = pc.get("models", [])

        fetched: list[dict] = []
        if api_base:
            try:
                headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
                async with aiohttp.ClientSession() as s:
                    async with s.get(
                        f"{api_base}/models",
                        headers=headers,
                        timeout=aiohttp.ClientTimeout(total=5),
                    ) as r:
                        data = await r.json()
                items = data.get("data") or data.get("models", [])
                fetched = [
                    {"name": m.get("id") or m.get("name"), "source": pname}
                    for m in items
                    if m.get("id") or m.get("name")
                ]
            except Exception as e:
                logger.warning("provider '{}' model fetch failed: {}", pname, e)

        model_list = fetched if fetched else [{"name": m, "source": pname} for m in static]
        providers.append({"name": pname, "label": label, "models": model_list})

    current = state._current_model()
    return web.json_response({"current": current, "providers": providers})


async def handle_image_gen(request: web.Request) -> web.Response:
    """Generate an image via xAI Grok. Returns { url, revised_prompt }."""
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")

    prompt = (body.get("prompt") or "").strip()
    model  = (body.get("model")  or "grok-imagine-image").strip()
    if not prompt:
        return web.Response(status=400, text="prompt required")
    if not state.GROK_API_KEY:
        return web.Response(status=500, text="GROK_API_KEY not configured")

    try:
        async with aiohttp.ClientSession() as s:
            async with s.post(
                f"{state.GROK_API_BASE}/images/generations",
                json={"model": model, "prompt": prompt, "n": 1, "response_format": "url"},
                headers={"Authorization": f"Bearer {state.GROK_API_KEY}"},
                timeout=aiohttp.ClientTimeout(total=90),
            ) as r:
                data = await r.json()
                if r.status != 200:
                    logger.error("image gen HTTP {}: {}", r.status, data)
                    return web.Response(status=r.status, text=str(data.get("error", data)))
    except Exception as e:
        logger.error("image gen error: {}", e)
        return web.Response(status=500, text=str(e))

    item = (data.get("data") or [{}])[0]
    return web.json_response({
        "url":            item.get("url", ""),
        "revised_prompt": item.get("revised_prompt", prompt),
    })


async def handle_set_model(request: web.Request) -> web.Response:
    """Persist model choice to config.json and reload agent."""
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")

    model    = (body.get("model")    or "").strip()
    provider = (body.get("provider") or "").strip()
    if not model:
        return web.Response(status=400, text="model required")

    # Persist model (and provider if supplied)
    cfg = state._read_config_raw()
    cfg["agents"]["defaults"]["model"] = model
    if provider and provider in cfg.get("providers", {}):
        cfg["agents"]["defaults"]["provider"] = provider
    state._write_config_raw(cfg)
    logger.info("model switched to {}", model)

    # Hot-reload agent
    try:
        if state._cron:
            state._cron.stop()
        config = _agent_mod._load_config()
        state._agent, state._cron = await _agent_mod._build_agent(config)
        logger.info("agent reloaded with model {}", model)
    except Exception as e:
        logger.error("agent reload failed: {}", e)
        return web.Response(status=500, text=f"config saved but reload failed: {e}")

    return web.json_response({"ok": True, "model": model})


# ── Workspace file management (Art Office) ───────────────────────────────────

_IDENTITY_FILES = {"SOUL.md", "AGENTS.md", "TOOLS.md", "HEARTBEAT.md", "USER.md"}


async def handle_workspace_get_file(request: web.Request) -> web.Response:
    name = request.match_info["name"]
    if name not in _IDENTITY_FILES:
        return web.Response(status=400, text="invalid filename")
    path = state.WORKSPACE_PATH / name
    content = path.read_text(encoding="utf-8") if path.exists() else ""
    return web.json_response({"name": name, "content": content})


async def handle_workspace_put_file(request: web.Request) -> web.Response:
    name = request.match_info["name"]
    if name not in _IDENTITY_FILES:
        return web.Response(status=400, text="invalid filename")
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")
    content = body.get("content", "")
    (state.WORKSPACE_PATH / name).write_text(content, encoding="utf-8")
    logger.info("workspace: saved {}", name)
    return web.json_response({"ok": True})


async def handle_workspace_get_memory(_: web.Request) -> web.Response:
    path = state.WORKSPACE_PATH / "memory" / "MEMORY.md"
    content = path.read_text(encoding="utf-8") if path.exists() else ""
    return web.json_response({"content": content})


async def handle_workspace_put_memory(request: web.Request) -> web.Response:
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")
    path = state.WORKSPACE_PATH / "memory" / "MEMORY.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.get("content", ""), encoding="utf-8")
    logger.info("workspace: saved memory/MEMORY.md")
    return web.json_response({"ok": True})


async def handle_workspace_get_skills(_: web.Request) -> web.Response:
    skills_dir = state.WORKSPACE_PATH / "skills"
    skills = []
    if skills_dir.exists():
        for d in sorted(skills_dir.iterdir()):
            if not d.is_dir():
                continue
            skill_file = d / "SKILL.md"
            content = skill_file.read_text(encoding="utf-8") if skill_file.exists() else ""
            skills.append({"name": d.name, "content": content})
    return web.json_response({"skills": skills})


async def handle_workspace_put_skill(request: web.Request) -> web.Response:
    name = request.match_info["name"]
    if not re.match(r"^[a-zA-Z0-9_\-]+$", name):
        return web.Response(status=400, text="invalid skill name")
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")
    skill_dir = state.WORKSPACE_PATH / "skills" / name
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(body.get("content", ""), encoding="utf-8")
    logger.info("workspace: saved skill '{}'", name)
    return web.json_response({"ok": True})


async def handle_workspace_delete_skill(request: web.Request) -> web.Response:
    name = request.match_info["name"]
    if not re.match(r"^[a-zA-Z0-9_\-]+$", name):
        return web.Response(status=400, text="invalid skill name")
    import shutil
    skill_dir = state.WORKSPACE_PATH / "skills" / name
    if skill_dir.exists():
        shutil.rmtree(skill_dir)
        logger.info("workspace: deleted skill '{}'", name)
    return web.json_response({"ok": True})


# ── Chat storage handlers ────────────────────────────────────────────────────

async def handle_list_chats(_: web.Request) -> web.Response:
    state.CHATS_DIR.mkdir(parents=True, exist_ok=True)
    chats = []
    for f in sorted(state.CHATS_DIR.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            with open(f, encoding="utf-8") as fp:
                data = json.load(fp)
            chats.append({
                "id":      data["id"],
                "title":   data.get("title", "Untitled"),
                "created": data.get("created", ""),
                "count":   len(data.get("messages", [])),
            })
        except Exception:
            pass
    return web.json_response({"chats": chats})


async def handle_save_chat(request: web.Request) -> web.Response:
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")
    messages = body.get("messages") or []
    title    = (body.get("title") or "").strip() or _auto_title(messages)
    chat_id  = (body.get("id")    or "").strip() or _new_id()
    state.CHATS_DIR.mkdir(parents=True, exist_ok=True)
    path = state.CHATS_DIR / f"{chat_id}.json"
    data = {
        "id":       chat_id,
        "title":    title,
        "created":  datetime.datetime.now().isoformat(timespec="seconds"),
        "messages": messages,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return web.json_response({"id": chat_id, "title": title})


async def handle_load_chat(request: web.Request) -> web.Response:
    chat_id = request.match_info["id"]
    if not re.match(r"^[a-f0-9]{12}$", chat_id):
        return web.Response(status=400, text="invalid id")
    path = state.CHATS_DIR / f"{chat_id}.json"
    if not path.exists():
        return web.Response(status=404, text="not found")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return web.json_response(data)


async def handle_delete_chat(request: web.Request) -> web.Response:
    chat_id = request.match_info["id"]
    if not re.match(r"^[a-f0-9]{12}$", chat_id):
        return web.Response(status=400, text="invalid id")
    path = state.CHATS_DIR / f"{chat_id}.json"
    if path.exists():
        path.unlink()
    return web.json_response({"ok": True})


async def handle_upload(request: web.Request) -> web.Response:
    try:
        reader = await request.multipart()
        field  = await reader.next()
    except Exception:
        return web.Response(status=400, text="multipart error")
    if not field:
        return web.Response(status=400, text="no file")
    filename  = field.filename or "upload.bin"
    safe_name = re.sub(r"[^\w\-_\.]", "_", filename)[:80]
    state.UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    ts   = int(time.time())
    dest = state.UPLOADS_DIR / f"{ts}_{safe_name}"
    with open(dest, "wb") as fp:
        while True:
            chunk = await field.read_chunk(65536)
            if not chunk:
                break
            fp.write(chunk)
    return web.json_response({"path": str(dest), "name": safe_name})


# ── MCP server management ────────────────────────────────────────────────────

async def handle_get_mcp(_: web.Request) -> web.Response:
    cfg = state._read_config_raw()
    mcp = cfg.get("tools", {}).get("mcpServers", {})
    servers = [{"name": k, **v} for k, v in mcp.items()]
    return web.json_response({"servers": servers})


async def handle_add_mcp(request: web.Request) -> web.Response:
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")

    name = (body.get("name") or "").strip()
    if not re.match(r"^[\w\-]+$", name):
        return web.Response(status=400, text="invalid name (alphanumeric + - only)")

    entry = {}
    if body.get("command"):
        entry["command"] = body["command"].strip()
        entry["args"] = body.get("args") or []
        if isinstance(entry["args"], str):
            entry["args"] = entry["args"].split()
        entry["env"] = body.get("env") or {}
    elif body.get("url"):
        entry["url"] = body["url"].strip()
        entry["headers"] = body.get("headers") or {}
    else:
        return web.Response(status=400, text="command or url required")

    if body.get("enabled_tools"):
        entry["enabledTools"] = body["enabled_tools"] if isinstance(body["enabled_tools"], list) else [body["enabled_tools"]]

    cfg = state._read_config_raw()
    cfg.setdefault("tools", {}).setdefault("mcpServers", {})[name] = entry
    state._write_config_raw(cfg)

    # Hot-reload agent to pick up new MCP server
    try:
        if state._cron: state._cron.stop()
        config = _agent_mod._load_config()
        state._agent, state._cron = await _agent_mod._build_agent(config)
        logger.info("MCP: added server '{}', agent reloaded", name)
    except Exception as e:
        logger.error("MCP agent reload failed: {}", e)
        return web.Response(status=500, text=f"saved but agent reload failed: {e}")

    return web.json_response({"ok": True, "name": name})


async def handle_del_mcp(request: web.Request) -> web.Response:
    name = request.match_info["name"]
    if not re.match(r"^[\w\-]+$", name):
        return web.Response(status=400, text="invalid name")

    cfg = state._read_config_raw()
    mcp = cfg.get("tools", {}).get("mcpServers", {})
    if name not in mcp:
        return web.Response(status=404, text="not found")
    del mcp[name]
    state._write_config_raw(cfg)

    try:
        if state._cron: state._cron.stop()
        config = _agent_mod._load_config()
        state._agent, state._cron = await _agent_mod._build_agent(config)
        logger.info("MCP: removed server '{}', agent reloaded", name)
    except Exception as e:
        logger.error("MCP agent reload failed: {}", e)

    return web.json_response({"ok": True})


# ── Cron job management ──────────────────────────────────────────────────────

def _serialize_job(j) -> dict:
    nxt  = j.state.next_run_at_ms
    last = j.state.last_run_at_ms
    return {
        "id":       j.id,
        "name":     j.name,
        "enabled":  j.enabled,
        "schedule": {
            "kind":    j.schedule.kind,
            "everyMs": j.schedule.every_ms,
            "expr":    j.schedule.expr,
            "atMs":    j.schedule.at_ms,
            "tz":      j.schedule.tz,
        },
        "message":     j.payload.message,
        "nextRunAt":   nxt,
        "lastRunAt":   last,
        "lastStatus":  j.state.last_status,
        "lastError":   j.state.last_error,
    }


async def handle_list_cron(_: web.Request) -> web.Response:
    jobs = state._cron.list_jobs(include_disabled=True) if state._cron else []
    return web.json_response({"jobs": [_serialize_job(j) for j in jobs]})


async def handle_add_cron(request: web.Request) -> web.Response:
    if not state._cron:
        return web.Response(status=503, text="cron not ready")
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")

    name    = (body.get("name") or "").strip()
    kind    = body.get("kind", "every")
    message = (body.get("message") or "").strip()
    if not name or not message:
        return web.Response(status=400, text="name and message required")

    from nanobot.cron.service import CronSchedule
    if kind == "every":
        every_ms = int(body.get("everyMs") or 0)
        if every_ms < 60_000:
            return web.Response(status=400, text="everyMs must be >= 60000")
        schedule = CronSchedule(kind="every", every_ms=every_ms)
    elif kind == "cron":
        expr = (body.get("expr") or "").strip()
        if not expr:
            return web.Response(status=400, text="expr required for cron kind")
        tz = body.get("tz") or "Europe/Brussels"
        schedule = CronSchedule(kind="cron", expr=expr, tz=tz)
    else:
        return web.Response(status=400, text="kind must be every or cron")

    job = state._cron.add_job(name=name, schedule=schedule, message=message)
    return web.json_response({"ok": True, "job": _serialize_job(job)})


async def handle_del_cron(request: web.Request) -> web.Response:
    if not state._cron:
        return web.Response(status=503, text="cron not ready")
    job_id = request.match_info["id"]
    ok = state._cron.remove_job(job_id)
    return web.json_response({"ok": ok})


async def handle_toggle_cron(request: web.Request) -> web.Response:
    if not state._cron:
        return web.Response(status=503, text="cron not ready")
    job_id = request.match_info["id"]
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")
    enabled = bool(body.get("enabled", True))
    job = state._cron.enable_job(job_id, enabled)
    if not job:
        return web.Response(status=404, text="not found")
    return web.json_response({"ok": True, "job": _serialize_job(job)})


async def handle_run_cron(request: web.Request) -> web.Response:
    if not state._cron:
        return web.Response(status=503, text="cron not ready")
    job_id = request.match_info["id"]
    ok = await state._cron.run_job(job_id, force=True)
    return web.json_response({"ok": ok})


# ── Agent status & settings (production mode) ────────────────────────────────

async def handle_agent_status(_: web.Request) -> web.Response:
    """Return basic identity info for the spawned agent web UI."""
    workspace_name = state.WORKSPACE_PATH.name
    # Extract agent name from first # heading in SOUL.md
    name = workspace_name
    soul = state.WORKSPACE_PATH / "SOUL.md"
    if soul.exists():
        for line in soul.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                name = line[2:].strip()
                break
    model = ""
    try:
        model = state._current_model()
    except Exception:
        pass
    return web.json_response({
        "workspace": workspace_name,
        "name":      name,
        "model":     model,
        "mode":      state.AGENT_MODE,
        "ready":     state._agent is not None,
    })


async def handle_agent_settings_get(_: web.Request) -> web.Response:
    """Return editable settings: model and Ollama base URL."""
    try:
        cfg = state._read_config_raw()
        model    = cfg.get("agents", {}).get("defaults", {}).get("model", "")
        providers = cfg.get("providers", {})
        local_cfg = providers.get("local") or {}
        ollama_base = local_cfg.get("apiBase", "") or local_cfg.get("api_base", "")
    except Exception:
        model = ""
        ollama_base = ""
    return web.json_response({"model": model, "ollamaBase": ollama_base})


async def handle_agent_settings_put(request: web.Request) -> web.Response:
    """Update model and/or Ollama base URL in config.json."""
    try:
        body = await request.json()
    except Exception:
        return web.Response(status=400, text="invalid JSON")
    try:
        cfg = state._read_config_raw()
        if "model" in body and body["model"]:
            cfg.setdefault("agents", {}).setdefault("defaults", {})["model"] = body["model"]
        if "ollamaBase" in body and body["ollamaBase"]:
            cfg.setdefault("providers", {}).setdefault("local", {})["apiBase"] = body["ollamaBase"]
        state._write_config_raw(cfg)
    except Exception as e:
        return web.Response(status=500, text=str(e))
    return web.json_response({"ok": True})
