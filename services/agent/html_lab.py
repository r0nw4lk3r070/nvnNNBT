"""html_lab.py — Lab page HTML."""
from __future__ import annotations

from html_art import _NAV, _SHARED_CSS

def _build_lab_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lab — Art</title>
<style>
{_SHARED_CSS}
  .lab-body {{ flex: 1; display: flex; overflow: hidden; }}
  .sidebar {{ width: 280px; flex-shrink: 0; border-right: 1px solid var(--border); display: flex; flex-direction: column; overflow: hidden; background: var(--surface); }}
  .sidebar-title {{ padding: 12px 16px; font-size: .8rem; font-weight: 700; color: var(--muted); letter-spacing: .08em; text-transform: uppercase; border-bottom: 1px solid var(--border); }}
  .ss-list {{ flex: 1; overflow-y: auto; padding: 8px; }}
  .ss-item {{ padding: 9px 12px; border-radius: 7px; cursor: pointer; font-size: .88rem; border: 1px solid transparent; margin-bottom: 3px; }}
  .ss-item:hover {{ background: var(--bg); }}
  .ss-item.selected {{ background: color-mix(in srgb, var(--accent) 12%, transparent); border-color: var(--accent); color: var(--accent2); }}
  .ss-files {{ font-size: .72rem; color: var(--muted); margin-top: 3px; }}
  .sidebar-footer {{ padding: 12px; border-top: 1px solid var(--border); display: flex; flex-direction: column; gap: 8px; }}
  .model-select-row {{ display: flex; gap: 6px; align-items: center; }}
  .model-select-label {{ font-size: .75rem; color: var(--muted); flex-shrink: 0; }}
  #lab-model-display {{ flex: 1; font-size: .78rem; font-family: monospace; color: var(--accent2); background: var(--bg); border: 1px solid var(--border); border-radius: 5px; padding: 5px 8px; cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  #lab-model-display:hover {{ border-color: var(--accent); }}
  #load-btn {{ background: var(--accent); border: none; border-radius: 6px; color: #fff; padding: 8px; font-size: .85rem; font-weight: 600; cursor: pointer; }}
  #load-btn:disabled {{ opacity: .4; cursor: default; }}
  #unload-btn {{ background: none; border: 1px solid var(--border); border-radius: 6px; color: var(--muted); padding: 6px; font-size: .8rem; cursor: pointer; }}
  #unload-btn:hover {{ border-color: var(--err); color: var(--err); }}
  .status-bar {{ font-size: .75rem; padding: 6px 12px; border-top: 1px solid var(--border); background: var(--surface); color: var(--muted); flex-shrink: 0; display: flex; align-items: center; gap: 6px; }}
  .status-dot {{ width: 7px; height: 7px; border-radius: 50%; background: var(--border); flex-shrink: 0; }}
  .status-dot.active {{ background: var(--ok); }}
  .chat-area {{ flex: 1; display: flex; flex-direction: column; overflow: hidden; }}
  .empty-state {{ flex: 1; display: flex; align-items: center; justify-content: center; color: var(--muted); font-size: .9rem; }}
  .sidebar-toggle {{ background: none; border: none; color: var(--text); font-size: 1.3rem; cursor: pointer; padding: 2px 8px; margin-right: 4px; }}
  .backdrop {{ position: fixed; inset: 0; background: rgba(0,0,0,.55); z-index: 199; display: none; }}
  /* Cron view */
  .area-tabs {{ display: flex; border-bottom: 1px solid var(--border); flex-shrink: 0; }}
  .area-tab {{ padding: 9px 18px; font-size: .84rem; cursor: pointer; color: var(--muted); background: none; border: none; border-bottom: 2px solid transparent; }}
  .area-tab.active {{ color: var(--accent2); border-bottom-color: var(--accent); }}
  #cron-view {{ flex: 1; overflow-y: auto; padding: 14px; display: none; flex-direction: column; gap: 10px; }}
  #cron-view.visible {{ display: flex; }}
  .cron-job {{ border: 1px solid var(--border); border-radius: 8px; padding: 10px 14px; font-size: .83rem; }}
  .cron-job-header {{ display: flex; align-items: center; gap: 10px; }}
  .cron-job-name {{ font-weight: 600; flex: 1; }}
  .cron-job-sched {{ font-family: monospace; font-size: .78rem; color: var(--muted); }}
  .cron-toggle {{ background: none; border: 1px solid var(--border); border-radius: 5px; cursor: pointer; padding: 3px 8px; font-size: .75rem; }}
  .cron-toggle.on {{ color: var(--ok); border-color: var(--ok); }}
  .cron-toggle.off {{ color: var(--muted); }}
  .cron-run-btn {{ background: none; border: 1px solid var(--border); border-radius: 5px; cursor: pointer; padding: 3px 8px; font-size: .75rem; color: var(--muted); }}
  .cron-run-btn:hover {{ border-color: var(--accent2); color: var(--accent2); }}
  .cron-del {{ background: none; border: 1px solid var(--border); border-radius: 5px; cursor: pointer; padding: 3px 8px; font-size: .75rem; }}
  .cron-del:hover {{ border-color: var(--err); color: var(--err); }}
  .cron-msg {{ margin-top: 5px; color: var(--muted); font-size: .77rem; }}
  .cron-status {{ margin-top: 3px; font-size: .72rem; }}
  .cron-status.ok {{ color: var(--ok); }} .cron-status.error {{ color: var(--err); }}
  .cron-next {{ font-size: .72rem; color: var(--muted); margin-top: 2px; }}
  .cron-add {{ border: 1px dashed var(--border); border-radius: 8px; padding: 12px; }}
  .cron-add-title {{ font-size: .8rem; font-weight: 600; color: var(--muted); margin-bottom: 8px; }}
  @media (max-width: 768px) {{
    .sidebar {{ position: fixed; top: 0; left: -100%; width: 85vw; max-width: 320px; height: 100dvh; z-index: 200; transition: left .25s ease; border-right: 1px solid var(--border); }}
    .sidebar.open {{ left: 0; }}
    .backdrop.open {{ display: block; }}
    .sidebar-toggle {{ display: flex; align-items: center; }}
    .hdr-sub {{ display: none; }}
  }}
  @media (min-width: 769px) {{
    .sidebar-toggle {{ display: none; }}
  }}
</style>
</head>
<body>
{_NAV}
<header>
  <button class="sidebar-toggle" id="sidebar-toggle" aria-label="Skill-sets">&#9776;</button>
  <h1>Lab</h1>
  <span class="hdr-sub" style="font-size:.8rem;color:var(--muted)">Load a skill-set and start chatting</span>
</header>

<div class="backdrop" id="backdrop"></div>
<div class="lab-body">
  <!-- Sidebar -->
  <div class="sidebar" id="sidebar">
    <div class="sidebar-title">Skill-sets</div>
    <div class="ss-list" id="ss-list"></div>
    <div class="sidebar-footer">
      <div class="model-select-row">
        <span class="model-select-label">Model</span>
        <div id="lab-model-display">select\u2026</div>
      </div>
      <button id="load-btn" disabled>Load</button>
      <button id="unload-btn" style="display:none">Unload</button>
    </div>
  </div>

  <!-- Main area -->
  <div class="chat-area">
    <div class="area-tabs">
      <button class="area-tab active" id="tab-chat" onclick="switchTab('chat')">Chat</button>
      <button class="area-tab" id="tab-cron" onclick="switchTab('cron')">Jobs</button>
    </div>

    <!-- Chat panel -->
    <div id="messages" style="display:none"></div>
    <div class="empty-state" id="empty-state">&#8592; Select a skill-set and load it</div>
    <div id="input-row" style="display:none">
      <textarea id="input" rows="2" placeholder="Message\u2026"></textarea>
      <button id="send-btn">&#9658;</button>
    </div>

    <!-- Cron panel -->
    <div id="cron-view">
      <div id="cron-list"></div>
      <!-- Add job form -->
      <div class="cron-add">
        <div class="cron-add-title">New scheduled job</div>
        <div class="add-form" style="padding:0;border:none">
          <input id="cron-name" placeholder="Job name" />
          <textarea id="cron-msg" placeholder="Message Art runs on schedule\u2026" style="min-height:46px"></textarea>
          <div class="add-form-row">
            <select id="cron-kind" onchange="cronKindChange()">
              <option value="every">Every …</option>
              <option value="cron">Cron expression</option>
            </select>
          </div>
          <div id="cron-every-row" class="add-form-row">
            <input id="cron-every-val" type="number" min="1" placeholder="Amount" value="60" style="width:80px"/>
            <select id="cron-every-unit">
              <option value="60000">minutes</option>
              <option value="3600000">hours</option>
              <option value="86400000">days</option>
            </select>
          </div>
          <div id="cron-expr-row" class="add-form-row" style="display:none">
            <input id="cron-expr" placeholder="0 9 * * * (cron expr)" />
          </div>
          <button class="add-btn" id="cron-add-btn" onclick="addCronJob()">Add job</button>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="status-bar">
  <div class="status-dot" id="status-dot"></div>
  <span id="status-text">No skill-set loaded</span>
</div>

<!-- Model panel -->
<div class="side-panel" id="model-panel">
  <header>
    <h2>Select model</h2>
    <button class="close-btn" id="close-panel">&times;</button>
  </header>
  <div class="tab-row">
    <button class="tab active" data-tab="local">Local</button>
    <button class="tab" data-tab="cloud">Cloud</button>
  </div>
  <input class="panel-search" id="model-search" type="text" placeholder="Search\u2026">
  <div class="panel-list" id="model-list"></div>
  <button class="panel-apply" id="apply-model-btn" disabled>Select</button>
</div>

<script>
const $ = id => document.getElementById(id);
document.querySelector('#nav-lab').classList.add('active');

let skillsets = [], selectedSS = null, labModel = '', labHistory = [];
let allModels = {{local:[],cloud:[]}}, panelSelected = '', panelTab = 'local';
let activeAreaTab = 'chat';

// ── Markdown renderer ──────────────────────────────────────────────────────
function renderMd(raw) {{
  const parts = raw.split(/(```[\\s\\S]*?```)/g);
  return parts.map((p, i) => {{
    if (i % 2 === 1) {{
      const m = p.match(/```(\\w*)\\n?([\\s\\S]*)```/);
      if (m) {{ const code = m[2].replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); return `<pre><code>${{code}}</code></pre>`; }}
      return `<pre>${{p.replace(/```/g,'')}}</pre>`;
    }}
    let h = p.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    h = h.replace(/`([^`\\n]+)`/g,'<code>$1</code>');
    h = h.replace(/\\*\\*([^*]+)\\*\\*/g,'<strong>$1</strong>');
    h = h.replace(/\\*([^*]+)\\*/g,'<em>$1</em>');
    h = h.replace(/^### (.+)$/gm,'<h3 style="font-size:.95rem;margin:.4em 0 .2em">$1</h3>');
    h = h.replace(/^## (.+)$/gm,'<h2 style="font-size:1.05rem;margin:.5em 0 .2em">$1</h2>');
    h = h.replace(/^# (.+)$/gm,'<h2 style="font-size:1.1rem;margin:.5em 0 .2em">$1</h2>');
    h = h.replace(/\\n/g,'<br>'); return h;
  }}).join('');
}}

// \u2500\u2500 Tab switching \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function switchTab(tab) {{
  activeAreaTab = tab;
  $('tab-chat').classList.toggle('active', tab==='chat');
  $('tab-cron').classList.toggle('active', tab==='cron');
  const inChat = tab === 'chat';
  $('cron-view').classList.toggle('visible', !inChat);
  if (!inChat) {{
    // hide chat elements
    $('empty-state').style.display = 'none';
    $('input-row').style.display = 'none';
    if ($('messages').style.display !== 'none') $('messages').style.display = 'none';
    loadCron();
  }} else {{
    // restore chat state
    const loaded = $('status-dot').classList.contains('active');
    $('messages').style.display = loaded ? 'flex' : 'none';
    $('empty-state').style.display = loaded ? 'none' : 'flex';
    $('input-row').style.display = loaded ? 'flex' : 'none';
  }}
}}

// \u2500\u2500 Init \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
async function init() {{
  await Promise.all([loadSkillsets(), loadModels()]);
  await loadStatus();
}}

async function loadSkillsets() {{
  const d = await fetch('/api/skillsets').then(r=>r.json());
  skillsets = d.skillsets; renderSS();
}}
async function loadModels() {{
  const d = await fetch('/api/models').then(r=>r.json());
  allModels = {{local:d.local, cloud:d.cloud}};
  if (!labModel) {{ labModel = d.current; $('lab-model-display').textContent = labModel; panelSelected = labModel; }}
}}
async function loadStatus() {{
  const d = await fetch('/api/lab/status').then(r=>r.json());
  if (d.loaded) setActive(d.name, d.model);
}}

function renderSS() {{
  const el = $('ss-list'); el.innerHTML = '';
  for (const ss of skillsets) {{
    const item = document.createElement('div');
    item.className = 'ss-item' + (ss.name === selectedSS ? ' selected' : '');
    item.innerHTML = `<div>${{ss.name}}</div><div class="ss-files">${{ss.files.slice(0,4).join(' \u00b7 ')}}</div>`;
    item.onclick = () => {{ selectedSS = ss.name; renderSS(); $('load-btn').disabled = !labModel; }};
    el.appendChild(item);
  }}
}}
function setActive(name, model) {{
  $('status-dot').classList.add('active');
  $('status-text').textContent = `Loaded: ${{name}} \u00b7 ${{model}}`;
  if (activeAreaTab === 'chat') {{
    $('messages').style.display = 'flex';
    $('empty-state').style.display = 'none';
    $('input-row').style.display = 'flex';
  }}
  $('unload-btn').style.display = '';
  $('load-btn').textContent = 'Reload';
}}
function setInactive() {{
  $('status-dot').classList.remove('active');
  $('status-text').textContent = 'No skill-set loaded';
  $('messages').style.display = 'none';
  $('empty-state').style.display = activeAreaTab === 'chat' ? 'flex' : 'none';
  $('input-row').style.display = 'none';
  $('unload-btn').style.display = 'none';
  $('load-btn').textContent = 'Load';
  $('messages').innerHTML = ''; labHistory = [];
}}
$('load-btn').onclick = async () => {{
  if (!selectedSS || !labModel) return;
  $('load-btn').disabled=true; $('load-btn').textContent='Loading\u2026';
  const r = await fetch('/api/lab/load',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{name:selectedSS,model:labModel}})}});
  if (r.ok) {{ $('messages').innerHTML=''; labHistory=[]; setActive(selectedSS, labModel); closeSidebar(); }}
  else alert('Load failed: ' + await r.text());
  $('load-btn').disabled=false;
}};
$('unload-btn').onclick = async () => {{
  await fetch('/api/lab/unload',{{method:'POST'}}); setInactive();
}};

// \u2500\u2500 Chat \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function addMsg(role, text, html) {{
  const el=document.createElement('div'); el.className=`msg ${{role}}`;
  if (html) el.innerHTML=html; else el.textContent=text;
  $('messages').appendChild(el); $('messages').scrollTop=99999; return el;
}}
async function send() {{
  const txt=$('input').value.trim(); if(!txt) return;
  $('input').value=''; $('input').style.height=''; $('send-btn').disabled=true;
  labHistory.push({{role:'user',content:txt}}); addMsg('user',txt);
  const thinking=addMsg('assistant','','<div class="thinking"><span></span><span></span><span></span></div>');
  thinking.classList.add('streaming');
  const el=document.createElement('div'); el.className='msg assistant streaming'; let buf='';
  $('send-btn').textContent='\u25a0'; $('send-btn').classList.add('stop'); $('send-btn').disabled=false;
  $('send-btn').onclick=()=>fetch('/api/lab/stop',{{method:'POST'}});
  try {{
    const resp=await fetch('/lab/chat',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{messages:labHistory}})}});
    const reader=resp.body.getReader(); const dec=new TextDecoder();
    while(true){{const {{done,value}}=await reader.read(); if(done)break;
      for(const line of dec.decode(value,{{stream:true}}).split('\\n')){{
        if(!line.startsWith('data: '))continue; const raw=line.slice(6).trim(); if(raw==='[DONE]')break;
        try{{
          const d=JSON.parse(raw).choices?.[0]?.delta?.content||'';
          if(d){{if(thinking.parentNode)thinking.replaceWith(el); buf+=d; el.textContent=buf; $('messages').scrollTop=99999;}}
        }}catch{{}}
      }}
    }}
  }}catch(e){{if(thinking.parentNode)thinking.remove(); el.textContent=`[error: ${{e.message}}]`;}}
  if(thinking.parentNode)thinking.remove();
  if(!el.parentNode)$('messages').appendChild(el);
  if(thinking.parentNode)thinking.remove();
  if(!el.parentNode)$('messages').appendChild(el);
  el.classList.remove('streaming');
  el.innerHTML = renderMd(buf);
  $('messages').scrollTop=99999;
  labHistory.push({{role:'assistant',content:buf}});
  $('send-btn').textContent='\u25b6'; $('send-btn').classList.remove('stop'); $('send-btn').disabled=false;
  $('send-btn').onclick=send; $('input').focus();
}}
$('send-btn').onclick=send;
$('input').addEventListener('keydown',e=>{{if(e.key==='Enter'&&!e.shiftKey){{e.preventDefault();send();}}}});
$('input').addEventListener('input',function(){{this.style.height='';this.style.height=Math.min(this.scrollHeight,140)+'px';}});

// \u2500\u2500 Cron \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
function fmtTime(ms) {{
  if (!ms) return '\u2014';
  const d=new Date(ms); return d.toLocaleString('nl-BE',{{hour:'2-digit',minute:'2-digit',day:'2-digit',month:'2-digit'}});
}}
function fmtSched(s) {{
  if (s.kind==='every') return `every ${{s.everyMs/60000}} min`;
  if (s.kind==='cron')  return s.expr;
  if (s.kind==='at')    return `once @ ${{fmtTime(s.atMs)}}`;
  return s.kind;
}}
async function loadCron() {{
  const d = await fetch('/api/cron').then(r=>r.json());
  const el=$('cron-list'); el.innerHTML='';
  if (!d.jobs.length) {{
    el.innerHTML='<div style="color:var(--muted);font-size:.85rem;margin-bottom:10px">No jobs scheduled yet.</div>';
    return;
  }}
  for (const j of d.jobs) {{
    const div=document.createElement('div'); div.className='cron-job'; div.dataset.id=j.id;
    const on=j.enabled;
    div.innerHTML=`
      <div class="cron-job-header">
        <span class="cron-job-name">${{esc(j.name)}}</span>
        <span class="cron-job-sched">${{esc(fmtSched(j.schedule))}}</span>
        <button class="cron-toggle ${{on?'on':'off'}}" onclick="toggleCron('${{j.id}}',${{!on}})">${{on?'ON':'OFF'}}</button>
        <button class="cron-run-btn" onclick="runCron('${{j.id}}')">Run</button>
        <button class="cron-del" onclick="delCron('${{j.id}}')">\u2715</button>
      </div>
      <div class="cron-msg">\u201c${{esc(j.message)}}\u201d</div>
      ${{j.nextRunAt ? `<div class="cron-next">Next: ${{fmtTime(j.nextRunAt)}}</div>` : ''}}
      ${{j.lastStatus ? `<div class="cron-status ${{j.lastStatus}}">${{j.lastStatus==='ok'?'\u2713':'\u2717'}} last: ${{fmtTime(j.lastRunAt)}} — ${{j.lastStatus}}${{j.lastError?' ('+esc(j.lastError)+')':''}}</div>` : ''}}
    `;
    el.appendChild(div);
  }}
}}
function cronKindChange() {{
  const v=$('cron-kind').value;
  $('cron-every-row').style.display=v==='every'?'':'none';
  $('cron-expr-row').style.display=v==='cron'?'':'none';
}}
async function addCronJob() {{
  const name=$('cron-name').value.trim();
  const msg=$('cron-msg').value.trim();
  const kind=$('cron-kind').value;
  if(!name||!msg){{alert('Name and message required');return;}}
  const body={{name,message:msg,kind}};
  if(kind==='every') {{
    body.everyMs=parseInt($('cron-every-val').value)*parseInt($('cron-every-unit').value);
    if(body.everyMs<60000){{alert('Minimum 1 minute');return;}}
  }} else {{
    body.expr=$('cron-expr').value.trim();
    if(!body.expr){{alert('Cron expression required');return;}}
  }}
  $('cron-add-btn').disabled=true;
  const r=await fetch('/api/cron',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(body)}});
  if(r.ok){{
    $('cron-name').value='';$('cron-msg').value='';
    loadCron();
  }} else alert('Error: '+await r.text());
  $('cron-add-btn').disabled=false;
}}
async function delCron(id) {{
  if(!confirm('Delete this job?'))return;
  await fetch(`/api/cron/${{id}}`,{{method:'DELETE'}});
  loadCron();
}}
async function toggleCron(id, enabled) {{
  await fetch(`/api/cron/${{id}}/toggle`,{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{enabled}})}});
  loadCron();
}}
async function runCron(id) {{
  const r=await fetch(`/api/cron/${{id}}/run`,{{method:'POST'}});
  const d=await r.json(); alert(d.ok?'Job triggered!':'Job not found');
}}
function esc(s) {{ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }}

// \u2500\u2500 Model panel \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
$('lab-model-display').onclick=()=>{{$('model-panel').classList.add('open');renderModelPanel();}};
$('close-panel').onclick=()=>$('model-panel').classList.remove('open');
document.querySelectorAll('.tab').forEach(t=>{{t.onclick=()=>{{
  document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active')); t.classList.add('active');
  panelTab=t.dataset.tab; $('model-search').value=''; renderModelPanel();
}}}});
$('model-search').addEventListener('input',renderModelPanel);
function renderModelPanel() {{
  const q=$('model-search').value.toLowerCase(); const el=$('model-list'); el.innerHTML='';
  for(const m of allModels[panelTab].filter(m=>m.name.includes(q))){{
    const item=document.createElement('div');
    item.className='model-item'+(m.name===panelSelected?' selected':'');
    item.innerHTML=`<span class="model-name">${{m.name}}</span><span class="badge ${{m.source}}">${{m.source}}</span>`;
    item.onclick=()=>{{panelSelected=m.name;$('apply-model-btn').disabled=false;renderModelPanel();}};
    el.appendChild(item);
  }}
}}
$('apply-model-btn').onclick=()=>{{
  labModel=panelSelected; $('lab-model-display').textContent=labModel;
  $('load-btn').disabled=!selectedSS;
  $('model-panel').classList.remove('open');
  $('apply-model-btn').disabled=true;
}};
// hamburger
$('hamburger').onclick=e=>{{e.stopPropagation();$('nav-links').classList.toggle('open');}};
document.addEventListener('click',e=>{{if(!e.target.closest('nav'))$('nav-links').classList.remove('open');}});
// sidebar drawer
function openSidebar(){{$('sidebar').classList.add('open');$('backdrop').classList.add('open');}}
function closeSidebar(){{$('sidebar').classList.remove('open');$('backdrop').classList.remove('open');}}
$('sidebar-toggle').onclick=e=>{{e.stopPropagation();openSidebar();}};
$('backdrop').onclick=closeSidebar;

init();
</script>
</body></html>"""

