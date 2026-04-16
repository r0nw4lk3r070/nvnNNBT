import { Router } from 'express'
import Dockerode from 'dockerode'
import { createProxyMiddleware } from 'http-proxy-middleware'
import { db } from '../db/database.js'

const router  = Router()
const docker  = new Dockerode({ socketPath: '/var/run/docker.sock' })

// Host-side project root — needed for bind mounts when spawning containers.
// Set HOST_PROJECT_PATH in .env to the absolute path of the nvnNNBT folder on the host.
const HOST_PROJECT_PATH = process.env.HOST_PROJECT_PATH ?? ''
const AGENT_IMAGE       = process.env.AGENT_IMAGE ?? 'nvnnnbt-agent:latest'
const NETWORK_NAME      = process.env.COMPOSE_NETWORK ?? 'nvnnnbt-net'
const OLLAMA_URL        = process.env.OLLAMA_BASE_URL ?? 'http://ollama:11434'

// Port range for spawned agents (host-side)
const PORT_MIN = 6200
const PORT_MAX = 6299

// ── Helpers ───────────────────────────────────────────────────────────────

function usedPorts(): Set<number> {
  const rows = db.prepare('SELECT port FROM agents').all() as { port: number }[]
  return new Set(rows.map(r => r.port))
}

function nextPort(): number {
  const used = usedPorts()
  for (let p = PORT_MIN; p <= PORT_MAX; p++) {
    if (!used.has(p)) return p
  }
  throw new Error('No free ports in range 6200–6299')
}

function slugSafe(s: string): boolean {
  return /^[a-z0-9][a-z0-9-]{0,30}$/.test(s)
}

async function syncStatuses(): Promise<void> {
  const rows = db.prepare("SELECT slug, container FROM agents").all() as { slug: string; container: string }[]
  const live  = await docker.listContainers({ all: true })
  const byName = new Map(live.flatMap(c => c.Names.map(n => [n.replace(/^\//, ''), c])))

  const update = db.prepare("UPDATE agents SET status=? WHERE slug=?")
  for (const row of rows) {
    const c = byName.get(row.container)
    const status = c ? c.State : 'removed'
    update.run(status, row.slug)
  }
}

// ── GET /agents ───────────────────────────────────────────────────────────
router.get('/', async (_req, res) => {
  try {
    await syncStatuses()
    const agents = db.prepare('SELECT * FROM agents ORDER BY created_at DESC').all()
    res.json({ agents })
  } catch (e) {
    res.status(500).json({ error: (e as Error).message })
  }
})

// ── POST /agents — spawn a new agent container ─────────────────────────────
router.post('/', async (req, res) => {
  const { slug, display_name, model } = req.body as {
    slug?: string
    display_name?: string
    model?: string
  }

  if (!slug || !slugSafe(slug)) {
    res.status(400).json({ error: 'slug required — lowercase alphanumeric + hyphens, max 31 chars' })
    return
  }
  if (!display_name?.trim()) {
    res.status(400).json({ error: 'display_name required' })
    return
  }
  if (!HOST_PROJECT_PATH) {
    res.status(500).json({ error: 'HOST_PROJECT_PATH not set — add it to .env' })
    return
  }

  const existing = db.prepare('SELECT slug FROM agents WHERE slug = ?').get(slug)
  if (existing) {
    res.status(409).json({ error: `agent '${slug}' already exists` })
    return
  }

  // Workspace must exist on the host before spawning.
  // If it's missing, Docker will create an empty dir — the agent will start but lack identity files.
  const workspaceHostPath = `${HOST_PROJECT_PATH}/data/workspaces/${slug}`
  const skillsetsHostPath = `${HOST_PROJECT_PATH}/skill-sets`
  const containerName     = `nvnnnbt-agent-${slug}`
  const chosenModel       = (model ?? 'qwen3:1.7b').trim()
  let   port: number

  try {
    port = nextPort()
  } catch (e) {
    res.status(503).json({ error: (e as Error).message })
    return
  }

  try {
    const container = await docker.createContainer({
      name:  containerName,
      Image: AGENT_IMAGE,
      Env: [
        'WORKSPACE_PATH=/workspace',
        'SKILLSETS_PATH=/skill-sets',
        'AGENT_PORT=6161',
        `OLLAMA_BASE_URL=${OLLAMA_URL}`,
      ],
      ExposedPorts: { '6161/tcp': {} },
      HostConfig: {
        Binds: [
          `${workspaceHostPath}:/workspace`,
          `${skillsetsHostPath}:/skill-sets:ro`,
        ],
        PortBindings: {
          '6161/tcp': [{ HostPort: String(port) }],
        },
        RestartPolicy: { Name: 'unless-stopped' },
        NetworkMode: NETWORK_NAME,
      },
    })

    await container.start()

    db.prepare(`
      INSERT INTO agents (slug, display_name, model, port, container, status, started_at)
      VALUES (?, ?, ?, ?, ?, 'running', datetime('now'))
    `).run(slug, display_name.trim(), chosenModel, port, containerName)

    res.status(201).json({ slug, display_name: display_name.trim(), model: chosenModel, port, container: containerName })
  } catch (e) {
    // Clean up if container was created but start failed
    try { docker.getContainer(containerName).remove({ force: true }) } catch { /* ignore */ }
    res.status(500).json({ error: (e as Error).message })
  }
})

// ── GET /agents/:slug/status ──────────────────────────────────────────────
router.get('/:slug/status', async (req, res) => {
  const row = db.prepare('SELECT * FROM agents WHERE slug = ?').get(req.params.slug) as any
  if (!row) { res.status(404).json({ error: 'not found' }); return }

  try {
    const info   = await docker.getContainer(row.container).inspect()
    const status = info.State.Running ? 'running' : info.State.Status
    db.prepare("UPDATE agents SET status=? WHERE slug=?").run(status, row.slug)
    res.json({ slug: row.slug, status, container: row.container, port: row.port })
  } catch (e: any) {
    // 404 from Docker means container was removed outside compose
    if (e?.statusCode === 404) {
      db.prepare("UPDATE agents SET status='removed' WHERE slug=?").run(row.slug)
      res.json({ slug: row.slug, status: 'removed', container: row.container, port: row.port })
    } else {
      res.status(500).json({ error: (e as Error).message })
    }
  }
})

// ── POST /agents/:slug/stop ────────────────────────────────────────────────
router.post('/:slug/stop', async (req, res) => {
  const row = db.prepare('SELECT * FROM agents WHERE slug = ?').get(req.params.slug) as any
  if (!row) { res.status(404).json({ error: 'not found' }); return }

  try {
    await docker.getContainer(row.container).stop()
    db.prepare("UPDATE agents SET status='stopped' WHERE slug=?").run(row.slug)
    res.json({ ok: true })
  } catch (e) {
    res.status(500).json({ error: (e as Error).message })
  }
})

// ── POST /agents/:slug/start ───────────────────────────────────────────────
router.post('/:slug/start', async (req, res) => {
  const row = db.prepare('SELECT * FROM agents WHERE slug = ?').get(req.params.slug) as any
  if (!row) { res.status(404).json({ error: 'not found' }); return }

  try {
    await docker.getContainer(row.container).start()
    db.prepare("UPDATE agents SET status='running', started_at=datetime('now') WHERE slug=?").run(row.slug)
    res.json({ ok: true })
  } catch (e) {
    res.status(500).json({ error: (e as Error).message })
  }
})

// ── DELETE /agents/:slug — stop + remove container + db row ───────────────
router.delete('/:slug', async (req, res) => {
  const row = db.prepare('SELECT * FROM agents WHERE slug = ?').get(req.params.slug) as any
  if (!row) { res.status(404).json({ error: 'not found' }); return }

  try {
    await docker.getContainer(row.container).remove({ force: true })
  } catch {
    // Container may already be gone — continue anyway
  }

  db.prepare('DELETE FROM agents WHERE slug=?').run(row.slug)
  res.json({ ok: true })
})

// ── POST /agents/:slug/chat — SSE proxy to spawned agent ──────────────────
// The spawned container is on the same Docker network as the API,
// reachable by container name.
router.post('/:slug/chat', async (req, res) => {
  const row = db.prepare('SELECT * FROM agents WHERE slug = ?').get(req.params.slug) as any
  if (!row) { res.status(404).json({ error: 'not found' }); return }
  if (row.status !== 'running') { res.status(503).json({ error: `agent '${req.params.slug}' is not running` }); return }

  const target = `http://${row.container}:6161`
  const proxy = createProxyMiddleware({
    target,
    changeOrigin: true,
    selfHandleResponse: false,
  })
  return proxy(req, res, (err?: unknown) => {
    if (err) {
      if (!res.headersSent) {
        res.status(502).json({ error: 'Agent not reachable' })
      }
    }
  })
})

export { router as agentsRouter }
