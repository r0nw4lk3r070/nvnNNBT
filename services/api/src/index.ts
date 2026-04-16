import express from 'express'
import { createProxyMiddleware } from 'http-proxy-middleware'
import { requireApiKey } from './middleware/auth.js'
import { initDb } from './db/database.js'
import { agentsRouter } from './routes/agents.js'

const app  = express()
const PORT = parseInt(process.env.PORT ?? '4000', 10)
const AGENT_URL = process.env.AGENT_URL ?? 'http://agent:6161'

app.use(express.json())

// ── Health — no auth ──────────────────────────────────────────────────────
app.get('/health', (_req, res) => {
  res.json({ status: 'ok', service: 'nvnnnbt-api', ts: new Date().toISOString() })
})

// ── All other routes require API key ─────────────────────────────────────
app.use(requireApiKey)

// ── Agent management (spawn, list, stop, delete, chat proxy) ─────────────
app.use('/agents', agentsRouter)

// ── SSE-capable proxy options ─────────────────────────────────────────────
const sseProxy = (target: string) =>
  createProxyMiddleware({
    target,
    changeOrigin: true,
    ws: false,
    on: {
      error: (err, _req, res: any) => {
        console.error('proxy error:', err.message)
        if (!res.headersSent) {
          res.writeHead(502, { 'Content-Type': 'application/json' })
          res.end(JSON.stringify({ error: 'Agent not reachable' }))
        }
      },
    },
    // Required for SSE streaming
    selfHandleResponse: false,
  })

// ── Routes proxied to agent ───────────────────────────────────────────────

// Chat (SSE)
app.post('/chat',      sseProxy(AGENT_URL))
app.post('/lab/chat',  sseProxy(AGENT_URL))

// Stop
app.post('/stop',      sseProxy(AGENT_URL))
app.post('/lab/stop',  sseProxy(AGENT_URL))

// Lab management
app.get ('/lab',            sseProxy(AGENT_URL))
app.post('/api/lab/load',   sseProxy(AGENT_URL))
app.post('/api/lab/unload', sseProxy(AGENT_URL))
app.get ('/api/lab/status', sseProxy(AGENT_URL))

// Models
app.get ('/api/models',     sseProxy(AGENT_URL))
app.post('/api/model',      sseProxy(AGENT_URL))

// Skill-sets
app.get ('/api/skillsets',  sseProxy(AGENT_URL))

// Chats
app.get ('/api/chats',        sseProxy(AGENT_URL))
app.post('/api/chats',        sseProxy(AGENT_URL))
app.get ('/api/chats/:id',    sseProxy(AGENT_URL))
app.delete('/api/chats/:id',  sseProxy(AGENT_URL))

// Uploads / MCP / Cron
app.post  ('/api/upload',           sseProxy(AGENT_URL))
app.get   ('/api/mcp',              sseProxy(AGENT_URL))
app.post  ('/api/mcp',              sseProxy(AGENT_URL))
app.delete('/api/mcp/:name',        sseProxy(AGENT_URL))
app.get   ('/api/cron',             sseProxy(AGENT_URL))
app.post  ('/api/cron',             sseProxy(AGENT_URL))
app.delete('/api/cron/:id',         sseProxy(AGENT_URL))
app.post  ('/api/cron/:id/toggle',  sseProxy(AGENT_URL))
app.post  ('/api/cron/:id/run',     sseProxy(AGENT_URL))

// ── Catch-all 404 ─────────────────────────────────────────────────────────
app.use((_req, res) => {
  res.status(404).json({ error: 'not found' })
})

initDb()
app.listen(PORT, '0.0.0.0', () => {
  console.log(`nvnnnbt-api listening on :${PORT}`)
  console.log(`  → proxying to agent at ${AGENT_URL}`)
})
