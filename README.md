# DevOps Assessment – Clients API

I choose flask for simplicity, Dockerized the app, and used Jenkins for CI/CD. Mongodb is deployed as datastore and Cer-manager is used for TLS.
Future Improvements : - Integrate Helm for packaging and adding automated tests with Pytest.

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
