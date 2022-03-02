import looker_sdk
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ['LOOKERSDK_BASE_URL'] = 'https://prod.looker.looker-plus.com'
os.environ['LOOKERSDK_CLIENT_ID'] = 'FV5WWgtZsP8j2xCZSMgz'
os.environ['LOOKERSDK_CLIENT_SECRET'] = 'PWx5nCYSvWhF2xrcg49mvFgd'
os.environ['LOOKERSDK_VERIFY_SSL']= 'False'
os.environ['LOOKERSDK_API_VERSION']= '4.0'
os.environ["LOOKERSDK_TIMEOUT"] = "120"

project_id = 'multi_instance_demo' # project name in looker
instance = 'prod.looker.looker-plus.com'  # host name e.g. 'mydomain.looker.com'
release_branch = 'prod'  # name of git branch, e.g. 'release-xyz'

sdk = looker_sdk.init40(ini_file, section=instance)

try:
    sdk.deploy_ref_to_production(project_id=project_id, branch=release_branch)
    print(f'Production mode for {project_id} in {instance} set to branch: {release_branch} \n')
except:
    print(f'Failed to Update Production mode for {project_id} in {instance} \n')
