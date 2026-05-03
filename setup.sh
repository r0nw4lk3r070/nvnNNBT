#!/usr/bin/env bash
# setup.sh — first-time setup for Linux/Mac
# Creates .env from .env.example and auto-fills HOST_PROJECT_PATH.

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/.env"
EXAMPLE_FILE="$SCRIPT_DIR/.env.example"

if [ -f "$ENV_FILE" ]; then
  echo ".env already exists — skipping creation."
  echo "Edit $ENV_FILE manually if needed."
  exit 0
fi

cp "$EXAMPLE_FILE" "$ENV_FILE"

# Replace the empty HOST_PROJECT_PATH= line with the actual path
sed -i "s|^HOST_PROJECT_PATH=$|HOST_PROJECT_PATH=$SCRIPT_DIR|" "$ENV_FILE"

echo "Created .env with HOST_PROJECT_PATH=$SCRIPT_DIR"
echo ""
echo "Next steps:"
echo "  1. Review and adjust .env (Ollama URL, API keys, ports)"
echo "  2. docker compose up -d --build"
