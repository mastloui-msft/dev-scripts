import requests
import webbrowser
import subprocess
import argparse
from utils import get_git_origin_branch, get_git_current_branch, get_access_token

def _get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-dg", required=False, help="Deployment group name")
    return parser

args = _get_parser().parse_args()

dg = None
if(args.dg):
    dg = args.dg

print("\n")
print(f"####################################################################")
print(f"Opening Kusto Dashboards.")
print(f"####################################################################")

dashboard_url = f"https://dataexplorer.azure.com/dashboards/09c3a5f9-75b7-46b3-8523-4d7530db2335?p-_startTime=1hours&p-_endTime=now&p-_region=all&p-_serviceNamespace=v-AzureOpenAI&p-_apps=v-model-endpoint-discovery&p-_apps=v-model-pool&p-_apps=v-model-pool-capacity-manager&p-_deploymentGroup=all&p-_poolName=all&p-_modelDefinitionId=all#b4386851-760e-4999-aae2-597f12e1efd2"
if(dg):
    dashboard_url = f"https://dataexplorer.azure.com/dashboards/09c3a5f9-75b7-46b3-8523-4d7530db2335?p-_startTime=1hours&p-_endTime=now&p-_region=all&p-_serviceNamespace=v-AzureOpenAI&p-_apps=v-model-endpoint-discovery&p-_apps=v-model-pool&p-_apps=v-model-pool-capacity-manager&p-_deploymentGroup={dg}&p-_poolName=all&p-_modelDefinitionId=all#b4386851-760e-4999-aae2-597f12e1efd2"

# Open the pull request URL in the default web browser
webbrowser.open(dashboard_url)

print(f'Dashboard URI: {dashboard_url}')
