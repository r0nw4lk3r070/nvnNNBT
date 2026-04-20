"""knowledge.py — Knowledge base subsystem for workspaces and teams.

Endpoints:
  POST   /knowledge/{scope}/{slug}/ingest           - ingest all files in inbox/
  GET    /knowledge/{scope}/{slug}/library          - list ingested documents
  DELETE /knowledge/{scope}/{slug}/library/{doc}   - remove a document + its vectors
  GET    /knowledge/{scope}/{slug}/search?q=&n=5   - semantic search

scope: "workspace" or "team"

Ingest pipeline:
  1. Read files from inbox/ (markdown, txt, html, pdf)
  2. Extract + clean text
  3. Chunk (500 tokens / 50-token overlap — approximated by characters: ~2000/200)
  4. Embed each chunk via Ollama /api/embed
  5. Store in vectors.db (sqlite-vec)
  6. Move source file to library/ as .md (cleaned text)

Embedding model: from workspace/team config.json agents.defaults.embedModel,
falling back to EMBED_MODEL env var, falling back to "nomic-embed-text".

sqlite-vec is a loadable extension. We use the sqlite-vec Python package which
bundles the extension and loads it automatically.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import struct
import time
import urllib.request
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel

from routers.events import log_event

# ── Config ────────────────────────────────────────────────────────────────────
WORKSPACES_ROOT = Path(os.environ.get("WORKSPACES_ROOT", "/app/data/workspaces"))
TEAMS_ROOT      = WORKSPACES_ROOT / "teams"
OLLAMA_BASE     = os.environ.get("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
DEFAULT_EMBED_MODEL = os.environ.get("EMBED_MODEL", "nomic-embed-text")

# Chunk size in characters (~2000 chars ≈ 500 tokens for English text)
CHUNK_SIZE    = 2000
CHUNK_OVERLAP = 200

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


# ── Path resolution ───────────────────────────────────────────────────────────

def _scope_root(scope: str, slug: str) -> Path:
    if scope == "workspace":
        p = WORKSPACES_ROOT / slug
    elif scope == "team":
        p = TEAMS_ROOT / slug
    else:
        raise HTTPException(status_code=400, detail="scope must be 'workspace' or 'team'")
    if not p.exists():
        raise HTTPException(status_code=404, detail=f"{scope.capitalize()} '{slug}' not found")
    return p


def _inbox(root: Path) -> Path:
    d = root / "knowledge" / "inbox"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _library(root: Path) -> Path:
    d = root / "knowledge" / "library"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _vectors_db(root: Path) -> Path:
    return root / "knowledge" / "vectors.db"


# ── Embedding ─────────────────────────────────────────────────────────────────

def _embed_model(root: Path) -> str:
    """Read embedModel from config.json, fall back to env/default."""
    cfg_path = root / "config.json"
    if cfg_path.exists():
        try:
            cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
            m = cfg.get("agents", {}).get("defaults", {}).get("embedModel", "")
            if m:
                return m
        except Exception:
            pass
    return DEFAULT_EMBED_MODEL


def _get_embedding(text: str, model: str) -> list[float]:
    """Call Ollama /api/embed and return the embedding vector."""
    payload = json.dumps({"model": model, "input": text}).encode()
    req = urllib.request.Request(
        f"{OLLAMA_BASE}/api/embed",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
            # Ollama /api/embed returns {"embeddings": [[...]]}
            embeddings = data.get("embeddings") or data.get("embedding")
            if isinstance(embeddings, list) and embeddings:
                first = embeddings[0]
                if isinstance(first, list):
                    return first
                return embeddings  # flat list
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Embedding failed: {e}")
    raise HTTPException(status_code=502, detail="Empty embedding response from Ollama")


# ── Text extraction ───────────────────────────────────────────────────────────

def _extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        try:
            import pypdf
            reader = pypdf.PdfReader(str(path))
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        except ImportError:
            raise HTTPException(status_code=500, detail="pypdf not installed — PDF ingestion unavailable")
    elif suffix in (".html", ".htm"):
        raw = path.read_text(encoding="utf-8", errors="replace")
        # Strip tags
        return re.sub(r"<[^>]+>", " ", raw)
    else:
        # markdown, txt, json, etc.
        return path.read_text(encoding="utf-8", errors="replace")


def _chunk_text(text: str) -> list[str]:
    """Split text into overlapping chunks."""
    text = text.strip()
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return [c for c in chunks if c.strip()]


# ── SQLite-vec helpers ────────────────────────────────────────────────────────

def _open_vec_db(db_path: Path):
    """Open a sqlite-vec database, creating tables if needed."""
    import sqlite3
    try:
        import sqlite_vec
    except ImportError:
        raise HTTPException(status_code=500, detail="sqlite-vec not installed in factory container")

    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)

    # Metadata table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            doc      TEXT NOT NULL,
            chunk_i  INTEGER NOT NULL,
            text     TEXT NOT NULL,
            added_at INTEGER NOT NULL DEFAULT (unixepoch())
        )
    """)
    conn.commit()
    return conn


def _ensure_vec_table(conn, dim: int) -> None:
    """Create the vec0 virtual table if it doesn't exist or has wrong dim."""
    conn.execute(f"""
        CREATE VIRTUAL TABLE IF NOT EXISTS vec_chunks
        USING vec0(embedding float[{dim}])
    """)
    conn.commit()


def _pack_vector(v: list[float]) -> bytes:
    return struct.pack(f"{len(v)}f", *v)


# ── Ingest ────────────────────────────────────────────────────────────────────

@router.post("/{scope}/{slug}/ingest")
async def ingest(scope: str, slug: str) -> dict:
    """Ingest all files currently in inbox/. Move processed files to library/."""
    root    = _scope_root(scope, slug)
    inbox   = _inbox(root)
    library = _library(root)
    model   = _embed_model(root)
    db_path = _vectors_db(root)

    files = [f for f in inbox.iterdir() if f.is_file() and not f.name.startswith(".")]
    if not files:
        return {"ok": True, "ingested": 0, "skipped": 0, "message": "inbox is empty"}

    conn = _open_vec_db(db_path)
    ingested = 0
    skipped  = 0
    errors   = []

    for f in files:
        try:
            text = _extract_text(f)
        except Exception as e:
            errors.append(f"{f.name}: extraction failed — {e}")
            skipped += 1
            continue

        chunks = _chunk_text(text)
        if not chunks:
            skipped += 1
            f.rename(library / (f.stem + ".md"))
            continue

        # Get first chunk's embedding to determine dimension
        try:
            first_vec = _get_embedding(chunks[0], model)
        except Exception as e:
            errors.append(f"{f.name}: embedding failed — {e}")
            skipped += 1
            continue

        _ensure_vec_table(conn, len(first_vec))

        doc_name = f.stem  # use stem as doc identifier

        # Remove any existing chunks for this doc (re-ingest = replace)
        existing = conn.execute(
            "SELECT id FROM chunks WHERE doc=?", (doc_name,)
        ).fetchall()
        if existing:
            ids = [str(r[0]) for r in existing]
            conn.execute(f"DELETE FROM chunks WHERE doc=?", (doc_name,))
            conn.execute(
                f"DELETE FROM vec_chunks WHERE rowid IN ({','.join(ids)})"
            )
            conn.commit()

        # Insert all chunks
        vecs = [first_vec] + [_get_embedding(c, model) for c in chunks[1:]]
        for i, (chunk_text, vec) in enumerate(zip(chunks, vecs)):
            cur = conn.execute(
                "INSERT INTO chunks (doc, chunk_i, text) VALUES (?, ?, ?)",
                (doc_name, i, chunk_text),
            )
            rowid = cur.lastrowid
            conn.execute(
                "INSERT INTO vec_chunks (rowid, embedding) VALUES (?, ?)",
                (rowid, _pack_vector(vec)),
            )
        conn.commit()

        # Write cleaned text to library/
        (library / (f.stem + ".md")).write_text(text, encoding="utf-8")
        # Remove from inbox
        f.unlink()
        ingested += 1

    conn.close()

    log_event(
        "knowledge_ingest",
        target_type=scope, target_slug=slug,
        detail=f"Ingested {ingested} files via model {model}. Skipped {skipped}.",
    )
    result: dict = {"ok": True, "ingested": ingested, "skipped": skipped}
    if errors:
        result["errors"] = errors
    return result


# ── List library ──────────────────────────────────────────────────────────────

@router.get("/{scope}/{slug}/library")
async def list_library(scope: str, slug: str) -> dict:
    """List all ingested documents in library/."""
    root    = _scope_root(scope, slug)
    library = _library(root)
    db_path = _vectors_db(root)

    docs = []
    for f in sorted(library.iterdir()):
        if f.is_file() and not f.name.startswith("."):
            # Count chunks in vectors.db
            chunk_count = 0
            if db_path.exists():
                try:
                    import sqlite3
                    conn = sqlite3.connect(str(db_path))
                    row = conn.execute(
                        "SELECT COUNT(*) FROM chunks WHERE doc=?", (f.stem,)
                    ).fetchone()
                    conn.close()
                    chunk_count = row[0] if row else 0
                except Exception:
                    pass
            docs.append({
                "name":     f.stem,
                "file":     f.name,
                "size":     f.stat().st_size,
                "chunks":   chunk_count,
                "modified": int(f.stat().st_mtime),
            })
    return {"docs": docs}


# ── Delete document ───────────────────────────────────────────────────────────

@router.delete("/{scope}/{slug}/library/{doc}")
async def delete_doc(scope: str, slug: str, doc: str) -> dict:
    """Remove a document from library/ and its vectors from vectors.db."""
    root    = _scope_root(scope, slug)
    library = _library(root)
    db_path = _vectors_db(root)

    # Remove library file
    for ext in (".md", ".txt", ".html", ".pdf"):
        f = library / (doc + ext)
        if f.exists():
            f.unlink()
            break

    # Remove from vectors.db
    if db_path.exists():
        try:
            conn = _open_vec_db(db_path)
            rows = conn.execute(
                "SELECT id FROM chunks WHERE doc=?", (doc,)
            ).fetchall()
            if rows:
                ids = [str(r[0]) for r in rows]
                conn.execute("DELETE FROM chunks WHERE doc=?", (doc,))
                conn.execute(
                    f"DELETE FROM vec_chunks WHERE rowid IN ({','.join(ids)})"
                )
                conn.commit()
            conn.close()
        except Exception:
            pass

    log_event("knowledge_delete", target_type=scope, target_slug=slug, detail=f"Deleted doc '{doc}'")
    return {"ok": True, "doc": doc}


# ── Semantic search ───────────────────────────────────────────────────────────

@router.get("/{scope}/{slug}/search")
async def search(scope: str, slug: str, q: str, n: int = 5) -> dict:
    """Semantic search over ingested documents. Returns top-N matching chunks."""
    if not q.strip():
        raise HTTPException(status_code=400, detail="q (query) is required")

    root    = _scope_root(scope, slug)
    db_path = _vectors_db(root)
    model   = _embed_model(root)

    if not db_path.exists():
        return {"results": [], "message": "No knowledge base yet — ingest documents first"}

    query_vec = _get_embedding(q, model)
    packed    = _pack_vector(query_vec)

    try:
        conn = _open_vec_db(db_path)
        # sqlite-vec KNN: WHERE embedding MATCH <blob> AND k = <int>
        rows = conn.execute(
            """
            SELECT c.doc, c.chunk_i, c.text, v.distance
            FROM vec_chunks v
            JOIN chunks c ON c.id = v.rowid
            WHERE v.embedding MATCH ?
              AND k = ?
            ORDER BY v.distance
            """,
            (packed, n),
        ).fetchall()
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vector search failed: {e}")

    return {
        "results": [
            {"doc": r[0], "chunk": r[1], "text": r[2], "distance": r[3]}
            for r in rows
        ]
    }


# ── Upload to inbox ───────────────────────────────────────────────────────────

@router.post("/{scope}/{slug}/inbox")
async def upload_to_inbox(scope: str, slug: str, file: UploadFile = File(...)) -> dict:
    """Upload a file to inbox/ ready for ingestion."""
    root  = _scope_root(scope, slug)
    inbox = _inbox(root)

    safe_name = re.sub(r"[^a-zA-Z0-9._-]", "_", file.filename or "upload")
    dest = inbox / safe_name
    content = await file.read()
    dest.write_bytes(content)

    return {"ok": True, "file": safe_name, "size": len(content)}


# ── List inbox ────────────────────────────────────────────────────────────────

@router.get("/{scope}/{slug}/inbox")
async def list_inbox(scope: str, slug: str) -> dict:
    """List files waiting in inbox/."""
    root  = _scope_root(scope, slug)
    inbox = _inbox(root)

    files = [
        {"name": f.name, "size": f.stat().st_size}
        for f in sorted(inbox.iterdir())
        if f.is_file() and not f.name.startswith(".")
    ]
    return {"files": files}
