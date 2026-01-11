@echo off
echo Starting Li-Taylored CV Backend...
start cmd /k "cd backend && python main.py"

timeout /t 3 /nobreak

echo Starting Li-Taylored CV Frontend...
start cmd /k "npm run dev"

echo.
echo Both servers are starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
