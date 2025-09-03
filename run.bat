@echo off
chcp 65001 >nul
SETLOCAL ENABLEDELAYEDEXPANSION

REM Set paths
SET VENV_DIR=%~dp0.venv
SET PYTHON_EXE=%VENV_DIR%\Scripts\python.exe
SET SCRIPT_DIR=%~dp0

REM Check if venv exists
IF NOT EXIST "%PYTHON_EXE%" (
    echo ❌ Virtual environment .venv not found!
    echo Please run 'python -m venv .venv' and 'pip install -r requirements.txt' first.
    pause
    exit /b 1
)
echo ✅ Virtual environment found.

:MENU
CLS
echo =====================================
echo       💻 Attendance Export System
echo =====================================
echo.
echo 1. Export data for a specific month (exportwithYearandMonth.py)
echo 2. Export all records (ExportAll.py)
echo 0. Exit the program
echo.
set /p choice=Please enter your choice:

IF "%choice%"=="1" (
    echo ✅ Running exportwithYearandMonth.py ...
    "%PYTHON_EXE%" "%SCRIPT_DIR%exportwithYearandMonth.py"
    pause
    GOTO MENU
) ELSE IF "%choice%"=="2" (
    echo ✅ Running ExportAll.py ...
    "%PYTHON_EXE%" "%SCRIPT_DIR%ExportAll.py"
    pause
    GOTO MENU
) ELSE IF "%choice%"=="0" (
    echo 👋 Goodbye!
    pause
    exit
) ELSE (
    echo ❌ Invalid option!
    pause
    GOTO MENU
)
