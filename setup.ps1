# setup.ps1 — first-time setup for Windows
# Creates .env from .env.example and auto-fills HOST_PROJECT_PATH.

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$EnvFile    = Join-Path $ScriptDir ".env"
$ExampleFile = Join-Path $ScriptDir ".env.example"

if (Test-Path $EnvFile) {
    Write-Host ".env already exists — skipping creation."
    Write-Host "Edit $EnvFile manually if needed."
    exit 0
}

# Convert Windows backslashes to forward slashes (Docker expects this)
$ProjectPath = $ScriptDir -replace '\\', '/'

Copy-Item $ExampleFile $EnvFile

# Replace empty HOST_PROJECT_PATH= line with the actual path
(Get-Content $EnvFile) -replace '^HOST_PROJECT_PATH=$', "HOST_PROJECT_PATH=$ProjectPath" |
    Set-Content $EnvFile

Write-Host "Created .env with HOST_PROJECT_PATH=$ProjectPath"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Review and adjust .env (Ollama URL, API keys, ports)"
Write-Host "  2. docker compose up -d --build"
