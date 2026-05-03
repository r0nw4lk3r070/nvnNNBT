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
    import os

    model = config.agents.defaults.model

    # Grok image models → xAI API (before the chat model check)
    if model.startswith("grok-imagine"):
        return OpenAICompatProvider(
            api_key       = _state.GROK_API_KEY,
            api_base      = _state.GROK_API_BASE,
            default_model = model,
            spec          = None,
        )

    # Grok chat models → xAI API
    if model.startswith("grok-"):
        return OpenAICompatProvider(
            api_key       = _state.GROK_API_KEY,
            api_base      = _state.GROK_API_BASE,
            default_model = model,
            spec          = None,
        )

    # All other models (Ollama local + cloud) — read provider from our config.
    # Ollama Desktop handles both local and :cloud suffix models at the same endpoint.
    raw         = _state._read_config_raw()
    providers   = raw.get("providers", {})
    pname       = getattr(config.agents.defaults, "provider", None) or ""
    p_cfg       = providers.get(pname) or providers.get("local") or {}

    api_base    = p_cfg.get("apiBase") or p_cfg.get("api_base") or f"{_state.OLLAMA_BASE}/v1"
    key_env     = p_cfg.get("apiKeyEnv", "")
    api_key     = (os.environ.get(key_env, "") if key_env else "") or \
                  p_cfg.get("apiKey", "") or p_cfg.get("api_key", "") or ""

    return OpenAICompatProvider(
        api_key       = api_key,
        api_base      = api_base,
        default_model = model,
        spec          = None,
    )


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


async def _build_skillset_agent(workspace: Path, model: str, provider_name: str = ""):
    """Build an ephemeral agent scoped to a skill-set workspace."""
    from nanobot.agent.loop                       import AgentLoop
    from nanobot.bus.queue                        import MessageBus
    from nanobot.cron.service                     import CronService
    from nanobot.session.manager                  import SessionManager
    from nanobot.utils.helpers                    import sync_workspace_templates
    from nanobot.providers.openai_compat_provider import OpenAICompatProvider
    import os

    sync_workspace_templates(workspace)

    # Route through the same provider resolution logic as _make_provider.
    # Grok image models → xAI
    if model.startswith("grok-imagine"):
        provider = OpenAICompatProvider(
            api_key       = _state.GROK_API_KEY,
            api_base      = _state.GROK_API_BASE,
            default_model = model,
            spec          = None,
        )
    # Grok chat models → xAI
    elif model.startswith("grok-"):
        provider = OpenAICompatProvider(
            api_key       = _state.GROK_API_KEY,
            api_base      = _state.GROK_API_BASE,
            default_model = model,
            spec          = None,
        )
    else:
        # Use configured provider (same as main agent path)
        raw       = _state._read_config_raw()
        providers = raw.get("providers", {})
        p_cfg     = providers.get(provider_name) or providers.get("local") or {}

        api_base  = p_cfg.get("apiBase") or p_cfg.get("api_base") or f"{_state.OLLAMA_BASE}/v1"
        key_env   = p_cfg.get("apiKeyEnv", "")
        api_key   = (os.environ.get(key_env, "") if key_env else "") or \
                    p_cfg.get("apiKey", "") or p_cfg.get("api_key", "") or ""

        provider = OpenAICompatProvider(
            api_key       = api_key,
            api_base      = api_base,
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
