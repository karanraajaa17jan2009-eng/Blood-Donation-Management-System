@echo off
title Blood Bank SQL Query & Table Viewer - Scenario 15
color 0b
echo ===============================================================================
echo      BLOOD DONATION MANAGEMENT SYSTEM - SQL QUERY & TABLE RUNNER
echo      Scenario 15 - Database Management Systems (25ITT31)
echo      Student: Karan Raajaa V | Reg No: 732925ITR045 | Class: 25IT3A
echo ===============================================================================
echo.

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" python/run_sql_queries.py %*
) else (
    python python/run_sql_queries.py %*
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] SQL Query execution encountered an error.
)
pause
