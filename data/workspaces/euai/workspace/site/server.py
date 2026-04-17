"""EUAI Research Site — FastAPI server serving markdown content as HTML."""

import re
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import markdown
import uvicorn

BASE = Path(__file__).parent
CONTENT = BASE / "content"
STATIC = BASE / "static"
LIBRARY = BASE.parent / "library"

app = FastAPI(title="EUAI Research Site")

app.mount("/static", StaticFiles(directory=str(STATIC)), name="static")

# ── Regulation metadata ──────────────────────────────────────────────────────

REGULATIONS = {
    "ai-act":    {"id": "32024R1689", "name": "AI Act",          "type": "Regulation", "year": 2024},
    "gdpr":      {"id": "32016R0679", "name": "GDPR",            "type": "Regulation", "year": 2016},
    "nis2":      {"id": "32022R2555", "name": "NIS2",            "type": "Directive",  "year": 2022},
    "dora":      {"id": "32022R2554", "name": "DORA",            "type": "Regulation", "year": 2022},
    "data-act":  {"id": "32023R2854", "name": "Data Act",        "type": "Regulation", "year": 2023},
    "cra":       {"id": "32024R1183", "name": "Cyber Resilience Act", "type": "Regulation", "year": 2024},
    "dga":       {"id": "32024R2847", "name": "Data Governance Act", "type": "Regulation", "year": 2024},
}

# ── Helpers ────────────────────────────────────────────────────────────────────

def get_nav():
    """Build navigation from content directory .md files."""
    pages = []
    if not CONTENT.exists():
        return pages
    for f in sorted(CONTENT.glob("*.md")):
        slug = f.stem
        if slug in ("index", "library"):
            continue
        title = slug.replace("-", " ").title()
        with open(f, "r", encoding="utf-8") as fh:
            first_line = fh.readline().strip()
            if first_line.startswith("# "):
                title = first_line[2:].strip()
        pages.append({"slug": slug, "title": title})
    return pages


def scan_library():
    """Dynamically scan the library directory and return data for all tabs."""
    data = {"legislation": [], "research": [], "sectors": []}

    # Legislation (EN + NL)
    for lang in ["EN", "NL"]:
        lang_dir = LIBRARY / "eu-laws" / lang
        if lang_dir.exists():
            for txt_file in sorted(lang_dir.glob("*.txt")):
                code = txt_file.stem.split("_")[0]
                reg = REGULATIONS.get(code.lower().replace("r", "").replace("l", ""), {})
                name = reg.get("name", code)
                meta = f"Regulation (EU) {code[:4]}/{code[4:]} • {lang}"
                data["legislation"].append({
                    "title": name,
                    "meta": meta,
                    "desc": f"Official consolidated text ({lang}).",
                    "en_link": f"/library/view/eu-laws/EN/{txt_file.stem}",
                    "nl_link": f"/library/view/eu-laws/NL/{txt_file.stem}" if (lang == "EN" and (LIBRARY / "eu-laws" / "NL" / f"{txt_file.stem}.txt").exists()) else None,
                    "lang": lang
                })

    # Research & Analysis + Sector Guides
    for lang_dir_name in ["english", "nederlands"]:
        research_dir = LIBRARY / "research" / lang_dir_name
        if research_dir.exists():
            for md_file in sorted(research_dir.glob("*.md")):
                title = md_file.stem.replace("-", " ").title()
                content = md_file.read_text(encoding="utf-8")
                if content.startswith("# "):
                    title = content.split("\n")[0][2:].strip()
                is_sector = md_file.stem.upper().startswith(("S", "T"))
                item = {
                    "title": title,
                    "meta": f"{lang_dir_name.title()} • {'Sector guide' if is_sector else 'Deep analysis'}",
                    "desc": "Practical compliance and analysis.",
                    "link": f"/library/view/research/{lang_dir_name}/{md_file.stem}"
                }
                if is_sector:
                    data["sectors"].append(item)
                else:
                    data["research"].append(item)

    return data


def scan_library():
    """Dynamically scan the library directory and return data for all tabs."""
    data = {"legislation": [], "research": [], "sectors": []}

    # Legislation (EN + NL)
    for lang in ["EN", "NL"]:
        lang_dir = LIBRARY / "eu-laws" / lang
        if lang_dir.exists():
            for txt_file in sorted(lang_dir.glob("*.txt")):
                code = txt_file.stem.split("_")[0]
                reg = REGULATIONS.get(code.lower().replace("r", "").replace("l", ""), {})
                name = reg.get("name", code)
                meta = f"Regulation (EU) {code[:4]}/{code[4:]} • {lang}"
                data["legislation"].append({
                    "title": name,
                    "meta": meta,
                    "desc": f"Official consolidated text ({lang}).",
                    "en_link": f"/library/view/eu-laws/EN/{txt_file.stem}",
                    "nl_link": f"/library/view/eu-laws/NL/{txt_file.stem}" if lang == "EN" else None,
                    "lang": lang
                })

    # Research & Analysis + Sector Guides
    research_dir = LIBRARY / "research" / "english"
    if research_dir.exists():
        for md_file in sorted(research_dir.glob("*.md")):
            title = md_file.stem.replace("-", " ").title()
            if md_file.stem.startswith("0"):
                title = md_file.read_text(encoding="utf-8").split("\n")[0].replace("#", "").strip()
            is_sector = md_file.stem.startswith(("S", "T"))
            item = {
                "title": title,
                "meta": "Deep analysis" if not is_sector else "Sector guide",
                "desc": "Practical compliance and analysis.",
                "link": f"/library/view/research/english/{md_file.stem}"
            }
            if is_sector:
                data["sectors"].append(item)
            else:
                data["research"].append(item)

    return data


def render_markdown(content: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list"],
        output_format="html5",
    )
    return md.convert(content)


def render_page(slug: str) -> str:
    md_path = CONTENT / f"{slug}.md"
    if not md_path.exists():
        raise HTTPException(status_code=404, detail=f"Page '{slug}' not found")

    content = md_path.read_text(encoding="utf-8")
    body_html = render_markdown(content)
    nav = get_nav()

    title = slug.replace("-", " ").title()
    first_line = content.strip().split("\n")[0]
    if first_line.startswith("# "):
        title = first_line[2:].strip()

    nav_html = ""
    for page in nav:
        active = " active" if page["slug"] == slug else ""
        nav_html += f'<a href="/{page["slug"]}" class="nav-link{active}">{page["title"]}</a>\n'

    template = (BASE / "templates" / "page.html").read_text(encoding="utf-8")
    return template.replace("{{TITLE}}", title).replace("{{NAV}}", nav_html).replace("{{CONTENT}}", body_html)


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(content=render_page("index"))


@app.get("/{slug}", response_class=HTMLResponse)
async def catch_all_page(slug: str):
    """Catch routes like /ai-act, /gdpr, /nis2, /key-persons"""
    if slug in ("library", "library/browse", "static", "health", "api", "favicon.ico"):
        raise HTTPException(status_code=404, detail="Not Found")
    try:
        return HTMLResponse(content=render_page(slug))
    except Exception:
        raise HTTPException(status_code=404, detail=f"Page '{slug}' not found")


@app.get("/library", response_class=HTMLResponse)
@app.get("/library/browse", response_class=HTMLResponse)
async def library_browse():
    """Beautiful library browser with tabs and cards."""
    if not LIBRARY.exists():
        raise HTTPException(status_code=404, detail="Library not found")

    template = (BASE / "templates" / "page.html").read_text(encoding="utf-8")
    nav = get_nav()
    nav_html = "".join(
        f'<a href="/{page["slug"]}" class="nav-link">{page["title"]}</a>\n' for page in nav
    )
    nav_html += '<a href="/library" class="nav-link active">Library</a>\n'

    library_data = scan_library()

    html = f"""
    <h1>LocAI Library</h1>
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
        <p class="intro" style="margin:0;">Curated collection of EU digital regulation, research and sector guidance.</p>
        <input type="text" id="search-input" placeholder="Search legislation, research, persons..." 
               onkeyup="if(event.key === 'Enter') performSearch()" 
               style="padding:0.6rem 1rem; width:280px; background:#1e293b; border:1px solid #475569; border-radius:8px; color:#e2e8f0; font-size:0.95rem;">
        <button onclick="performSearch()" class="btn" style="padding:0.6rem 1.2rem; margin-left:0.5rem;">Search</button>
    </div>

    <div class="tabs">
        <div class="tab active" onclick="switchTab(0)">Legislation</div>
        <div class="tab" onclick="switchTab(1)">Research &amp; Analysis</div>
        <div class="tab" onclick="switchTab(2)">Sector Guides</div>
    </div>

    <div id="tab-content">
        <!-- Populated by JS -->
    </div>

    <script>
    let currentLang = 'EN';
    let libraryData = {library_data};

    function renderLegislation() {{
        let html = `<h2>EU Legislation</h2><div class="library-grid">`;
        libraryData.legislation.forEach(item => {{
            if (currentLang === 'ALL' || item.lang === currentLang) {{
                html += `
                    <div class="library-card">
                        <h3>${{item.title}}</h3>
                        <div class="meta">${{item.meta}}</div>
                        <p class="description">${{item.desc}}</p>
                        <a href="${{item.en_link}}" class="btn">Read English</a>
                `;
                if (item.nl_link) {{
                    html += `<a href="${{item.nl_link}}" class="btn">Lees Nederlands</a>`;
                }}
                html += `</div>`;
            }}
        }});
        html += `</div>`;
        return html;
    }}

    function switchTab(n) {{
        const tabs = document.querySelectorAll('.tab');
        tabs.forEach(t => t.classList.remove('active'));
        tabs[n].classList.add('active');

        const content = document.getElementById('tab-content');
        if (n === 0) {{
            content.innerHTML = renderLegislation();
        }} else if (n === 1) {{
            let html = `<h2>Research &amp; In-depth Analysis</h2><div class="library-grid">`;
            libraryData.research.forEach(item => {{
                html += `
                    <div class="library-card">
                        <h3>${{item.title}}</h3>
                        <div class="meta">${{item.meta}}</div>
                        <p class="description">${{item.desc}}</p>
                        <a href="${{item.link}}" class="btn">Read Analysis</a>
                    </div>`;
            }});
            html += `</div>`;
            content.innerHTML = html;
        }} else {{
            let html = `<h2>Sector Guides</h2><div class="library-grid">`;
            libraryData.sectors.forEach(item => {{
                html += `
                    <div class="library-card">
                        <h3>${{item.title}}</h3>
                        <div class="meta">${{item.meta}}</div>
                        <p class="description">${{item.desc}}</p>
                        <a href="${{item.link}}" class="btn">Open Guide</a>
                    </div>`;
            }});
            html += `</div><p style="margin-top:2rem; font-size:0.9rem; color:#64748b;">Full set of 14 sector guides available.</p>`;
            content.innerHTML = html;
        }}
    }}

    function toggleLanguage() {{
        const toggle = document.getElementById('lang-toggle');
        if (currentLang === 'EN') {{
            currentLang = 'ALL';
            toggle.textContent = '🌐 All Languages';
        }} else if (currentLang === 'ALL') {{
            currentLang = 'NL';
            toggle.textContent = '🌐 Nederlands';
        }} else {{
            currentLang = 'EN';
            toggle.textContent = '🌐 English';
        }}
        // Refresh current tab (legislation only for now)
        const activeTab = document.querySelector('.tab.active');
        if (activeTab && activeTab.textContent.includes('Legislation')) {{
            document.getElementById('tab-content').innerHTML = renderLegislation();
        }}
    }}

    // Load first tab on start
    window.onload = () => {{
        switchTab(0);
        document.getElementById('search-input').focus();
    }};

    function performSearch() {{
        const query = document.getElementById('search-input').value.toLowerCase().trim();
        if (!query) {{
            switchTab(0); // reset to legislation
            return;
        }}

        let resultsHTML = `<h2>Search Results for "${{query}}"</h2><div class="library-grid">`;
        let found = 0;

        // Search legislation
        libraryData.legislation.forEach(item => {{
            if (item.title.toLowerCase().includes(query) || item.meta.toLowerCase().includes(query)) {{
                resultsHTML += `
                    <div class="library-card">
                        <h3>${{item.title}}</h3>
                        <div class="meta">${{item.meta}}</div>
                        <p class="description">${{item.desc}}</p>
                        <a href="${{item.en_link}}" class="btn">Read English</a>
                `;
                if (item.nl_link) resultsHTML += `<a href="${{item.nl_link}}" class="btn">Lees Nederlands</a>`;
                resultsHTML += `</div>`;
                found++;
            }}
        }});

        // Search research + sectors
        [...libraryData.research, ...libraryData.sectors].forEach(item => {{
            if (item.title.toLowerCase().includes(query) || item.meta.toLowerCase().includes(query) || item.desc.toLowerCase().includes(query)) {{
                resultsHTML += `
                    <div class="library-card">
                        <h3>${{item.title}}</h3>
                        <div class="meta">${{item.meta}}</div>
                        <p class="description">${{item.desc}}</p>
                        <a href="${{item.link}}" class="btn">Open Document</a>
                    </div>`;
                found++;
            }}
        }});

        if (found === 0) {{
            resultsHTML += `<p style="grid-column: 1 / -1; text-align:center; padding:3rem; color:#64748b;">No matches found for <strong>${{query}}</strong>. Try broader terms like "AI Act", "GDPR", "smart home" or "Virkkunen".</p>`;
        }}

        resultsHTML += `</div>`;
        document.getElementById('tab-content').innerHTML = resultsHTML;
    }}
    </script>
    """

    return HTMLResponse(content=template.replace("{{TITLE}}", "LocAI Library").replace("{{NAV}}", nav_html).replace("{{CONTENT}}", html))


@app.get("/library/view/{path:path}", response_class=HTMLResponse)
async def library_view(path: str):
    file_path = LIBRARY / path
    if not file_path.exists():
        for ext in (".txt", ".md"):
            candidate = file_path.parent / (file_path.stem + ext)
            if candidate.exists():
                file_path = candidate
                break

    if not file_path.exists() or not str(file_path).startswith(str(LIBRARY)):
        raise HTTPException(status_code=404, detail="File not found")

    content = file_path.read_text(encoding="utf-8")
    is_markdown = file_path.suffix.lower() == ".md"

    template = (BASE / "templates" / "page.html").read_text(encoding="utf-8")
    nav = get_nav()
    nav_html = "".join(f'<a href="/{p["slug"]}" class="nav-link">{p["title"]}</a>\n' for p in nav)
    nav_html += '<a href="/library" class="nav-link active">Library</a>\n'

    if is_markdown:
        body_html = render_markdown(content)
    else:
        # PDF / TXT viewer
        if file_path.suffix.lower() == ".pdf":
            body_html = f'''
                <h2>{file_path.name}</h2>
                <div style="height:80vh; border:1px solid #334155; border-radius:8px; overflow:hidden; background:#111827;">
                    <embed src="/library/download/{path}" type="application/pdf" width="100%" height="100%" style="border:none;">
                </div>
                <p style="margin-top:1rem; text-align:center;">
                    <a href="/library/download/{path}" class="btn" style="background:var(--accent);">Download PDF</a>
                </p>
            '''
        else:
            body_html = f"<pre><code>{content}</code></pre>"

    title = file_path.stem.replace("_", " ").replace("EN", "").replace("NL", "").strip()
    return HTMLResponse(content=template.replace("{{TITLE}}", title).replace("{{NAV}}", nav_html).replace("{{CONTENT}}", body_html))


@app.get("/library/download/{path:path}")
async def library_download(path: str):
    file_path = LIBRARY / path
    if not file_path.exists() or not str(file_path).startswith(str(LIBRARY)):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(str(file_path), filename=file_path.name)


# ── API ───────────────────────────────────────────────────────────────────────

@app.get("/api/pages")
async def api_pages():
    return {"pages": get_nav()}


@app.get("/api/content/{slug}")
async def api_content(slug: str):
    md_path = CONTENT / f"{slug}.md"
    if not md_path.exists():
        raise HTTPException(status_code=404, detail=f"Page '{slug}' not found")
    return {"slug": slug, "content": md_path.read_text(encoding="utf-8")}


@app.get("/api/library")
async def api_library():
    return {"status": "ok", "message": "Library endpoint ready — use /library/browse"}


@app.get("/health")
async def health():
    return {"status": "ok", "service": "euai-site", "port": 6163}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6163)
