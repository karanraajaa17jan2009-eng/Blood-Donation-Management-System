@echo off
echo ======================================================================
echo Launching Blood Donation Management Interactive Website...
echo Opening in default browser at http://localhost:8000
echo (Press Ctrl+C to stop local server)
echo ======================================================================
start "" http://localhost:8000
if exist .\.venv\Scripts\python.exe (
    .\.venv\Scripts\python.exe -m http.server 8000
) else (
    python -m http.server 8000
)
pause
