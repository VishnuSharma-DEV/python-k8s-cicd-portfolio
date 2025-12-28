Python Kubernetes CI/CD on AWS (DevOps Portfolio)
This project implements a full production-grade CI/CD pipeline that automatically builds, containerizes, and deploys a Python Flask application into a multi-node Kubernetes cluster running on AWS EC2 using Jenkins.

It reflects real enterprise DevOps architecture and not a basic tutorial setup.

Demo
http://<MASTER_PUBLIC_IP>:31260

Features
Fully automated CI/CD pipeline
Docker image versioning & registry publishing
Kubernetes high availability & scaling
NGINX Ingress public routing
Auto deployment on every GitHub push
Secure credentials management
Tech Stack
AWS: EC2

Jenkins: CI/CD

Docker: Containerization

Kubernetes: Orchestration

NGINX: Ingress Controller

Python: Flask Application

AWS Infrastructure Design
This project is deployed on AWS EC2 based Kubernetes infrastructure designed with production networking and security principles.

EC2 Instances
Instance	Description
Jenkins Server	CI/CD Automation Engine
K8s Masterr	Kubernetes Control Plane
K8s Worker-1	Application Node 1
K8s Worker-2	Application Node 2
All instances run Ubuntu Linux.

🔐 Security Groups & Networking

A single Security Group is used with controlled rules:

Rule	Purpose
22	SSH management
6443	Kubernetes API
10250	Node communication
30000–32767	Kubernetes NodePort services
Self-referencing	All Traffic Pod-to-Pod overlay networking
This ensures secure but fully functional cluster networking.

🌐 Public Access Design
Workers remain private-only. Public access is routed via the control plane using NodePort + kube-proxy binding.

This design mirrors production-grade security where compute nodes are not internet exposed.

Jenkins CI/CD Pipeline
This project uses a Jenkins Freestyle CI/CD pipeline to automate build and deployment. To deploy this project run

Pipeline Stages
Source Checkout - Pulls code from GitHub
Test - Validates Python application
Build - Creates Docker image
Push - Publishes image to DockerHub
Deploy - Updates Kubernetes deployment
Jenkins - Build Commands
Test Stage

  python3 -m venv venv
  . venv/bin/activate
  pip install -r requirements.txt
  python -m py_compile app.py
Build Stage

  docker build -t vishnusharma06102000
  python-k8s-app:$BUILD_NUMBER .
Push Stage

  docker push vishnusharma06102000/python-k8s-app:$BUILD_NUMBER
Deploy Stage

  kubectl set image deployment/python-app python-k8s-app=vishnusharma06102000/python-k8s-app:$BUILD_NUMBER
Run Locally
Clone the project

  git clone https://github.com/VishnuSharma-DEV/python-k8s-cicd-portfolio.git
Go to the project directory

  cd python-k8s-cicd-portfolio
Install the python module

  pip install flask
  python app.py
Create the deployment for k8s

  kubectl create deployment python-app --image=vishnusharma06102000/python-k8s-app:latest
  kubectl expose deployment python-app --type=NodePort --port=5000
Running Test

  python -m py_compile app.py
Environment Variables
To run this project, you will need to add the following environment variables to your jenkins pipeline file

DockerHub username DOCKER_USER
DockerHub password DOCKER_PASS
Kubernetes API token K8S_TOKEN
Authors
@VishnuSharma
🛠 Skills
AWS
Kubernetes
Jenkins
Docker
Linux
CI/CD
NGINX
🔗 Links
https://github.com/VishnuSharma-DEV

https://hub.docker.com/u/vishnusharma06102000
