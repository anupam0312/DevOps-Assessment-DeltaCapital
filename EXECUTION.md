# Execution Steps

##  Clone Repository

git clone https://github.com/anupam0312/DevOps-Assessment-DeltaCapital.git
cd DevOps-Assessment-DeltaCapital

## Build & Run Locally (Optional)
cd app
docker build -t clients-api .
docker run -p 5000:5000 clients-api

Visit: http://localhost:5000/clients

## Deploy to Kubernetes
Have a running cluster (Minikube, Kind, or EKS).
Ensure kubectl, ingress-nginx, and cert-manager are installed.

kubectl apply -f k8s/

## Verify Deployment
kubectl get pods
kubectl get svc
kubectl get ingress

## Access API

curl http://localhost:8080/clients
Or via Ingress:
https://clients.api.deltacapita.com/clients

## CI/CD via Jenkins

Add repo to Jenkins.
Configure DockerHub creds (dockerhub-creds).
Run pipeline → builds, pushes, deploys automatically.








