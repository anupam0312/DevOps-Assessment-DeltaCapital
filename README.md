# DevOps Assessment – Clients API

## Overview
This repo contains:
- A simple Clients API (Flask, Dockerized)
- Kubernetes manifests (API, MongoDB, Ingress, Cert-Manager)
- Jenkins pipeline for CI/CD

## Structure
```
app/ → Clients API code + Dockerfile
k8s/ → Kubernetes YAML files
Jenkinsfile → CI/CD pipeline
```

## Setup
1. Install Docker, Kubernetes (minikube/kind/EKS), and cert-manager.
2. Deploy ingress-nginx controller.
3. Run:
   ```bash
   kubectl apply -f k8s/
   ```
4. API will be available at:  
   `https://clients.api.deltacapita.com/clients`

## CI/CD
- Jenkins pipeline builds & pushes Docker image to DockerHub, then deploys to Kubernetes.
