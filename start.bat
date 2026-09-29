@echo off

echo ==========================================
echo     INCIDENT RESPONSE AGENT
echo ==========================================

echo.

echo Starting Member 2 API...

uvicorn api.main:app --reload

pause