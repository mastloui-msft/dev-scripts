import requests
import webbrowser
import subprocess
import argparse
from utils import get_git_origin_branch, get_git_current_branch, get_access_token

def _get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", required=False, help="Pull request title.")
    return parser

organization = 'msdata'
project = 'vienna'
repository_id = 'vienna'
source_branch = get_git_current_branch()
target_branch = get_git_origin_branch()
prTitle = f"PR for {source_branch}"

args = _get_parser().parse_args()
if(args.t):
    prTitle = args.t

# Azure DevOps API URL
url = f'https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{repository_id}/pullrequests?api-version=6.0'

# Pull request details
pr_data = {
    "sourceRefName": source_branch,
    "targetRefName": target_branch,
    "title": prTitle,
    "description": "Your PR Description"
}

# Headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {get_access_token()}'
}

print("\n")
print(f"####################################################################")
print(f"Creating a new pull request on repository {repository_id}.")
print(f"PR Title: {prTitle}.")
print(f"Source branch: {source_branch}.")
print(f"Target branch: {target_branch}.")
print(f"####################################################################")

# Create the pull request
response = requests.post(url, json=pr_data, headers=headers)
response.raise_for_status()  # Raise an error for bad status codes

# Get the URL of the created pull request
pr_id = response.json()['pullRequestId']
pr_url = f"https://{organization}.visualstudio.com/{project}/_git/{repository_id}/pullrequest/{pr_id}"

# Open the pull request URL in the default web browser
webbrowser.open(pr_url)

print(f'Pull request created: {pr_url}')
