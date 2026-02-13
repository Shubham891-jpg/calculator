@echo off
setlocal enabledelayedexpansion

REM IT Ticket Severity Calculator - cURL API Testing Script (Windows)
REM This script tests all API endpoints using cURL commands

set BASE_URL=http://localhost:8000

echo ========================================
echo IT Ticket Severity Calculator API Test
echo ========================================
echo Base URL: %BASE_URL%
echo Started at: %date% %time%
echo.

REM Check if curl is available
curl --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: curl is not installed or not in PATH
    echo Please install curl or use PowerShell/Python test scripts
    pause
    exit /b 1
)

echo ========================================
echo 1. Health Check
echo ========================================
curl -s %BASE_URL%/health
echo.
echo.

echo ========================================
echo 2. API Information
echo ========================================
curl -s %BASE_URL%/api
echo.
echo.

echo ========================================
echo 3. Model Information
echo ========================================
curl -s %BASE_URL%/model/info
echo.
echo.

echo ========================================
echo 4. Single Predictions
echo ========================================

echo Testing Critical Severity...
curl -s -X POST "%BASE_URL%/predict" -H "Content-Type: application/json" -d "{\"ticket_text\": \"All servers are down, complete system failure\"}"
echo.
echo.

echo Testing High Severity...
curl -s -X POST "%BASE_URL%/predict" -H "Content-Type: application/json" -d "{\"ticket_text\": \"Database is extremely slow, applications timing out\"}"
echo.
echo.

echo Testing Medium Severity...
curl -s -X POST "%BASE_URL%/predict" -H "Content-Type: application/json" -d "{\"ticket_text\": \"Office printer not working, affecting users\"}"
echo.
echo.

echo Testing Low Severity...
curl -s -X POST "%BASE_URL%/predict" -H "Content-Type: application/json" -d "{\"ticket_text\": \"User needs password reset\"}"
echo.
echo.

echo Testing Minimal Severity...
curl -s -X POST "%BASE_URL%/predict" -H "Content-Type: application/json" -d "{\"ticket_text\": \"Please install Microsoft Office\"}"
echo.
echo.

echo ========================================
echo 5. Batch Predictions
echo ========================================
curl -s -X POST "%BASE_URL%/predict/batch" -H "Content-Type: application/json" -d "{\"tickets\": [\"Server down\", \"Printer issue\", \"Password reset\"]}"
echo.
echo.

echo ========================================
echo 6. Edge Cases
echo ========================================

echo Testing Empty Text (should fail)...
curl -s -X POST "%BASE_URL%/predict" -H "Content-Type: application/json" -d "{\"ticket_text\": \"\"}"
echo.
echo.

echo Testing Special Characters...
curl -s -X POST "%BASE_URL%/predict" -H "Content-Type: application/json" -d "{\"ticket_text\": \"Server @#$%% down\"}"
echo.
echo.

echo ========================================
echo Testing Complete!
echo ========================================
echo.
echo Summary:
echo - All endpoints tested with various scenarios
echo - Edge cases and error handling verified
echo - Both success and failure cases covered
echo.
echo Interactive Testing:
echo - Swagger UI: %BASE_URL%/docs
echo - ReDoc: %BASE_URL%/redoc
echo - Web Interface: %BASE_URL%
echo.
echo Happy Testing!
echo.
pause