@echo off
echo.
echo [EUAI Site] Restarting on port 6163...
echo Killing any existing processes...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":6163 "') do (
    echo   Killing PID %%a
    taskkill /F /PID %%a 2>nul
)
timeout /t 3 /nobreak >nul

echo Starting new server (new console window)...
cd /d "%~dp0"
start "EUAI Research Site - 6163" python server.py

echo.
echo Done. Site should be available at http://localhost:6163/library
echo New features deployed:
echo   • Real-time search bar (titles, meta, descriptions)
echo   • Key Persons page (/key-persons)
echo   • Improved EN/NL toggle + dynamic scanning
echo   • Inline PDF viewer for all regulations
echo.
pause
