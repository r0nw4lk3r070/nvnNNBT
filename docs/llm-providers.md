# LLM Providers

nvnNNBT supports multiple LLM backends. The agent uses an OpenAI-compatible API interface, which means anything that speaks that protocol works — local or cloud.

The default model is **`gemma4:2b`** (Gemma 4, 2B parameters). Small, fast, capable enough for most assistant tasks. Change it in `workspace/config.json` or via the model selector in the chat UI.

---

## Bundled Ollama (default)

The simplest setup. Ollama runs as a service inside the Compose stack. No external dependencies.

**`docker-compose.yml`** — Ollama is included and configured automatically. The agent reaches it at `http://ollama:11434`.

**Pull a model after first start:**

```bash
docker exec nvnnnbt-ollama ollama pull gemma4:2b
```

Other models worth having available:

```bash
# Larger Gemma 4 variant — more capable, needs more VRAM
docker exec nvnnnbt-ollama ollama pull gemma4:12b

# Qwen 3 — strong reasoning, good context window
docker exec nvnnnbt-ollama ollama pull qwen3:8b

# Very small, lowest resource use
docker exec nvnnnbt-ollama ollama pull qwen3:1.7b
```

**Config (`workspace/config.json`):**

```json
{
  "agents": {
    "defaults": {
      "model": "gemma4:2b",
      "provider": "ollama"
    }
  },
  "providers": {
    "ollama": {
      "apiKey": "",
      "apiBase": "http://ollama:11434/v1"
    }
  }
}
```

---

## Ollama on the host machine

If Ollama is already running outside of Docker (e.g. on a machine that also runs other services), skip the bundled container and point the agent at the host.

**`.env`:**

```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
```

`host.docker.internal` resolves to the host machine from inside a container on both Windows/macOS (Docker Desktop) and Linux (requires the `extra_hosts` entry already in the `api` service — replicate it in the `agent` service if needed).

In `docker-compose.yml`, comment out or remove the `ollama:` service and the `ollama` dependency in the `agent` service.

**Config:** same as bundled Ollama — the URL is injected via `OLLAMA_BASE_URL`.

---

## vLLM

vLLM provides a high-throughput OpenAI-compatible inference server. Suitable for machines with NVIDIA GPUs where you want to serve a larger model efficiently.

vLLM is not part of the Compose stack — run it separately on the host or another machine.

**Start vLLM (example with Gemma 4):**

```bash
python -m vllm.entrypoints.openai.api_server \
  --model google/gemma-4-2b-it \
  --served-model-name gemma4:2b \
  --port 8000
```

**`.env`:**

```env
OLLAMA_BASE_URL=http://host.docker.internal:8000
```

**`workspace/config.json`:**

```json
{
  "agents": {
    "defaults": {
      "model": "gemma4:2b",
      "provider": "ollama"
    }
  },
  "providers": {
    "ollama": {
      "apiKey": "",
      "apiBase": "http://host.docker.internal:8000/v1"
    }
  }
}
```

The provider key is still `"ollama"` here — it refers to the OpenAI-compatible backend pattern, not the Ollama application specifically. Any server that speaks the `/v1/chat/completions` API works.

---

## External API providers

For cloud models or API-based providers, configure them in `workspace/config.json` under `providers` and set the model name accordingly. The agent recognises the model prefix and routes to the correct provider.

### xAI (Grok)

**`.env`:**

```env
GROK_API_KEY=xai-xxxxxxxxxxxxxxxx
```

**`workspace/config.json`:**

```json
{
  "agents": {
    "defaults": {
      "model": "grok-3-mini"
    }
  }
}
```

Grok models (`grok-*`) are automatically routed to `https://api.x.ai/v1`. No extra provider config needed — just the key in `.env`.

### OpenAI-compatible providers (OpenAI, Groq, Together AI, etc.)

Any provider with an OpenAI-compatible API can be wired in as a named provider.

**`workspace/config.json`:**

```json
{
  "agents": {
    "defaults": {
      "model": "llama-3.3-70b-versatile",
      "provider": "groq"
    }
  },
  "providers": {
    "groq": {
      "apiKey": "gsk_xxxxxxxxxxxxxxxx",
      "apiBase": "https://api.groq.com/openai/v1"
    }
  }
}
```

Or for OpenAI directly:

```json
{
  "agents": {
    "defaults": {
      "model": "gpt-4o-mini",
      "provider": "openai"
    }
  },
  "providers": {
    "openai": {
      "apiKey": "sk-xxxxxxxxxxxxxxxx",
      "apiBase": "https://api.openai.com/v1"
    }
  }
}
```

Keep API keys out of `config.json` when sharing workspaces. Prefer environment variables and load them in `config.json` if the nanobot-ai config loader supports env interpolation — or hardcode for personal/local use with the understanding that `config.json` is not committed.

---

## Per-agent model override (spawned agents)

When spawning an agent via the API, the `model` field in the spawn request is stored in the registry and passed to the container as an environment variable. Each spawned agent can use a different model.

```bash
# Spawn with a heavier model
curl -X POST http://localhost:4000/agents \
  -H "Content-Type: application/json" \
  -d '{"slug":"analyst","display_name":"Analyst","model":"gemma4:12b"}'
```

The spawned container inherits `OLLAMA_BASE_URL` from the Compose environment, so all agents point to the same inference backend by default.

---

## Choosing a model

| Use case | Recommended model | Notes |
|---|---|---|
| Default / everyday | `gemma4:2b` | Fast, low VRAM, capable |
| Deeper reasoning | `gemma4:12b` | Needs ~8 GB VRAM |
| Long context tasks | `qwen3:8b` | Strong 32K context window |
| Minimal resources | `qwen3:1.7b` | Runs on CPU |
| Cloud fallback | `grok-3-mini` | Requires `GROK_API_KEY` |

Switching models does not require a container restart. Use the model selector in the chat UI or edit `workspace/config.json` and the change takes effect on the next conversation.
