@echo off
setlocal

:: Get the name of the current branch
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD') do set CURRENT_BRANCH=%%i

:: Get the name of the main branch
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref origin/HEAD') do set MAIN_BRANCH=%%i

:: Loop through all local branches
for /f "tokens=*" %%i in ('git branch --format="%%(refname:short)"') do (
    if not "%%i"=="%CURRENT_BRANCH%" if not "%%i"=="%MAIN_BRANCH%" (
        git branch -D %%i
    )
)

endlocal