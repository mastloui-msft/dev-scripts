import subprocess
import json

def cli (args_str):
    args = args_str.split()
    return subprocess.run(args, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)

def get_git_current_branch():
    process = subprocess.Popen(["git", "branch", "--show-current"], stdout=subprocess.PIPE)
    branch_name, branch_error = process.communicate()
    return "refs/heads/" + branch_name.decode("utf-8").strip()

def get_git_origin_branch():
    process = subprocess.Popen(["git", "symbolic-ref", "refs/remotes/origin/HEAD", "--short"], stdout=subprocess.PIPE)
    branch_name, branch_error = process.communicate()
    return "refs/heads/" + branch_name.decode("utf-8").strip().replace("origin/", "")

def get_access_token():
    response = json.loads(cli("az account get-access-token").stdout.decode("utf-8"))
    return response["accessToken"]

def get_user_alias():
    p = cli(f"az account show")
    response = json.loads(p.stdout)
    alias = response["user"]["name"].split("@")[0]
    return alias