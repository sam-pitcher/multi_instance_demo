import looker_sdk
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# env variables have been declared in the yaml file

project_id = 'multi_instance_demo' # project name in looker
instance = '452227bf-6f71-4262-bb19-e913e4ee41db.looker.app'  # host name e.g. 'mydomain.looker.com'
release_branch = 'master'  # name of git branch, e.g. 'release-xyz'

sdk = looker_sdk.init40()

try:
    sdk.deploy_ref_to_production(project_id=project_id, branch=release_branch)
    print(f'Production mode for {project_id} in {instance} set to branch: {release_branch} \n')
except:
    print(f'Failed to Update Production mode for {project_id} in {instance} \n')
