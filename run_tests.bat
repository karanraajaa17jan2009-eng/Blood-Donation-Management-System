@echo off
echo ======================================================================
echo Running Comprehensive Test and Verification Suite...
echo ======================================================================
if exist .\.venv\Scripts\python.exe (
    .\.venv\Scripts\python.exe verify_all_requirements.py
) else (
    python verify_all_requirements.py
)
echo.
pause

