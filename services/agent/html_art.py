"""html_art.py — Art page HTML, shared CSS, and nav fragment."""
from __future__ import annotations

_NAV = """
<nav>
  <button class="hamburger" id="hamburger" aria-label="Menu">&#9776;</button>
  <div class="nav-links" id="nav-links">
    <a href="/" id="nav-art">Art</a>
    <a href="/lab" id="nav-lab">Lab</a>
  </div>
</nav>
"""

_SHARED_CSS = """
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg: #0d0d0d; --surface: #161616; --border: #2a2a2a;
    --accent: #7c5cfc; --accent2: #b48aff;
    --text: #e8e8e8; --muted: #666; --ok: #4caf50; --err: #f44;
  }
  html, body { height: 100%; }
  body { background: var(--bg); color: var(--text); font-family: 'Segoe UI', system-ui, sans-serif; height: 100dvh; display: flex; flex-direction: column; }
  nav { display: flex; align-items: center; gap: 2px; padding: 8px 20px; border-bottom: 1px solid var(--border); flex-shrink: 0; background: var(--surface); flex-wrap: wrap; }
  .hamburger { display: none; background: none; border: none; color: var(--text); font-size: 1.4rem; cursor: pointer; padding: 2px 10px; line-height: 1; }
  .nav-links { display: flex; gap: 2px; }
  nav a { color: var(--muted); text-decoration: none; font-size: .85rem; font-weight: 600; padding: 4px 12px; border-radius: 5px; letter-spacing: .04em; }
  nav a:hover { color: var(--text); background: var(--bg); }
  nav a.active { color: var(--accent2); background: color-mix(in srgb, var(--accent) 12%, transparent); }
  header { display: flex; align-items: center; gap: 12px; padding: 10px 20px; border-bottom: 1px solid var(--border); flex-shrink: 0; }
  header h1 { font-size: 1.05rem; font-weight: 600; color: var(--accent2); letter-spacing: .05em; }
  .hdr-btn { background: var(--surface); border: 1px solid var(--border); border-radius: 6px; color: var(--text); font-size: .8rem; padding: 5px 12px; cursor: pointer; display: flex; align-items: center; gap: 6px; }
  .hdr-btn:hover { border-color: var(--accent); }
  .accent { color: var(--accent2); font-weight: 600; }
  #messages { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 14px; min-height: 0; }
  .msg { max-width: 78%; padding: 10px 14px; border-radius: 10px; line-height: 1.55; font-size: .92rem; white-space: pre-wrap; word-break: break-word; }
  .msg.user { align-self: flex-end; background: var(--accent); color: #fff; border-bottom-right-radius: 3px; }
  .msg.assistant { align-self: flex-start; background: var(--surface); border: 1px solid var(--border); border-bottom-left-radius: 3px; }
  .msg.assistant.streaming { border-color: var(--accent); }
  #input-row { display: flex; gap: 10px; padding: 14px 20px; border-top: 1px solid var(--border); flex-shrink: 0; }
  #input { flex: 1; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: var(--text); font-size: .95rem; padding: 10px 14px; resize: none; outline: none; font-family: inherit; }
  #input:focus { border-color: var(--accent); }
  #send-btn { background: var(--accent); border: none; border-radius: 8px; color: #fff; padding: 0 20px; cursor: pointer; font-size: 1rem; font-weight: 600; transition: background .15s; }
  #send-btn:disabled { opacity: .4; cursor: default; }
  #send-btn.stop { background: #c0392b; }
  #send-btn.stop:disabled { opacity: .4; }
  /* Thinking dots */
  .thinking { display: flex; gap: 5px; align-items: center; padding: 4px 0; }
  .thinking span { width: 7px; height: 7px; border-radius: 50%; background: var(--muted); display: inline-block; animation: bounce 1.2s infinite ease-in-out; }
  .thinking span:nth-child(2) { animation-delay: .2s; }
  .thinking span:nth-child(3) { animation-delay: .4s; }
  @keyframes bounce { 0%,80%,100% { transform: scale(.7); opacity:.4; } 40% { transform: scale(1.1); opacity:1; } }
  /* Model panel */
  .side-panel { display: flex; position: fixed; top: 0; bottom: 0; right: 0; width: 340px; background: var(--surface); border-left: 1px solid var(--border); flex-direction: column; z-index: 100; overflow: hidden; transform: translateX(100%); transition: transform .25s cubic-bezier(.4,0,.2,1); }
  .side-panel.open { transform: translateX(0); }
  .side-panel > header { justify-content: space-between; }
  .side-panel > header h2 { font-size: 1rem; color: var(--accent2); }
  .close-btn { background: none; border: none; color: var(--muted); font-size: 1.3rem; cursor: pointer; }
  .close-btn:hover { color: var(--text); }
  .tab-row { display: flex; border-bottom: 1px solid var(--border); flex-shrink: 0; }
  .tab { flex: 1; padding: 10px; text-align: center; font-size: .85rem; cursor: pointer; color: var(--muted); border: none; background: none; }
  .tab.active { color: var(--accent2); border-bottom: 2px solid var(--accent); }
  .panel-search { flex-shrink: 0; margin: 10px; background: var(--bg); border: 1px solid var(--border); border-radius: 6px; color: var(--text); padding: 7px 12px; font-size: .85rem; outline: none; width: calc(100% - 20px); }
  .panel-search:focus { border-color: var(--accent); }
  .panel-list-wrap { flex: 1; min-height: 0; overflow: hidden; position: relative; }
  .panel-list { position: absolute; inset: 0; overflow-y: auto; padding: 0 10px 10px; scrollbar-width: thin; scrollbar-color: var(--border) transparent; }
  .model-item { display: flex; align-items: center; padding: 8px 10px; border-radius: 6px; cursor: pointer; font-size: .85rem; gap: 8px; }
  .model-item:hover { background: var(--bg); }
  .model-item.selected { background: color-mix(in srgb, var(--accent) 15%, transparent); }
  .model-name { flex: 1; font-family: monospace; font-size: .82rem; }
  .badge { font-size: .7rem; padding: 2px 7px; border-radius: 10px; background: var(--bg); border: 1px solid var(--border); color: var(--muted); flex-shrink: 0; }
  .badge.cloud { border-color: var(--accent); color: var(--accent2); }
  .badge.grok { border-color: #f0a030; color: #f0a030; }
  .badge.grok-image { border-color: #d35fd3; color: #d35fd3; }
  .panel-apply { flex-shrink: 0; margin: 10px; background: var(--accent); border: none; border-radius: 7px; color: #fff; padding: 10px; cursor: pointer; font-size: .9rem; font-weight: 600; }
  .panel-apply:disabled { opacity: .4; }
  /* Code */
  pre { background: #111; border: 1px solid var(--border); border-radius: 6px; padding: 10px 14px; overflow-x: auto; margin: 6px 0; white-space: pre; }
  code { font-family: 'Consolas','Cascadia Code',monospace; font-size: .82rem; background: rgba(255,255,255,.07); padding: 1px 5px; border-radius: 3px; }
  pre code { background: none; padding: 0; color: #d4d4d4; }
  .msg.assistant { white-space: normal; }
  .msg.assistant strong { font-weight: 700; }
  .msg.assistant em { font-style: italic; }
  /* Header */
  header { justify-content: space-between; }
  .hdr-actions { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
  /* Chats panel (left) */
  .side-left { display: none; position: fixed; top: 0; left: 0; width: 300px; height: 100dvh; background: var(--surface); border-right: 1px solid var(--border); flex-direction: column; z-index: 102; }
  .side-left.open { display: flex; }
  .side-left > header { justify-content: space-between; }
  .side-left > header h2 { font-size: 1rem; color: var(--accent2); }
  .chats-list { flex: 1; overflow-y: auto; padding: 8px; }
  .chat-item { display: flex; align-items: center; padding: 9px 12px; border-radius: 7px; cursor: pointer; gap: 8px; border: 1px solid transparent; margin-bottom: 2px; }
  .chat-item:hover { background: var(--bg); }
  .chat-item.active { background: color-mix(in srgb, var(--accent) 12%, transparent); border-color: var(--accent); }
  .chat-item-meta { flex: 1; min-width: 0; }
  .chat-item-title { font-size: .84rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .chat-item-sub { font-size: .72rem; color: var(--muted); margin-top: 2px; }
  .chat-del { font-size: .8rem; color: var(--muted); background: none; border: none; cursor: pointer; padding: 2px 5px; border-radius: 4px; flex-shrink: 0; opacity: 0; }
  .chat-item:hover .chat-del { opacity: 1; }
  .chat-del:hover { color: var(--err); }
  /* File preview bar */
  #file-preview { display: none; padding: 4px 20px; flex-shrink: 0; border-top: 1px solid var(--border); }
  .file-preview-inner { display: flex; align-items: center; gap: 8px; font-size: .8rem; }
  .file-preview-inner img { width: 42px; height: 42px; object-fit: cover; border-radius: 4px; }
  .fp-thumb-icon { font-size: 1.4rem; }
  .file-preview-name { flex: 1; color: var(--muted); }
  .fp-clear { background: none; border: none; color: var(--muted); font-size: .95rem; cursor: pointer; padding: 0 4px; }
  .fp-clear:hover { color: var(--err); }
  /* Upload button */
  .upload-btn { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: var(--muted); padding: 0 12px; cursor: pointer; font-size: 1.1rem; flex-shrink: 0; }
  .upload-btn:hover { border-color: var(--accent); color: var(--text); }
  /* Dropdown menus */
  .dropdown { position: relative; display: inline-block; }
  .dropdown-menu { display: none; position: absolute; top: 110%; right: 0; background: var(--surface); border: 1px solid var(--border); border-radius: 7px; min-width: 140px; z-index: 200; box-shadow: 0 4px 20px rgba(0,0,0,.5); overflow: hidden; }
  .dropdown-menu.open { display: block; }
  .dropdown-item { display: block; padding: 9px 14px; font-size: .83rem; cursor: pointer; color: var(--text); text-align: left; width: 100%; background: none; border: none; }
  .dropdown-item:hover { background: var(--bg); color: var(--accent2); }

// ── Cron panel (Art) ─────────────────────────────────────────────────────────
$('cron-btn').onclick = () => { $('cron-panel').classList.add('open'); loadCron(); };
$('close-cron').onclick = () => $('cron-panel').classList.remove('open');
function fmtCronSched(s) {
  if (!s) return '—';
  if (s.every_ms) return `every ${Math.round(s.every_ms/60000)}m`;
  if (s.expr) return s.expr;
  return JSON.stringify(s);
}
async function loadCron() {
  const d = await fetch('/api/cron').then(r=>r.json());
  const el = $('cron-list'); el.innerHTML = '';
  if (!d.jobs.length) { el.innerHTML = '<div style="color:var(--muted);font-size:.82rem">No scheduled jobs.</div>'; return; }
  for (const j of d.jobs) {
    const row = document.createElement('div'); row.className = 'mcp-server-row';
    row.style.flexWrap = 'wrap'; row.style.gap = '4px';
    const enabled = j.enabled !== false;
    row.innerHTML = `<span class="mcp-server-name" style="flex:1;min-width:120px">${esc(j.name)}</span><span class="mcp-server-cmd" style="flex:2;min-width:120px">${esc(fmtCronSched(j.schedule))}</span><button class="mcp-del-btn" style="background:${enabled?'var(--accent)':''};color:${enabled?'#fff':''};border-color:${enabled?'var(--accent)':''}" onclick="toggleCron('${j.id}',${enabled})">${enabled?'ON':'OFF'}</button> <button class="mcp-del-btn" onclick="runCron('${j.id}')">Run</button> <button class="mcp-del-btn" onclick="delCron('${j.id}')">Del</button>`;
    el.appendChild(row);
  }
}
async function toggleCron(id, enabled) {
  await fetch(`/api/cron/${id}/toggle`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({enabled:!enabled})}); loadCron();
}
async function runCron(id) {
  const r = await fetch(`/api/cron/${id}/run`, {method:'POST'});
  if (!r.ok) alert('Run failed: ' + await r.text());
}
async function delCron(id) {
  if (!confirm('Delete this job?')) return;
  await fetch(`/api/cron/${id}`, {method:'DELETE'}); loadCron();
}
async function addCronJob() {
  const name = $('cron-name').value.trim(); if (!name) { alert('Name required'); return; }
  const kind = $('cron-kind').value;
  const val  = $('cron-val').value.trim();  if (!val) { alert('Schedule value required'); return; }
  const msg  = $('cron-msg').value.trim();  if (!msg) { alert('Message required'); return; }
  const schedule = kind === 'every'
    ? {kind:'every', every_ms: parseFloat(val)*60000}
    : {kind:'cron', expr: val, tz: 'Europe/Brussels'};
  $('cron-add-btn').disabled = true; $('cron-add-btn').textContent = 'Adding…';
  const r = await fetch('/api/cron', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name, schedule, message:msg})});
  if (r.ok) { $('cron-name').value=''; $('cron-val').value=''; $('cron-msg').value=''; loadCron(); }
  else alert('Error: ' + await r.text());
  $('cron-add-btn').disabled = false; $('cron-add-btn').textContent = 'Add Job';
}

  /* MCP panel */
  .mcp-server-row { display: flex; align-items: center; padding: 9px 12px; border-radius: 7px; gap: 8px; border: 1px solid var(--border); margin-bottom: 4px; font-size: .82rem; }
  .mcp-server-name { font-family: monospace; font-weight: 600; flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .mcp-server-cmd { color: var(--muted); font-family: monospace; font-size: .75rem; flex: 2; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .mcp-del-btn { background: none; border: 1px solid var(--border); border-radius: 5px; color: var(--muted); cursor: pointer; padding: 3px 8px; font-size: .75rem; flex-shrink: 0; }
  .mcp-del-btn:hover { border-color: var(--err); color: var(--err); }
  .add-form { flex-shrink: 0; padding: 10px; border-top: 1px solid var(--border); display: flex; flex-direction: column; gap: 6px; }
  .add-form input, .add-form select, .add-form textarea { background: var(--bg); border: 1px solid var(--border); border-radius: 5px; color: var(--text); padding: 6px 10px; font-size: .82rem; font-family: inherit; outline: none; }
  .add-form input:focus, .add-form textarea:focus { border-color: var(--accent); }
  .add-form textarea { resize: vertical; min-height: 50px; }
  .add-form-row { display: flex; gap: 6px; }
  .add-form-row input, .add-form-row select { flex: 1; }
  .add-btn { background: var(--accent); border: none; border-radius: 6px; color: #fff; padding: 7px 12px; font-size: .83rem; font-weight: 600; cursor: pointer; }
  .add-btn:disabled { opacity: .4; }
  /* ── Mobile ──────────────────────────────────────────────────────────── */
  @media (max-width: 768px) {
    .hamburger { display: block; }
    nav { padding: 8px 14px; }
    .nav-links { display: none; flex-direction: column; width: 100%; padding: 4px 0 8px; gap: 0; }
    .nav-links.open { display: flex; }
    .nav-links a { padding: 10px 20px; border-radius: 0; font-size: .95rem; width: 100%; border-bottom: 1px solid var(--border); }
    .side-panel { width: 100% !important; }
    .side-left { width: 90vw !important; max-width: 320px !important; }
    #messages { padding: 10px; }
    #input-row { padding: 8px 10px; gap: 6px; }
    #file-preview { padding: 4px 10px; }
    header { padding: 8px 14px; }
    .msg { max-width: 92%; font-size: .88rem; }
    .hdr-btn { font-size: .72rem; padding: 4px 7px; }
    .hdr-actions { gap: 3px; }
  }
  @media print {
    nav, header, #input-row, #file-preview, .side-panel, .side-left, #chats-panel, #mcp-panel, #cron-panel { display: none !important; }
    body { background: #fff; color: #000; }
    .msg.user { background: #e8e8ff; color: #000; }
    .msg.assistant { background: #f4f4f4; border-color: #ccc; color: #000; }
    pre { border: 1px solid #ccc; }
  }
"""




def _build_art_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Art</title>
<style>{_SHARED_CSS}</style>
</head>
<body>
{_NAV}
<header>
  <h1>Art</h1>
  <div class="hdr-actions">
    <button class="hdr-btn" id="chats-btn">Chats</button>
    <button class="hdr-btn" id="new-chat-btn">&#xff0b; New</button>
    <button class="hdr-btn" id="save-btn">Save</button>
    <div class="dropdown">
      <button class="hdr-btn" id="export-btn">Export &#9662;</button>
      <div class="dropdown-menu" id="export-menu">
        <button class="dropdown-item" onclick="exportMd()">Markdown</button>
        <button class="dropdown-item" onclick="exportPdf()">PDF (print)</button>
      </div>
    </div>
    <button class="hdr-btn" id="cron-btn">&#9201; Jobs</button>
    <button class="hdr-btn" id="mcp-btn">&#9881; MCP</button>
    <button class="hdr-btn" id="model-btn">Model: <span class="accent" id="model-label">...</span></button>
  </div>
</header>
<div id="messages"></div>
<div id="file-preview">
  <div class="file-preview-inner">
    <div id="fp-thumb"></div>
    <span id="fp-name" class="file-preview-name"></span>
    <button class="fp-clear" id="fp-clear">&#x2715;</button>
  </div>
</div>
<div id="input-row">
  <button class="upload-btn" id="upload-btn" title="Attach file (or Ctrl+V for screenshot)">&#128206;</button>
  <input type="file" id="file-input" style="display:none" accept="*/*">
  <textarea id="input" rows="2" placeholder="Message Art\u2026 (Ctrl+V to paste screenshot)"></textarea>
  <button id="send-btn">&#9658;</button>
</div>

<!-- Chats panel -->
<div class="side-left" id="chats-panel">
  <header>
    <h2>Saved chats</h2>
    <button class="close-btn" id="close-chats">&times;</button>
  </header>
  <div class="chats-list" id="chats-list"></div>
</div>

<!-- Model panel -->
<div class="side-panel" id="model-panel">
  <header>
    <h2>Switch model</h2>
    <button class="close-btn" id="close-panel">&times;</button>
  </header>
  <div class="tab-row" id="model-tabs"></div>
  <div class="panel-list-wrap"><div class="panel-list" id="model-list"></div></div>
  <input class="panel-search" id="model-search" type="text" placeholder="Search\u2026">
  <button class="panel-apply" id="apply-btn" disabled>Apply</button>
</div>

<!-- Cron panel -->
<div class="side-panel" id="cron-panel">
  <header>
    <h2>Scheduled Jobs</h2>
    <button class="close-btn" id="close-cron">&times;</button>
  </header>
  <div class="panel-list-wrap"><div class="panel-list" id="cron-list" style="padding:10px"></div></div>
  <div class="add-form" id="cron-add-form">
    <div style="font-size:.8rem;font-weight:700;color:var(--muted);margin-bottom:4px">Add job</div>
    <input id="cron-name" placeholder="Job name" />
    <select id="cron-kind">
      <option value="every">Every N minutes</option>
      <option value="cron">Cron expression</option>
    </select>
    <input id="cron-val" placeholder="e.g. 60 (minutes) or 0 9 * * *" />
    <input id="cron-msg" placeholder="Message to send" />
    <button class="add-btn" id="cron-add-btn" onclick="addCronJob()">Add Job</button>
  </div>
</div>

<!-- MCP panel -->
<div class="side-panel" id="mcp-panel">
  <header>
    <h2>MCP Servers</h2>
    <button class="close-btn" id="close-mcp">&times;</button>
  </header>
  <div class="panel-list-wrap"><div class="panel-list" id="mcp-list" style="padding:10px"></div></div>
  <div class="add-form" id="mcp-add-form">
    <div style="font-size:.8rem;font-weight:700;color:var(--muted);margin-bottom:4px">Add server</div>
    <input id="mcp-name" placeholder="name (e.g. filesystem)" />
    <select id="mcp-type" onchange="mcpTypeChange()">
      <option value="stdio">stdio (command)</option>
      <option value="http">HTTP / SSE (url)</option>
    </select>
    <div id="mcp-stdio-row">
      <input id="mcp-cmd" placeholder="Command (e.g. npx)" />
      <input id="mcp-args" placeholder="Args (space-separated)" />
    </div>
    <div id="mcp-http-row" style="display:none">
      <input id="mcp-url" placeholder="URL (e.g. http://localhost:3000/sse)" />
    </div>
    <button class="add-btn" id="mcp-add-btn" onclick="addMcp()">Connect</button>
  </div>
</div>

<script>
const $ = id => document.getElementById(id);
let history = [], currentChatId = null, isDirty = false;
let allModels = {{}}, allProviders = [], currentModel = '', selectedModel = '', selectedProvider = '', activeTab = '';
let pendingFile = null;
document.querySelector('#nav-art').classList.add('active');

// \u2500\u2500 Notifications \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
if ('Notification' in window && Notification.permission === 'default') {{
  Notification.requestPermission();
}}
function notifyDone() {{
  if (document.hasFocus()) return;
  if ('Notification' in window && Notification.permission === 'granted') {{
    const n = new Notification('Art', {{ body: 'Response ready \u2713', icon: '' }});
    setTimeout(() => n.close(), 4000);
  }}
}}

// \u2500\u2500 Markdown renderer \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function renderMd(raw) {{
  const parts = raw.split(/(```[\\s\\S]*?```)/g);
  return parts.map((p, i) => {{
    if (i % 2 === 1) {{
      const m = p.match(/```(\\w*)\\n?([\\s\\S]*)```/);
      if (m) {{
        const code = m[2].replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
        return `<pre><code>${{code}}</code></pre>`;
      }}
      return `<pre>${{p.replace(/```/g,'')}}</pre>`;
    }}
    let h = p.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    h = h.replace(/`([^`\\n]+)`/g,'<code>$1</code>');
    h = h.replace(/\\*\\*([^*]+)\\*\\*/g,'<strong>$1</strong>');
    h = h.replace(/\\*([^*]+)\\*/g,'<em>$1</em>');
    h = h.replace(/^### (.+)$/gm,'<h3 style="font-size:.95rem;margin:.4em 0 .2em">$1</h3>');
    h = h.replace(/^## (.+)$/gm,'<h2 style="font-size:1.05rem;margin:.5em 0 .2em">$1</h2>');
    h = h.replace(/^# (.+)$/gm,'<h2 style="font-size:1.1rem;margin:.5em 0 .2em">$1</h2>');    h = h.replace(/!\[([^\]]*)\]\(([^)]+)\)/g,'<img src="$2" alt="$1" style="max-width:100%;border-radius:8px;margin:4px 0">');    h = h.replace(/^-\\s+(.+)$/gm,'\u2022\u00a0$1');    h = h.replace(/\\n/g,'<br>');
    return h;
  }}).join('');
}}

// \u2500\u2500 Init \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
async function init() {{
  try {{ await loadModels(); }}
  catch(e) {{ $('model-label').textContent = 'err'; console.error('init failed:', e); }}
}}
async function loadModels() {{
  const r = await fetch('/api/models');
  if (!r.ok) throw new Error('HTTP ' + r.status);
  const d = await r.json();
  currentModel = d.current;
  allProviders = d.providers || [];
  allModels = {{}};
  for (const p of allProviders) allModels[p.name] = p.models || [];
  if (!activeTab && allProviders.length) activeTab = allProviders[0].name;
  $('model-label').textContent = currentModel; selectedModel = currentModel;
  renderTabs();
  renderModelList();
}}
function renderTabs() {{
  const row = $('model-tabs'); row.innerHTML = '';
  for (const p of allProviders) {{
    const btn = document.createElement('button');
    btn.className = 'tab' + (p.name === activeTab ? ' active' : '');
    btn.textContent = p.label || p.name;
    btn.dataset.tab = p.name;
    btn.onclick = () => {{ activeTab = p.name; $('model-search').value=''; renderTabs(); renderModelList(); }};
    row.appendChild(btn);
  }}
}}

// \u2500\u2500 Messages \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function addMsg(role, content, html) {{
  const el = document.createElement('div');
  el.className = `msg ${{role}}`;
  if (html) el.innerHTML = html; else el.textContent = content;
  $('messages').appendChild(el); $('messages').scrollTop = 99999; return el;
}}
function renderHistory() {{
  $('messages').innerHTML = '';
  for (const m of history) {{
    const html = m.role === 'assistant' ? renderMd(m.content) : null;
    addMsg(m.role, m.content, html);
  }}
  $('messages').scrollTop = 99999;
}}

// \u2500\u2500 Send \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
async function send() {{
  let txt = $('input').value.trim();
  if (!txt && !pendingFile) return;
  let displayTxt = txt || '';
  if (pendingFile) {{
    txt = (txt ? txt + '\\n\\n' : '') + `[Attached file: ${{pendingFile.path}}]`;
    displayTxt = (displayTxt ? displayTxt + '\\n' : '') + `📎 ${{pendingFile.name}}`;
  }}
  $('input').value = ''; $('input').style.height = ''; $('send-btn').disabled = true;
  clearPreview();
  history.push({{role:'user',content:txt}});
  addMsg('user', displayTxt);
  // thinking dots
  const thinking = addMsg('assistant', '', '<div class="thinking"><span></span><span></span><span></span></div>');
  thinking.classList.add('streaming');
  const el = document.createElement('div'); el.className = 'msg assistant streaming'; let buf = '';
  // switch send → stop
  $('send-btn').textContent = '\u25a0'; $('send-btn').classList.add('stop'); $('send-btn').disabled = false;
  $('send-btn').onclick = () => fetch('/api/stop', {{method:'POST'}});
  const isImageModel = currentModel.startsWith('grok-imagine');
  try {{
    if (isImageModel) {{
      const r = await fetch('/api/image', {{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{prompt:txt,model:currentModel}})}});
      if (thinking.parentNode) thinking.remove();
      if (!el.parentNode) $('messages').appendChild(el);
      if (r.ok) {{
        const d = await r.json();
        buf = `![generated](${{d.url}})`;
        el.innerHTML = `<img src="${{d.url}}" alt="generated" style="max-width:100%;border-radius:8px">`;
        if (d.revised_prompt && d.revised_prompt !== txt) el.innerHTML += `<div style="font-size:.75rem;color:var(--muted);margin-top:6px">\u2728 ${{esc(d.revised_prompt)}}</div>`;
      }} else {{
        buf = `[image error: ${{await r.text()}}]`; el.textContent = buf;
      }}
    }} else {{
      const resp = await fetch('/chat', {{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{messages:history}})}});
      const reader = resp.body.getReader(); const dec = new TextDecoder();
      while (true) {{
        const {{done,value}} = await reader.read(); if (done) break;
        for (const line of dec.decode(value,{{stream:true}}).split('\\n')) {{
          if (!line.startsWith('data: ')) continue;
          const raw = line.slice(6).trim(); if (raw==='[DONE]') break;
          try {{
            const d = JSON.parse(raw).choices?.[0]?.delta?.content||'';
            if (d) {{
              if (thinking.parentNode) {{ thinking.replaceWith(el); $('messages').appendChild; }}
              buf+=d; el.textContent=buf; $('messages').scrollTop=99999;
            }}
          }} catch{{}}
        }}
      }}
    }}
  }} catch(e) {{ if (thinking.parentNode) thinking.remove(); el.textContent=`[error: ${{e.message}}]`; }}
  if (thinking.parentNode) thinking.remove();
  if (!el.parentNode) $('messages').appendChild(el);
  el.classList.remove('streaming');
  el.innerHTML = renderMd(buf);
  $('messages').scrollTop = 99999;
  history.push({{role:'assistant',content:buf}});
  isDirty = true; updateSaveLabel();
  // restore send button
  $('send-btn').textContent = '\u25b6'; $('send-btn').classList.remove('stop'); $('send-btn').disabled = false;
  $('send-btn').onclick = send;
  $('input').focus();
  if (buf) notifyDone();
}}
$('send-btn').onclick = send;
$('input').addEventListener('keydown', e => {{ if(e.key==='Enter'&&!e.shiftKey){{e.preventDefault();send();}} }});
$('input').addEventListener('input', function(){{ this.style.height=''; this.style.height=Math.min(this.scrollHeight,140)+'px'; }});

// \u2500\u2500 Paste screenshots \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
document.addEventListener('paste', async e => {{
  if (!e.clipboardData) return;
  for (const item of e.clipboardData.items) {{
    if (item.type.startsWith('image/')) {{
      e.preventDefault();
      await uploadBlob(item.getAsFile(), `paste_${{Date.now()}}.png`);
      break;
    }}
  }}
}});

// \u2500\u2500 File upload \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
$('upload-btn').onclick = () => $('file-input').click();
$('file-input').onchange = async e => {{
  const f = e.target.files?.[0]; if (!f) return; e.target.value = '';
  await uploadBlob(f, f.name);
}};
async function uploadBlob(blob, fname) {{
  const fd = new FormData(); fd.append('file', blob, fname);
  try {{
    const r = await fetch('/api/upload', {{method:'POST',body:fd}});
    if (!r.ok) {{ alert('Upload failed: ' + await r.text()); return; }}
    const d = await r.json();
    const isImg = (blob.type||'').startsWith('image/');
    pendingFile = {{path:d.path, name:d.name}};
    $('fp-thumb').innerHTML = isImg
      ? `<img src="${{URL.createObjectURL(blob)}}" style="width:42px;height:42px;object-fit:cover;border-radius:4px">`
      : `<span class="fp-thumb-icon">📄</span>`;
    $('fp-name').textContent = d.name;
    $('file-preview').style.display = '';
    $('input').focus();
  }} catch(e) {{ alert('Upload error: ' + e.message); }}
}}
function clearPreview() {{
  pendingFile = null; $('file-preview').style.display = 'none';
  $('fp-thumb').innerHTML = ''; $('fp-name').textContent = '';
}}
$('fp-clear').onclick = clearPreview;

// \u2500\u2500 Chat history \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
$('chats-btn').onclick = e => {{ e.stopPropagation(); $('chats-panel').classList.add('open'); loadChatsList(); }};
$('close-chats').onclick = () => $('chats-panel').classList.remove('open');
document.addEventListener('click', ev => {{
  if (!ev.target.closest('#chats-panel') && !ev.target.closest('#chats-btn'))
    $('chats-panel').classList.remove('open');
}});

async function loadChatsList() {{
  const d = await fetch('/api/chats').then(r=>r.json());
  const el = $('chats-list'); el.innerHTML = '';
  if (!d.chats.length) {{
    el.innerHTML = '<div style="padding:16px;color:var(--muted);font-size:.85rem">No saved chats yet</div>';
    return;
  }}
  for (const c of d.chats) {{
    const item = document.createElement('div');
    item.className = 'chat-item' + (c.id === currentChatId ? ' active' : '');
    const dt = c.created ? new Date(c.created).toLocaleDateString() : '';
    item.innerHTML = `<div class="chat-item-meta"><div class="chat-item-title">${{esc(c.title)}}</div><div class="chat-item-sub">${{dt}} \u00b7 ${{c.count}} msgs</div></div><button class="chat-del" title="Delete">\u2715</button>`;
    item.querySelector('.chat-item-meta').onclick = () => {{
      loadChat(c.id); $('chats-panel').classList.remove('open');
    }};
    item.querySelector('.chat-del').onclick = async ev => {{
      ev.stopPropagation();
      if (!confirm('Delete this chat?')) return;
      await fetch(`/api/chats/${{c.id}}`, {{method:'DELETE'}});
      if (currentChatId === c.id) {{ history=[]; currentChatId=null; isDirty=false; $('messages').innerHTML=''; updateSaveLabel(); }}
      loadChatsList();
    }};
    el.appendChild(item);
  }}
}}

function esc(s) {{ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }}

async function loadChat(id) {{
  const d = await fetch(`/api/chats/${{id}}`).then(r=>r.json());
  history = d.messages || []; currentChatId = d.id; isDirty = false;
  renderHistory(); updateSaveLabel();
}}

$('new-chat-btn').onclick = () => {{
  if (isDirty && history.length && !confirm('Discard unsaved changes?')) return;
  history = []; currentChatId = null; isDirty = false;
  $('messages').innerHTML = ''; updateSaveLabel();
}};

$('save-btn').onclick = async () => {{
  if (!history.length) {{ alert('Nothing to save yet.'); return; }}
  const body = {{messages: history}};
  if (currentChatId) {{
    body.id = currentChatId;
  }} else {{
    const t = prompt('Title (blank = auto):','');
    if (t === null) return;
    if (t.trim()) body.title = t.trim();
  }}
  const r = await fetch('/api/chats', {{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(body)}});
  if (r.ok) {{
    const d = await r.json(); currentChatId = d.id; isDirty = false; updateSaveLabel();
    $('save-btn').textContent = '\u2713 Saved';
    setTimeout(updateSaveLabel, 1800);
  }} else alert('Save failed: ' + await r.text());
}};

function updateSaveLabel() {{
  $('save-btn').textContent = (isDirty && history.length) ? 'Save \u2217' : 'Save';
}}

// \u2500\u2500 Model panel \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
$('model-btn').onclick = () => {{ $('model-panel').classList.add('open'); renderTabs(); renderModelList(); }};
$('close-panel').onclick = () => $('model-panel').classList.remove('open');
$('model-search').addEventListener('input', renderModelList);
$('model-search').addEventListener('keydown', e => {{ if (e.key === 'Enter' && !$('apply-btn').disabled) $('apply-btn').click(); }});
function renderModelList() {{
  const q = $('model-search').value.toLowerCase();
  const el = $('model-list'); el.innerHTML = '';
  for (const m of (allModels[activeTab] || []).filter(m=>m.name.toLowerCase().includes(q))) {{
    const item = document.createElement('div');
    item.className = 'model-item'+(m.name===selectedModel?' selected':'');
    item.innerHTML = `<span class="model-name">${{m.name}}</span><span class="badge ${{m.source}}">${{m.source}}</span>`;
    item.onclick = () => {{ selectedModel=m.name; selectedProvider=activeTab; $('apply-btn').disabled=(selectedModel===currentModel); renderModelList(); }};
    el.appendChild(item);
  }}
}}
$('apply-btn').onclick = async () => {{
  $('apply-btn').disabled=true; $('apply-btn').textContent='Applying\u2026';
  const r = await fetch('/api/model',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{model:selectedModel,provider:selectedProvider}})}});
  if(r.ok){{ currentModel=selectedModel; $('model-label').textContent=currentModel; $('model-panel').classList.remove('open'); }}
  else alert('Failed: '+await r.text());
  $('apply-btn').textContent='Apply';
}};

// \u2500\u2500 Export \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
$('export-btn').onclick = e => {{ e.stopPropagation(); $('export-menu').classList.toggle('open'); }};
document.addEventListener('click', ev => {{ if (!ev.target.closest('.dropdown')) $('export-menu').classList.remove('open'); }});
function exportMd() {{
  $('export-menu').classList.remove('open');
  if (!history.length) {{ alert('Nothing to export.'); return; }}
  let md = `# Art chat \u2014 ${{new Date().toLocaleDateString('nl-BE')}}\\n\\n`;
  for (const m of history) {{
    md += m.role === 'user' ? `**You:** ${{m.content}}\\n\\n` : `**Art:** ${{m.content}}\\n\\n`;
  }}
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([md], {{type:'text/markdown'}}));
  a.download = `art-chat-${{Date.now()}}.md`; a.click();
}}
function exportPdf() {{
  $('export-menu').classList.remove('open');
  window.print();
}}

// \u2500\u2500 MCP panel \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
$('mcp-btn').onclick = () => {{ $('mcp-panel').classList.add('open'); loadMcp(); }};
$('close-mcp').onclick = () => $('mcp-panel').classList.remove('open');
function mcpTypeChange() {{
  const v = $('mcp-type').value;
  $('mcp-stdio-row').style.display = v==='stdio' ? '' : 'none';
  $('mcp-http-row').style.display  = v==='http'  ? '' : 'none';
}}
async function loadMcp() {{
  const d = await fetch('/api/mcp').then(r=>r.json());
  const el = $('mcp-list'); el.innerHTML = '';
  if (!d.servers.length) {{
    el.innerHTML = '<div style="color:var(--muted);font-size:.82rem">No MCP servers configured.</div>';
    return;
  }}
  for (const s of d.servers) {{
    const row = document.createElement('div'); row.className = 'mcp-server-row';
    const cmd = s.command ? `${{s.command}} ${{(s.args||[]).join(' ')}}`.trim() : s.url || '';
    row.innerHTML = `<span class="mcp-server-name">${{esc(s.name)}}</span><span class="mcp-server-cmd">${{esc(cmd)}}</span><button class="mcp-del-btn" onclick="delMcp('${{s.name}}')">Remove</button>`;
    el.appendChild(row);
  }}
}}
async function addMcp() {{
  const name = $('mcp-name').value.trim(); if (!name) {{ alert('Name required'); return; }}
  const type = $('mcp-type').value;
  const body = {{name}};
  if (type === 'stdio') {{
    body.command = $('mcp-cmd').value.trim();
    body.args    = $('mcp-args').value.trim().split(/\\s+/).filter(Boolean);
    if (!body.command) {{ alert('Command required'); return; }}
  }} else {{
    body.url = $('mcp-url').value.trim();
    if (!body.url) {{ alert('URL required'); return; }}
  }}
  $('mcp-add-btn').disabled = true; $('mcp-add-btn').textContent = 'Connecting\u2026';
  const r = await fetch('/api/mcp', {{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(body)}});
  if (r.ok) {{ $('mcp-name').value=''; $('mcp-cmd').value=''; $('mcp-args').value=''; $('mcp-url').value=''; loadMcp(); }}
  else alert('Error: ' + await r.text());
  $('mcp-add-btn').disabled = false; $('mcp-add-btn').textContent = 'Connect';
}}
async function delMcp(name) {{
  if (!confirm(`Remove MCP server "${{name}}"?`)) return;
  await fetch(`/api/mcp/${{name}}`, {{method:'DELETE'}}); loadMcp();
}}

// \u2500\u2500 Hamburger nav \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
$('hamburger').onclick = e => {{ e.stopPropagation(); $('nav-links').classList.toggle('open'); }};
document.addEventListener('click', () => $('nav-links').classList.remove('open'));

init();
</script>
</body></html>"""

