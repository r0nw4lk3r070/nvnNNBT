"""agent.py — Nanobot bootstrap: load config, build agent + cron."""
from __future__ import annotations

from pathlib import Path

import state as _state
from loguru import logger


def _load_config():
    from nanobot.config.loader import load_config, set_config_path
    set_config_path(_state.CONFIG_PATH)
    return load_config(_state.CONFIG_PATH)


def _make_provider(config):
    from nanobot.providers.openai_compat_provider import OpenAICompatProvider

    model = config.agents.defaults.model

    # Grok chat models → xAI API
    if model.startswith("grok-") and not model.startswith("grok-imagine"):
        return OpenAICompatProvider(
            api_key       = _state.GROK_API_KEY,
            api_base      = _state.GROK_API_BASE,
            default_model = model,
            spec          = None,
        )

    from nanobot.providers.registry import find_by_name
    provider_name = config.get_provider_name(model)
    p             = config.get_provider(model)
    spec          = find_by_name(provider_name) if provider_name else None
    backend       = spec.backend if spec else "openai_compat"

    if backend == "openai_compat":
        api_key  = (p.api_key  if p else "") or ""
        # If no key in config, fall back to {PROVIDER_NAME}_API_KEY env var.
        # This lets each machine set its own keys without editing config.json.
        if not api_key and provider_name:
            import os
            api_key = os.environ.get(f"{provider_name.upper()}_API_KEY", "")
        api_base = (p.api_base if p else None) or (spec.default_api_base if spec else None)
        return OpenAICompatProvider(
            api_key       = api_key,
            api_base      = api_base,
            default_model = model,
            spec          = spec,
        )
    raise RuntimeError(f"Unsupported provider backend: {backend}")


async def _build_agent(config):
    from nanobot.agent.loop       import AgentLoop
    from nanobot.bus.queue        import MessageBus
    from nanobot.cron.service     import CronService
    from nanobot.session.manager  import SessionManager
    from nanobot.utils.helpers    import sync_workspace_templates

    sync_workspace_templates(config.workspace_path)

    bus         = MessageBus()
    _state._bus = bus
    provider    = _make_provider(config)
    session_mgr = SessionManager(config.workspace_path)
    cron_store  = config.workspace_path / "cron" / "jobs.json"
    cron        = CronService(cron_store)

    agent = AgentLoop(
        bus                   = bus,
        provider              = provider,
        workspace             = config.workspace_path,
        model                 = config.agents.defaults.model,
        max_iterations        = config.agents.defaults.max_tool_iterations,
        context_window_tokens = config.agents.defaults.context_window_tokens,
        web_config            = config.tools.web,
        exec_config           = config.tools.exec,
        cron_service          = cron,
        restrict_to_workspace = config.tools.restrict_to_workspace,
        session_manager       = session_mgr,
        mcp_servers           = getattr(config.tools, "mcp_servers", {}),
        channels_config       = config.channels,
        timezone              = config.agents.defaults.timezone,
    )

    await cron.start()
    return agent, cron


async def _build_skillset_agent(workspace: Path, model: str):
    """Build an ephemeral agent scoped to a skill-set workspace."""
    from nanobot.agent.loop                       import AgentLoop
    from nanobot.bus.queue                        import MessageBus
    from nanobot.cron.service                     import CronService
    from nanobot.session.manager                  import SessionManager
    from nanobot.utils.helpers                    import sync_workspace_templates
    from nanobot.providers.openai_compat_provider import OpenAICompatProvider

    sync_workspace_templates(workspace)

    # Grok chat models → xAI API; everything else → Ollama (via env var URL)
    if model.startswith("grok-") and not model.startswith("grok-imagine"):
        provider = OpenAICompatProvider(
            api_key       = _state.GROK_API_KEY,
            api_base      = _state.GROK_API_BASE,
            default_model = model,
            spec          = None,
        )
    else:
        provider = OpenAICompatProvider(
            api_key       = "",
            api_base      = f"{_state.OLLAMA_BASE}/v1",
            default_model = model,
            spec          = None,
        )

    bus         = MessageBus()
    session_mgr = SessionManager(workspace)
    cron_store  = workspace / "cron" / "jobs.json"
    cron        = CronService(cron_store)

    cfg = _state._base_config
    agent = AgentLoop(
        bus                   = bus,
        provider              = provider,
        workspace             = workspace,
        model                 = model,
        max_iterations        = cfg.agents.defaults.max_tool_iterations,
        context_window_tokens = cfg.agents.defaults.context_window_tokens,
        web_config            = cfg.tools.web,
        exec_config           = cfg.tools.exec,
        cron_service          = cron,
        restrict_to_workspace = True,
        session_manager       = session_mgr,
        mcp_servers           = {},
        channels_config       = cfg.channels,
        timezone              = cfg.agents.defaults.timezone,
    )

    await cron.start()
    return agent, cron
