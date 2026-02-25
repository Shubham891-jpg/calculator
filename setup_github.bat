@echo off
echo ============================================================
echo GitHub Repository Setup
echo ============================================================
echo.
echo Current remote: https://github.com/Shubham891-jpg/ticket2.git
echo.
echo This repository was not found. Please:
echo 1. Create a new repository on GitHub
echo 2. Copy the repository URL
echo 3. Run this script again with the new URL
echo.
echo ============================================================
echo.

set /p REPO_URL="Enter your GitHub repository URL (or press Enter to skip): "

if "%REPO_URL%"=="" (
    echo.
    echo Skipped. Create your repository first at: https://github.com/new
    echo Then run this script again.
    pause
    exit /b
)

echo.
echo Updating git remote to: %REPO_URL%
git remote set-url origin %REPO_URL%

echo.
echo Verifying remote...
git remote -v

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo ============================================================
echo Done! Your code is now on GitHub.
echo Next: Deploy on Render at https://render.com
echo ============================================================
pause
