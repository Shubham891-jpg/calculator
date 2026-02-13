@echo off
echo ========================================
echo IT Ticket Severity Calculator
echo Setup Validation
echo ========================================
echo.

echo [1/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)
python --version
echo ✅ Python is installed
echo.

echo [2/5] Checking required packages...
python -c "import fastapi, uvicorn, sklearn, sentence_transformers" >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Required packages are missing
    echo Installing dependencies...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ❌ Failed to install dependencies
        pause
        exit /b 1
    )
)
echo ✅ All required packages are installed
echo.

echo [3/5] Checking model files...
if not exist "models\severity_model.pkl" (
    echo ❌ Model file not found: models\severity_model.pkl
    echo Please train the model first
    pause
    exit /b 1
)
if not exist "models\severity_scaler.pkl" (
    echo ❌ Scaler file not found: models\severity_scaler.pkl
    echo Please train the model first
    pause
    exit /b 1
)
if not exist "models\embeddings_info.pkl" (
    echo ❌ Embeddings file not found: models\embeddings_info.pkl
    echo Please train the model first
    pause
    exit /b 1
)
echo ✅ All model files are present
echo.

echo [4/5] Checking static files...
if not exist "static\index.html" (
    echo ❌ Web interface not found: static\index.html
    pause
    exit /b 1
)
echo ✅ Web interface files are present
echo.

echo [5/5] Checking port availability...
netstat -ano | findstr ":8000" >nul 2>&1
if %errorlevel% equ 0 (
    echo ⚠️  Port 8000 is already in use
    echo The server might already be running or another application is using port 8000
    echo.
) else (
    echo ✅ Port 8000 is available
    echo.
)

echo ========================================
echo ✅ VALIDATION COMPLETE
echo ========================================
echo.
echo Your setup is ready! You can now:
echo   1. Run START_SERVER_HERE.bat to start the server
echo   2. Run test_api_endpoints.py to test the API
echo.
pause
