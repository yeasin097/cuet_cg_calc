@echo off
REM Set variables
set REPO_URL=https://github.com/yeasin097/cuet_cg_calc.git
set EXT_DIR=%cd%\cuet_cg_calc
set CUET_URL=https://course.cuet.ac.bd/index.php

REM Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Git is not installed or not in PATH.
    pause
    exit /b
)

REM Clone the repo if not already present
if not exist "%EXT_DIR%" (
    echo Cloning the cuet_cg_calc extension from GitHub...
    git clone %REPO_URL% "%EXT_DIR%"
) else (
    echo Extension already cloned. Skipping clone...
)

REM Set Chrome path (adjust if Chrome is installed elsewhere)
set CHROME_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"

REM Check if Chrome exists
if not exist %CHROME_PATH% (
    echo Chrome not found at %CHROME_PATH%
    pause
    exit /b
)

REM Launch Chrome with the extension and open the CUET course page
echo Launching Chrome with cuet_cg_calc extension and opening course page...
start "" %CHROME_PATH% --load-extension="%EXT_DIR%" --app=%CUET_URL%

pause
