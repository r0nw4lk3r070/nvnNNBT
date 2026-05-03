"""
Canonical list of cloud models available via Ollama and xAI.
"""

KNOWN_CLOUD_MODELS = [
    "gemma4:31b-cloud",
    "glm-5.1:cloud",
    "minimax-m2.7:cloud",
    "qwen3.5:397b-cloud",
    "qwen3-coder-next:cloud",
    "ministral-3:14b-cloud",
    "devstral-small-2:24b-cloud",
    "kimi-k2.5:cloud",
    "nemotron-3-nano:30b-cloud",
    "gemini-3-flash-preview:cloud",
    "deepseek-v3.2:cloud",
    "kimi-k2-thinking:cloud",
    "mistral-large-3:675b-cloud",
    "qwen3-coder:480b-cloud",
]

# xAI Grok — chat models (routed directly to api.x.ai)
GROK_CHAT_MODELS = [
    "grok-4.20-0309-reasoning",
    "grok-4.20-0309-non-reasoning",
    "grok-4.20-multi-agent-0309",
    "grok-4-1-fast-reasoning",
    "grok-4-1-fast-non-reasoning",
]

# xAI Grok — image generation models
GROK_IMAGE_MODELS = [
    "grok-imagine-image",
    "grok-imagine-image-pro",
]
