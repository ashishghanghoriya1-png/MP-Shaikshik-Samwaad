@echo off
echo ======================================================
echo   MP Shaikshik Samwaad - Live Sync to GitHub Pages
echo ======================================================
cd /d "%~dp0"

echo [1/3] Copying RSK_Master_CLSS_Executive_Dashboard.html to index.html if updated...
if exist "RSK_Master_CLSS_Executive_Dashboard.html" (
    copy /y "RSK_Master_CLSS_Executive_Dashboard.html" "index.html" >nul
    copy /y "RSK_Master_CLSS_Executive_Dashboard.html" "deploy\index.html" >nul
    copy /y "RSK_Master_CLSS_Executive_Dashboard.html" "RSK_Executive_BI_ProMax.html" >nul
) else if exist "RSK_Executive_BI_ProMax.html" (
    copy /y "RSK_Executive_BI_ProMax.html" "index.html" >nul
    copy /y "RSK_Executive_BI_ProMax.html" "deploy\index.html" >nul
)

echo [2/3] Staging all changed files and committing...
git add .
set datestr=%date% %time%
git commit -m "Auto-update: %datestr%"

echo [3/3] Pushing updates to GitHub Pages...
git push origin main

echo.
echo ======================================================
echo   SUCCESS! Your live website is updating now at:
echo   https://ashishghanghoriya1-png.github.io/MP-Shaikshik-Samwaad/
echo ======================================================
pause
