import Database from 'better-sqlite3'
import path from 'path'
import fs from 'fs'

const DB_PATH = process.env.DB_PATH ?? '/app/data/nanobot.db'

fs.mkdirSync(path.dirname(DB_PATH), { recursive: true })

export const db = new Database(DB_PATH)

export function initDb(): void {
  db.pragma('journal_mode = WAL')
  db.pragma('foreign_keys = ON')

  db.exec(`
    CREATE TABLE IF NOT EXISTS agents (
      slug          TEXT PRIMARY KEY,
      display_name  TEXT    NOT NULL,
      model         TEXT    NOT NULL DEFAULT 'qwen3:1.7b',
      port          INTEGER NOT NULL,
      container     TEXT    NOT NULL,
      status        TEXT    NOT NULL DEFAULT 'stopped',
      created_at    TEXT    NOT NULL DEFAULT (datetime('now')),
      started_at    TEXT
    );
  `)
}
