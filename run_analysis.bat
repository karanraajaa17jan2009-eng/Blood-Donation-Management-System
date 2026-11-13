@echo off
echo ======================================================================
echo Running Python Data Science and Visualization Pipeline...
echo ======================================================================
if exist .\.venv\Scripts\python.exe (
    .\.venv\Scripts\python.exe python\main_analysis.py
) else (
    python python\main_analysis.py
)
echo.
pause

