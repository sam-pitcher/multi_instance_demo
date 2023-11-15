import looker_sdk
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# env variables have been declared in the yaml file

project_id = 'multi_instance_demo' # project name in looker
instance = 'test.looker.shredr.xyz/'  # host name e.g. 'mydomain.looker.com'
release_branch = 'uat'  # name of git branch, e.g. 'release-xyz'

sdk = looker_sdk.init40()

try:
    sdk.deploy_ref_to_production(project_id=project_id, branch=release_branch)
    print(f'Production mode for {project_id} in {instance} set to branch: {release_branch} \n')
except:
    print(f'Failed to Update Production mode for {project_id} in {instance} \n')
