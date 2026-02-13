@echo off
echo ========================================
echo IT Ticket Severity Calculator
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check if required packages are installed
echo Checking dependencies...
python -c "import fastapi, uvicorn, sklearn, sentence_transformers" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Some packages are missing
    echo Installing dependencies...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed
    echo.
)

REM Check if models exist
if not exist "models\severity_model.pkl" (
    echo ❌ ERROR: Model files not found
    echo Please ensure the models folder contains the trained models
    pause
    exit /b 1
)

echo ✅ All checks passed
echo.
echo Starting server...
echo.
echo The server will be available at:
echo   http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python run_server.py

pause
