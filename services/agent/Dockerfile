FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY server.py handlers.py state.py agent.py html_art.py html_lab.py html_agent.py _cloud_models.py mcp_team.py mcp_factory.py ./

# Workspace and skill-sets are mounted as volumes at runtime
# /workspace  — agent identity (SOUL.md, AGENTS.md, config.json, memory/, cron/)
# /skill-sets — skill-set folders (one sub-dir per skill-set)

ENV WORKSPACE_PATH=/workspace
ENV SKILLSETS_PATH=/skill-sets
ENV AGENT_PORT=6161
ENV OLLAMA_BASE_URL=http://ollama:11434

EXPOSE 6161

CMD ["python", "-u", "server.py"]
