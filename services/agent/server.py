#!/usr/bin/env python3
"""server.py -- Art nanobot web server (entry point)."""
from __future__ import annotations

import asyncio

from aiohttp import web
from loguru import logger

import state
import agent as _agent_mod
from handlers import (
    handle_index, handle_health, handle_chat, handle_stop,
    handle_lab_index, handle_lab_chat, handle_lab_stop,
    handle_skillsets, handle_lab_load, handle_lab_unload, handle_lab_status,
    handle_models, handle_set_model,
    handle_image_gen,
    handle_list_chats, handle_save_chat, handle_load_chat, handle_delete_chat,
    handle_upload,
    handle_get_mcp, handle_add_mcp, handle_del_mcp,
    handle_list_cron, handle_add_cron, handle_del_cron,
    handle_toggle_cron, handle_run_cron,
    handle_workspace_get_file, handle_workspace_put_file,
    handle_workspace_get_memory, handle_workspace_put_memory,
    handle_workspace_get_skills, handle_workspace_put_skill, handle_workspace_delete_skill,
    handle_agent_status, handle_agent_settings_get, handle_agent_settings_put,
)


async def run() -> None:
    logger.info("Art: loading config from {}", state.CONFIG_PATH)
    state._base_config = _agent_mod._load_config()

    logger.info("Art: building agent (model={})", state._base_config.agents.defaults.model)
    state._agent, state._cron = await _agent_mod._build_agent(state._base_config)

    # Start native Discord channel if configured
    _disc_cfg = getattr(state._base_config.channels, "discord", None)
    if isinstance(_disc_cfg, dict) and _disc_cfg.get("enabled") and state._bus:
        from nanobot.channels.manager import ChannelManager
        state._channel_manager = ChannelManager(state._base_config, state._bus)
        # Start agent bus loop so inbound messages get dispatched
        asyncio.ensure_future(state._agent.run())
        asyncio.ensure_future(state._channel_manager.start_all())
        logger.info("Art: Discord channel started")

    # Restore last-loaded skill-set if one was active before shutdown
    _saved_name, _saved_model = state._load_lab_state()
    if _saved_name and _saved_model:
        _workspace = state.SKILLSETS_DIR / _saved_name
        if _workspace.exists():
            try:
                state._lab_agent, state._lab_cron = await _agent_mod._build_skillset_agent(_workspace, _saved_model)
                state._lab_name  = _saved_name
                state._lab_model = _saved_model
                logger.info("lab: restored skill-set '{}' (model {})", _saved_name, _saved_model)
            except Exception as _e:
                logger.warning("lab: could not restore skill-set '{}': {}", _saved_name, _e)
        else:
            logger.warning("lab: saved skill-set '{}' no longer exists, skipping restore", _saved_name)

    app = web.Application()
    app.router.add_get("/",                handle_index)
    app.router.add_get("/lab",             handle_lab_index)
    app.router.add_get("/health",          handle_health)
    app.router.add_get("/api/health",      handle_health)   # alias for nginx /api/ proxy
    app.router.add_post("/chat",           handle_chat)
    app.router.add_post("/lab/chat",       handle_lab_chat)
    app.router.add_get("/api/models",      handle_models)
    app.router.add_post("/api/model",      handle_set_model)
    app.router.add_post("/api/image",      handle_image_gen)
    app.router.add_get("/api/skillsets",   handle_skillsets)
    app.router.add_post("/api/lab/load",   handle_lab_load)
    app.router.add_post("/api/lab/unload", handle_lab_unload)
    app.router.add_get("/api/lab/status",  handle_lab_status)
    app.router.add_get("/api/chats",             handle_list_chats)
    app.router.add_post("/api/chats",            handle_save_chat)
    app.router.add_get("/api/chats/{id}",        handle_load_chat)
    app.router.add_delete("/api/chats/{id}",     handle_delete_chat)
    app.router.add_post("/api/upload",           handle_upload)
    app.router.add_post("/api/stop",             handle_stop)
    app.router.add_post("/api/lab/stop",         handle_lab_stop)
    app.router.add_get("/api/mcp",               handle_get_mcp)
    app.router.add_post("/api/mcp",              handle_add_mcp)
    app.router.add_delete("/api/mcp/{name}",     handle_del_mcp)
    app.router.add_get("/api/cron",              handle_list_cron)
    app.router.add_post("/api/cron",             handle_add_cron)
    app.router.add_delete("/api/cron/{id}",      handle_del_cron)
    app.router.add_post("/api/cron/{id}/toggle", handle_toggle_cron)
    app.router.add_post("/api/cron/{id}/run",    handle_run_cron)
    app.router.add_get("/api/workspace/files/{name}",    handle_workspace_get_file)
    app.router.add_put("/api/workspace/files/{name}",    handle_workspace_put_file)
    app.router.add_get("/api/workspace/memory",          handle_workspace_get_memory)
    app.router.add_put("/api/workspace/memory",          handle_workspace_put_memory)
    app.router.add_get("/api/workspace/skills",          handle_workspace_get_skills)
    app.router.add_put("/api/workspace/skills/{name}",   handle_workspace_put_skill)
    app.router.add_delete("/api/workspace/skills/{name}",handle_workspace_delete_skill)
    app.router.add_get("/api/status",                    handle_agent_status)
    app.router.add_get("/api/settings",                  handle_agent_settings_get)
    app.router.add_put("/api/settings",                  handle_agent_settings_put)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", state.HTTP_PORT)
    await site.start()
    logger.info("Art: listening on http://localhost:{}", state.HTTP_PORT)
    import socket as _socket
    with _socket.socket(_socket.AF_INET, _socket.SOCK_DGRAM) as _s:
        try: _s.connect(("8.8.8.8", 80)); _local_ip = _s.getsockname()[0]
        except Exception: _local_ip = "?"
    logger.info("Art: network access  http://{}:{}", _local_ip, state.HTTP_PORT)

    try:
        await asyncio.Event().wait()
    finally:
        await runner.cleanup()
        if state._channel_manager: await state._channel_manager.stop_all()
        if state._lab_cron: state._lab_cron.stop()
        if state._lab_agent: state._lab_agent.stop()
        if state._cron: state._cron.stop()
        if state._agent: state._agent.stop()


if __name__ == "__main__":
    asyncio.run(run())
