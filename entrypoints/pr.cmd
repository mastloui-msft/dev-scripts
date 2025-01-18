@echo off

:: Check for the -t parameter
set "param="
if "%1"=="-t" (
    set "param=%1 %2"
)

:: Run the Python script with the optional parameter
python %~dp0/../scripts/create_pr.py %param%