@echo off

:: Check for the -t parameter
set "param="
if "%1"=="-dg" (
    set "param=%1 %2"
)

:: Run the Python script with the optional parameter
python %~dp0/../scripts/open_dashboard.py %param%