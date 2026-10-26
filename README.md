# Three-Tier DevOps Application

A containerized three-tier application with Docker Hub image publishing,
Kubernetes deployment, Argo CD GitOps, and optional Prometheus/Grafana monitoring.

## Architecture

User
  |
  v
Nginx reverse proxy (port 80)
  |
  v
Flask application (port 5000)
  |                 |
  v                 v
PostgreSQL         Redis

## Repository structure

- `app/` - Flask application and Dockerfile
- `nginx/` - Nginx configuration
- `docker-compose.yml` - Local multi-container deployment
- `k8s/` - Kubernetes manifests for the application and data services
- `argocd-app.yaml` - Argo CD application definition
- `monitoring/` - Prometheus/Grafana Helm values and instructions
- `.github/workflows/deploy.yml` - Build and publish Docker images

## CI pipeline

On pushes to `main`, GitHub Actions builds the application image and pushes
`umanisarga/three-tier-app:1.0` and `umanisarga/three-tier-app:latest`
to Docker Hub.

Configure these repository Actions secrets:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Never store credentials directly in workflow files.

## Kubernetes deployment

Apply the manifests to a working Kubernetes cluster:

    kubectl apply -f k8s/namespace.yaml
    kubectl apply -f k8s/ -n three-tier

Check the workloads:

    kubectl get deployments,services -n three-tier
    kubectl get pods -n three-tier

Test application health from inside the cluster:

    kubectl run health-test -n three-tier --restart=Never \
      --image=curlimages/curl --command -- \
      curl -sS --max-time 10 http://nginx/health

The expected health response reports the application, PostgreSQL, and Redis
as healthy/connected.

## Argo CD GitOps

Apply the Argo CD application manifest after Argo CD is installed:

    kubectl apply -f argocd-app.yaml
    kubectl get applications -n argocd

Argo CD tracks the `main` branch and the `k8s/` directory. Automated sync,
pruning, and self-healing are enabled.

## Prometheus and Grafana

Follow `monitoring/README.md`. Use a working cluster with sufficient resources
and provide a strong Grafana password at installation time.

## Important

Kubernetes clusters in temporary labs can be deleted when the lab session
ends. GitHub stores the project configuration but does not keep the cluster
or its workloads running.

This project can run without AWS. AWS deployment is not currently required.

## Project Documentation

- [Architecture and CI/GitOps Flow](docs/ARCHITECTURE.md)
- [Final Assignment Demonstration](docs/DEMO.md)
- [Troubleshooting Guide](docs/TROUBLESHOOTING.md)
- [Prometheus and Grafana Setup](monitoring/README.md)

## Completion Status

- [x] Docker Hub image publishing workflow configured.
- [x] GitHub Actions build and push workflow verified successful.
- [x] Kubernetes application health previously verified.
- [x] Argo CD synchronization previously verified.
- [x] Architecture, demonstration, and troubleshooting documentation added.
- [ ] Prometheus and Grafana installation and dashboard verification.
