@echo off
REM Check if the branch name argument is provided
if "%1"=="" (
    echo Please provide a branch name.
    exit /b
)

REM Create a new branch with the name provided in the first argument
git checkout -b users/mastloui/%1

REM Push the branch to the remote repository and set the upstream
git push --set-upstream origin users/mastloui/%1