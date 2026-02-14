@echo off
REM ==========================================
REM Valentine's Day App Launcher
REM Created with love for Valentine 2026
REM ==========================================

REM Set window title
title Valentine's Day Adventure - Running...

REM Change to app directory
cd /d "d:\valentine vaniaa"

REM Check if Python exists
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ================================================================
    echo ERROR: Python is not installed or not in PATH!
    echo ================================================================
    echo.
    echo Please install Python from: https://www.python.org/downloads
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    echo After installing Python, try again.
    echo ================================================================
    echo.
    pause
    exit /b 1
)

REM Check if valentine_app.py exists
if not exist valentine_app.py (
    echo.
    echo ================================================================
    echo ERROR: valentine_app.py not found!
    echo ================================================================
    echo.
    echo Make sure you are in the correct folder:
    echo d:\valentine vaniaa
    echo.
    echo Or edit this file to point to correct location.
    echo ================================================================
    echo.
    pause
    exit /b 1
)

REM Run the application
echo.
echo ================================================================
echo Valentine's Day Adventure - Starting...
echo ================================================================
echo.
echo Good luck! 💕
echo.
echo This window will close when you close the app.
echo ================================================================
echo.

python valentine_app.py

REM If we're here, app was closed
echo.
echo ================================================================
echo Application closed. Goodbye! 💕
echo ================================================================
echo.
pause
