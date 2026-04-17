"""html_agent.py — Standalone web UI for spawned production agents."""
from __future__ import annotations


def _build_agent_html() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agent</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg:      #0d0d0d;
    --surface: #141a19;
    --border:  #1e2d2b;
    --accent:  #00b4a2;
    --accent2: #4dd0c4;
    --text:    #e4efee;
    --muted:   #5a7a76;
    --green:   #3dd68c;
    --red:     #f05353;
  }
  html, body { height: 100%; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Segoe UI', system-ui, sans-serif;
    height: 100dvh;
    display: flex;
    flex-direction: column;
  }

  /* ── Header ── */
  header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 18px;
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
    background: var(--surface);
  }
  .hdr-dot {
    width: 9px; height: 9px; border-radius: 50%;
    background: var(--muted); flex-shrink: 0;
    transition: background .3s;
  }
  .hdr-dot.ready { background: var(--green); }
  .hdr-name {
    font-size: 1rem; font-weight: 700;
    color: var(--accent2); letter-spacing: .04em; flex: 1;
  }
  .hdr-model {
    font-size: .72rem; font-family: monospace;
    color: var(--muted); padding: 2px 8px;
    border: 1px solid var(--border); border-radius: 12px;
  }
  .hdr-settings {
    background: none; border: none; color: var(--muted);
    font-size: 1.1rem; cursor: pointer; padding: 3px 6px;
    border-radius: 5px; line-height: 1;
  }
  .hdr-settings:hover { color: var(--text); background: var(--bg); }

  /* ── Messages ── */
  #messages {
    flex: 1; overflow-y: auto; padding: 18px 20px;
    display: flex; flex-direction: column; gap: 12px;
  }
  .msg {
    max-width: 80%; padding: 10px 14px;
    border-radius: 10px; line-height: 1.6;
    font-size: .92rem; white-space: pre-wrap; word-break: break-word;
  }
  .msg.user {
    align-self: flex-end;
    background: var(--accent);
    color: #001a18;
    border-bottom-right-radius: 3px;
  }
  .msg.assistant {
    align-self: flex-start;
    background: var(--surface);
    border: 1px solid var(--border);
    border-bottom-left-radius: 3px;
  }
  .msg.assistant.streaming { border-color: var(--accent); }
  .msg.assistant pre {
    background: var(--bg); border: 1px solid var(--border);
    border-radius: 6px; padding: 10px 12px;
    overflow-x: auto; font-size: .82rem;
    margin: 8px 0;
  }
  .msg.assistant code { font-family: 'Cascadia Code', 'Fira Mono', monospace; }
  .msg.assistant strong { font-weight: 700; }
  .msg.assistant em { font-style: italic; }

  /* ── Thinking dots ── */
  .thinking { display: flex; gap: 5px; align-items: center; padding: 4px 0; }
  .thinking span {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--muted); display: inline-block;
    animation: bounce 1.2s infinite ease-in-out;
  }
  .thinking span:nth-child(2) { animation-delay: .2s; }
  .thinking span:nth-child(3) { animation-delay: .4s; }
  @keyframes bounce {
    0%,80%,100% { transform: scale(.7); opacity: .4; }
    40%          { transform: scale(1.1); opacity: 1; }
  }

  /* ── Input row ── */
  #input-row {
    display: flex; gap: 10px;
    padding: 12px 18px;
    border-top: 1px solid var(--border);
    flex-shrink: 0;
  }
  #input {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text);
    font-size: .95rem;
    padding: 10px 14px;
    resize: none; outline: none;
    font-family: inherit;
  }
  #input:focus { border-color: var(--accent); }
  #send-btn {
    background: var(--accent);
    border: none; border-radius: 8px;
    color: #001a18;
    padding: 0 20px; cursor: pointer;
    font-size: 1rem; font-weight: 700;
    transition: background .15s;
  }
  #send-btn:disabled { opacity: .4; cursor: default; }
  #send-btn.stop { background: var(--red); color: #fff; }
  #send-btn.stop:disabled { opacity: .4; }

  /* ── Settings panel ── */
  .settings-panel {
    display: none;
    position: fixed; top: 0; right: 0;
    width: 320px; height: 100dvh;
    background: var(--surface);
    border-left: 1px solid var(--border);
    flex-direction: column;
    z-index: 100;
  }
  .settings-panel.open { display: flex; }
  .settings-hdr {
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 16px;
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
  }
  .settings-hdr h2 { font-size: .95rem; color: var(--accent2); font-weight: 700; }
  .close-btn { background: none; border: none; color: var(--muted); font-size: 1.2rem; cursor: pointer; }
  .close-btn:hover { color: var(--text); }
  .settings-body { padding: 16px; display: flex; flex-direction: column; gap: 14px; flex: 1; overflow-y: auto; }
  .field { display: flex; flex-direction: column; gap: 5px; }
  .field label { font-size: .75rem; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: .05em; }
  .field input {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text);
    font-size: .85rem;
    font-family: monospace;
    padding: 8px 10px;
    outline: none;
  }
  .field input:focus { border-color: var(--accent); }
  .field .hint { font-size: .72rem; color: var(--muted); }
  .save-btn {
    background: var(--accent);
    border: none; border-radius: 7px;
    color: #001a18;
    padding: 9px 16px;
    font-size: .85rem; font-weight: 700;
    cursor: pointer; margin-top: 4px;
  }
  .save-btn:disabled { opacity: .4; cursor: default; }
  .save-status { font-size: .77rem; color: var(--green); }
  .save-status.err { color: var(--red); }

  @media (max-width: 600px) {
    .settings-panel { width: 100%; }
    .msg { max-width: 92%; }
    #messages { padding: 10px 12px; }
    #input-row { padding: 8px 12px; }
  }
</style>
</head>
<body>

<header>
  <div class="hdr-dot" id="hdr-dot"></div>
  <div class="hdr-name" id="hdr-name">Loading…</div>
  <span class="hdr-model" id="hdr-model"></span>
  <button class="hdr-settings" id="settings-btn" title="Settings">&#9881;</button>
</header>

<div id="messages"></div>

<div id="input-row">
  <textarea id="input" rows="2" placeholder="Send a message…"></textarea>
  <button id="send-btn">&#9658;</button>
</div>

<!-- Settings panel -->
<div class="settings-panel" id="settings-panel">
  <div class="settings-hdr">
    <h2>Settings</h2>
    <button class="close-btn" id="close-settings">&#10005;</button>
  </div>
  <div class="settings-body">
    <div class="field">
      <label>Model</label>
      <input type="text" id="s-model" placeholder="e.g. qwen3:1.7b">
      <span class="hint">Any model available in your Ollama instance.</span>
    </div>
    <div class="field">
      <label>Ollama base URL</label>
      <input type="text" id="s-ollama" placeholder="http://host.docker.internal:11434/v1">
      <span class="hint">
        Windows/Mac: <code>http://host.docker.internal:11434/v1</code><br>
        Linux: <code>http://172.17.0.1:11434/v1</code>
      </span>
    </div>
    <button class="save-btn" id="save-settings-btn">Save</button>
    <div class="save-status" id="save-status" style="display:none"></div>
  </div>
</div>

<script>
'use strict';

const $ = id => document.getElementById(id);
const messages = [];
let streaming  = false;
let chatTask   = null;

// ── Load status on startup ────────────────────────────────────────────────────
async function loadStatus() {
  try {
    const r = await fetch('/api/status');
    if (!r.ok) return;
    const d = await r.json();
    $('hdr-name').textContent  = d.name  || d.workspace || 'Agent';
    $('hdr-model').textContent = d.model || '';
    document.title             = d.name  || 'Agent';
    if (d.ready) $('hdr-dot').classList.add('ready');
  } catch {}
}

// ── Render helpers ───────────────────────────────────────────────────────────
function esc(t) {
  return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function renderMsg(msg) {
  const el = document.createElement('div');
  el.className = 'msg ' + msg.role;
  el.dataset.id = msg.id;
  if (msg.role === 'assistant') {
    el.innerHTML = formatAssistant(msg.content);
  } else {
    el.textContent = msg.content;
  }
  return el;
}

function formatAssistant(text) {
  if (!text) return '<span class="thinking"><span></span><span></span><span></span></span>';
  // Simple markdown: code blocks, bold, italic
  return text
    .replace(/```([\s\S]*?)```/g, (_, c) => `<pre><code>${esc(c)}</code></pre>`)
    .replace(/`([^`]+)`/g,       (_, c) => `<code>${esc(c)}</code>`)
    .replace(/\*\*(.+?)\*\*/g,   (_, c) => `<strong>${c}</strong>`)
    .replace(/\*(.+?)\*/g,       (_, c) => `<em>${c}</em>`)
    .replace(/\n/g, '<br>');
}

function scrollBottom() {
  const el = $('messages');
  el.scrollTop = el.scrollHeight;
}

function renderAll() {
  const container = $('messages');
  container.innerHTML = '';
  for (const m of messages) container.appendChild(renderMsg(m));
  scrollBottom();
}

function updateLast() {
  const last = messages[messages.length - 1];
  if (!last) return;
  const el = $('messages').querySelector(`[data-id="${last.id}"]`);
  if (!el) return;
  if (last.role === 'assistant') {
    el.innerHTML = formatAssistant(last.content);
  } else {
    el.textContent = last.content;
  }
  el.classList.toggle('streaming', last.streaming === true);
  scrollBottom();
}

// ── Send message ──────────────────────────────────────────────────────────────
async function send() {
  const input = $('input');
  const text  = input.value.trim();
  if (!text || streaming) return;

  input.value = '';
  input.style.height = '';

  messages.push({ id: Date.now() + 'u', role: 'user', content: text });
  messages.push({ id: Date.now() + 'a', role: 'assistant', content: '', streaming: true });
  renderAll();

  streaming = true;
  $('send-btn').textContent = '◼';
  $('send-btn').classList.add('stop');

  const body = { messages: messages.filter(m => m.role !== 'assistant' || m.content)
                                   .map(({ role, content }) => ({ role, content })) };

  try {
    const resp = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });

    if (!resp.ok) {
      messages[messages.length - 1].content = 'Error ' + resp.status;
      messages[messages.length - 1].streaming = false;
      updateLast(); return;
    }

    const reader = resp.body.getReader();
    const dec    = new TextDecoder();
    let buf = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buf += dec.decode(value, { stream: true });
      const parts = buf.split('\\n\\n');
      buf = parts.pop();
      for (const part of parts) {
        const line = part.replace(/^data:\\s*/, '');
        if (!line || line === '[DONE]') continue;
        try {
          const d = JSON.parse(line);
          const delta = d?.choices?.[0]?.delta?.content || d?.error || '';
          if (delta) {
            messages[messages.length - 1].content += delta;
            updateLast();
          }
        } catch {}
      }
    }
  } catch (e) {
    messages[messages.length - 1].content = e.message || 'Network error';
  }

  messages[messages.length - 1].streaming = false;
  updateLast();
  streaming = false;
  $('send-btn').textContent = '▶';
  $('send-btn').classList.remove('stop');
}

async function stopStream() {
  try { await fetch('/api/stop', { method: 'POST' }); } catch {}
}

// ── Input events ──────────────────────────────────────────────────────────────
$('input').addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    if (streaming) stopStream(); else send();
  }
});
$('input').addEventListener('input', () => {
  const el = $('input');
  el.style.height = '';
  el.style.height = Math.min(el.scrollHeight, 140) + 'px';
});
$('send-btn').addEventListener('click', () => {
  if (streaming) stopStream(); else send();
});

// ── Settings panel ────────────────────────────────────────────────────────────
$('settings-btn').addEventListener('click', async () => {
  $('settings-panel').classList.add('open');
  try {
    const r = await fetch('/api/settings');
    if (r.ok) {
      const d = await r.json();
      $('s-model').value  = d.model      || '';
      $('s-ollama').value = d.ollamaBase || '';
    }
  } catch {}
});
$('close-settings').addEventListener('click', () => {
  $('settings-panel').classList.remove('open');
  $('save-status').style.display = 'none';
});
$('save-settings-btn').addEventListener('click', async () => {
  const btn = $('save-settings-btn');
  const st  = $('save-status');
  btn.disabled = true; btn.textContent = 'Saving…';
  st.style.display = 'none';
  try {
    const r = await fetch('/api/settings', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model:      $('s-model').value.trim(),
        ollamaBase: $('s-ollama').value.trim(),
      }),
    });
    if (r.ok) {
      st.className = 'save-status';
      st.textContent = 'Saved. Reload the page to apply model change.';
    } else {
      st.className = 'save-status err';
      st.textContent = 'Save failed — ' + r.status;
    }
  } catch (e) {
    st.className = 'save-status err';
    st.textContent = e.message;
  }
  st.style.display = '';
  btn.disabled = false; btn.textContent = 'Save';
  // Refresh model badge in header
  await loadStatus();
});

// ── Init ──────────────────────────────────────────────────────────────────────
loadStatus();
$('input').focus();
</script>
</body>
</html>
"""
