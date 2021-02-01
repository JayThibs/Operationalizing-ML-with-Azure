from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config()

# Set with the deployment name
name = "votens-bank-12921"

# Load existing web service
service = Webservice(name=name, workspace=ws)
logs = service.get_logs()

# Turn on Application Insight (since we did not turn it on during deployment)
service.update(enable_app_insights=True)

for line in logs.split('\n'):
    print(line)
