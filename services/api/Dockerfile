FROM node:20-slim AS builder

WORKDIR /app

# better-sqlite3 needs native build tools
RUN apt-get update && apt-get install -y python3 make g++ && rm -rf /var/lib/apt/lists/*

COPY package.json tsconfig.json ./
RUN npm install
COPY src ./src
RUN npm run build

# ── Runtime ───────────────────────────────────────────────────────────────
FROM node:20-slim

# Runtime also needs the native .node bindings to load
RUN apt-get update && apt-get install -y python3 make g++ && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package.json ./
RUN npm install --omit=dev

COPY --from=builder /app/dist ./dist

ENV PORT=4000
ENV AGENT_URL=http://agent:6161

EXPOSE 4000

CMD ["node", "dist/index.js"]
