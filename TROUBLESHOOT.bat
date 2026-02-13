@echo off
echo ========================================
echo IT Ticket Severity Calculator
echo Troubleshooting Tool
echo ========================================
echo.

:menu
echo What issue are you experiencing?
echo.
echo 1. Server won't start
echo 2. Port 8000 already in use
echo 3. Import errors / Missing packages
echo 4. Model not found errors
echo 5. Web interface can't connect to API
echo 6. Run full diagnostic
echo 7. Exit
echo.
set /p choice="Enter your choice (1-7): "

if "%choice%"=="1" goto server_wont_start
if "%choice%"=="2" goto port_in_use
if "%choice%"=="3" goto import_errors
if "%choice%"=="4" goto model_not_found
if "%choice%"=="5" goto web_cant_connect
if "%choice%"=="6" goto full_diagnostic
if "%choice%"=="7" goto end
goto menu

:server_wont_start
echo.
echo === Troubleshooting: Server Won't Start ===
echo.
echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Solution: Install Python from https://www.python.org/
    goto menu
)
echo.
echo Checking dependencies...
python -c "import fastapi" 2>nul
if %errorlevel% neq 0 (
    echo ❌ FastAPI not installed
    echo Solution: Run 'python -m pip install -r requirements.txt'
    goto menu
)
echo ✅ Dependencies look good
echo.
echo Try running: python run_server.py
echo.
pause
goto menu

:port_in_use
echo.
echo === Troubleshooting: Port 8000 Already in Use ===
echo.
echo Finding processes using port 8000...
netstat -ano | findstr ":8000"
echo.
echo To kill the process, note the PID (last column) and run:
echo taskkill /F /PID [PID_NUMBER]
echo.
echo Or kill all Python processes:
echo taskkill /F /IM python.exe
echo.
pause
goto menu

:import_errors
echo.
echo === Troubleshooting: Import Errors ===
echo.
echo Reinstalling all dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt --force-reinstall
echo.
if %errorlevel% equ 0 (
    echo ✅ Dependencies reinstalled successfully
) else (
    echo ❌ Failed to install dependencies
    echo Try running as Administrator
)
echo.
pause
goto menu

:model_not_found
echo.
echo === Troubleshooting: Model Not Found ===
echo.
echo Checking model files...
if exist "models\severity_model.pkl" (
    echo ✅ severity_model.pkl found
) else (
    echo ❌ severity_model.pkl NOT FOUND
)
if exist "models\severity_scaler.pkl" (
    echo ✅ severity_scaler.pkl found
) else (
    echo ❌ severity_scaler.pkl NOT FOUND
)
if exist "models\embeddings_info.pkl" (
    echo ✅ embeddings_info.pkl found
) else (
    echo ❌ embeddings_info.pkl NOT FOUND
)
echo.
echo If models are missing, you need to train them first.
echo The models should already be included in the project.
echo.
pause
goto menu

:web_cant_connect
echo.
echo === Troubleshooting: Web Interface Can't Connect ===
echo.
echo Checking if server is running...
curl -s http://localhost:8000/health >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Server is running and responding
    echo.
    echo The issue might be:
    echo 1. Browser cache - Press Ctrl+Shift+Delete and clear cache
    echo 2. Firewall blocking - Check Windows Firewall settings
    echo 3. Try a different browser
    echo 4. Try http://127.0.0.1:8000 instead of localhost
) else (
    echo ❌ Server is NOT running
    echo.
    echo Solution: Start the server first
    echo Run: START_SERVER_HERE.bat
)
echo.
pause
goto menu

:full_diagnostic
echo.
echo === Running Full Diagnostic ===
echo.
echo [1/7] Python Version:
python --version
echo.
echo [2/7] Installed Packages:
python -m pip list | findstr "fastapi uvicorn scikit-learn sentence-transformers"
echo.
echo [3/7] Model Files:
dir /b models\*.pkl 2>nul
echo.
echo [4/7] Static Files:
dir /b static\*.html 2>nul
echo.
echo [5/7] Port 8000 Status:
netstat -ano | findstr ":8000"
if %errorlevel% neq 0 echo Port 8000 is available
echo.
echo [6/7] Server Health Check:
curl -s http://localhost:8000/health 2>nul
if %errorlevel% neq 0 echo Server is not running
echo.
echo [7/7] Disk Space:
dir models
echo.
echo === Diagnostic Complete ===
echo.
pause
goto menu

:end
echo.
echo Exiting troubleshooter...
exit /b 0
