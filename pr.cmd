@echo off
REM Ensure Azure CLI is installed and user is logged in
where az >nul 2>nul
if errorlevel 1 (
    echo Azure CLI is not installed. Please install Azure CLI first.
    exit /b
)

REM Get the current branch name
for /f "tokens=*" %%a in ('git symbolic-ref --short HEAD') do set branchName=%%a

REM If branchName is empty, exit with a message
if "%branchName%"=="" (
    echo Could not determine the current branch. Please make sure you're in a git repository.
    exit /b
)

REM Set your Azure DevOps organization, project, and repository names
set organization=msdata
set project=vienna
set repository=vienna

REM Set the target branch for the PR (e.g., 'master')
set targetBranch=master

REM Set the title and description for the PR
set prTitle=Create PR for %branchName%
set prDescription=This PR is automatically created for the branch %branchName%.

REM Use Azure CLI to get an Azure DevOps personal access token (PAT)
for /f "delims=" %%t in ('az account get-access-token --query "accessToken" -o tsv') do set accessToken=%%t

REM Check if we got the token
if "%accessToken%"=="" (
    echo Failed to get Azure DevOps access token. Ensure that you are logged in via Azure CLI.
    exit /b
)

REM Make the REST API call to create the PR using curl
curl -u :%accessToken% ^
    -X POST ^
    -H "Content-Type: application/json" ^
    -d "{\"sourceRefName\": \"refs/heads/%branchName%\", \"targetRefName\": \"refs/heads/%targetBranch%\", \"title\": \"%prTitle%\", \"description\": \"%prDescription%\"}" ^
    https://dev.azure.com/%organization%/%project%/_apis/git/repositories/%repository%/pullrequests?api-version=7.1-preview.1

REM Check for success or failure
if %errorlevel% neq 0 (
    echo Failed to create the PR.
    exit /b
)

echo Pull Request created successfully for branch %branchName%.