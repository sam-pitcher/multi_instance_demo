# Looker Multi Instance Demo

This repository shows how to use GitHub Actions to perform a multi instance workflow in Looker.

## Description

It's good practice to have different environments for development, testing and production.
To do this, you need to do 2 things:
1. Pull Request from master branch to **uat** or **prod**
2. Deploy the code either via a webhook or using the Looker API.
Here we use the API with a Looker Admin account to deploy the code.

## Looker Instance Set Up
Development instance is set up as default. This means you can develop your code in personal and shared branches and then 'push to prod' to merge with the master branch and deploy the code to 'Production Mode' in the instance.
UAT and Prod instances need to be set to [Advanced Deploy Mode](https://docs.looker.com/data-modeling/getting-started/advanced-deploy-mode).

<img width="997" alt="image" src="https://github.com/sam-pitcher/multi_instance_demo/assets/45974014/96ec36d9-dc4a-434a-92b7-e8733f31965b">


## GitHub Set Up
### Branches
Create **uat** and **prod** branches in github.
The UAT Instance will use the **uat** branch for Production Mode.
The Prod Instance will use the **prod** branch for Production Mode.

### Workflow Code
Github Actions are stored in the .github/workflows directory.
For this workflow there are 2 files:
- yaml file (this describes the steps the Action takes)
    - will install python and the packages needed
    - set env variables (Github Secrets below)
- python file (this hits the Looker API to deploy the lookml code)

### Github Secrets
You need to declare you API credentials (CLIENT_ID and CLIENT_SECRET) in the Secrets menu
![image](https://user-images.githubusercontent.com/45974014/156515663-08e732ec-0d70-4f7b-91fa-e1dfea1c146e.png)
These will be defined in the yaml file and then used in the python script

### Environment Variables
LOOKERSDK_CLIENT_ID - This is the Looker API Client ID that is pointing to the CLIENT_ID Secret declared above
LOOKERSDK_CLIENT_SECRET - This is the Looker API Client Secret that is pointing to the CLIENT_SECRET Secret declared above
HOST_NAME - This is the host name of the instace you are deploying on, for example: 'https://prod.looker.looker-plus.com'

## Steps

In Looker:
1. Develop lookml code in dev instance on personal and shared branches
2. Create content in the UI. When the content is ready, copy the dashboard lookml into the code base. Preferably in a lookml_dashboard folder
3. When happy with the code, commit the code and then click 'Push to Prod'

In Github:
1. Create a Pull Request from **master** to **uat**
2. Confirm the PR (this should do 2 things)
  - Merge the **master** branch code with the **uat** branch
  - Deploy the **uat** code to Production Mode of the UAT Instance

Repeat for Prod after testing
