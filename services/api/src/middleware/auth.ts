import { Request, Response, NextFunction } from 'express'

export function requireApiKey(req: Request, res: Response, next: NextFunction): void {
  const apiKey = process.env.API_KEY
  // If no API_KEY is set, auth is disabled (useful for local dev without a key)
  if (!apiKey) {
    next()
    return
  }
  // Accept key from X-Api-Key header or ?key= query param (for EventSource)
  const provided = req.headers['x-api-key'] ?? req.query.key
  if (provided !== apiKey) {
    res.status(401).json({ error: 'Unauthorized' })
    return
  }
  next()
}
