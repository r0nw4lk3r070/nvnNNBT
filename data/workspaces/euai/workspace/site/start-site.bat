@echo off
echo Killing any existing process on port 6163...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":6163"') do (
    echo Killing PID %%a
    taskkill /F /PID %%a 2>nul
)
timeout /t 2 /nobreak >nul

echo Starting EUAI Research Site on http://localhost:6163
cd /d "%~dp0"
python server.py
pause