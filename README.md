# Chicken Disease Classification 🐓

## Workflows

1. Update `config.yaml`
2. Update `secrets.yaml` [Optional]
3. Update `params.yaml` [Optional]
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline
8. Update the `main.py`
9. Update the `dvc.yaml`

# How to run?

### Steps:

Clone the repository

```bash
https://github.com/Wilsven/chicken-disease-classification.git
```

### Step 01- Create a conda environment after opening the repository

```bash
conda create -n <ENV NAME> python=3.8 -y
```

```bash
conda activate <ENV NAME>
```

### Step 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

# CI/CD Deployment with GitHub Actions with AWS

## 1. Login to AWS Console

## 2. Create IAM User for Deployment

    # Specific access

    1. EC2 access : It is a virtual machine

    2. ECR: Elastic Container registry to save your docker image in AWS


    # Description

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull your image from ECR in EC2

    5. Lauch your docker image in EC2

    # Policy

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR Repository to store/save Docker Image

    - Save the URI: 797496359327.dkr.ecr.ap-southeast-2.amazonaws.com/chicken-disease-classification

## 4. Create EC2 Machine (Ubuntu)

## 5. Open EC2 and Install Docker in EC2 Machine

    # Optional

    sudo apt-get update -y

    sudo apt-get upgrade -y

    # Required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## 6. Configure EC2 as Self-hosted Runner:

    Settings > Actions > Runner > New self-hosted runner > Select Linux > Execute commands one by one in your Virtual Machine

## 7. Setup GitHub Secrets

    AWS_ACCESS_KEY_ID

    AWS_SECRET_ACCESS_KEY

    AWS_REGION

    AWS_ECR_LOGIN_URI

    ECR_REPOSITORY_NAME

# CI/CD Deployment with GitHub Actions with Azure

## 1. Save Pass

    XyB08HKEZXVFMDwdMm2rZF+09KDPTzCnOe8Lk0VP6I+ACRBxx5PL

## 2. Run from Terminal

    docker build -t chicken.azurecr.io/chicken:latest .
    
    docker login chicken.azurecr.io
    
    docker push chicken.azurecr.io/chicken:latest

## Deployment Steps

1. Build the Docker Image of the source code
2. Push the Docker Image to Container Registry
3. Launch the Web App Server in Azure
4. Pull the Docker Image from the Container Registry to Web App server and run
