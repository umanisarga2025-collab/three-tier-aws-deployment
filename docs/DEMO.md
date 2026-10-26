# Final Assignment Demonstration

## Project overview
This project uses Nginx, Flask, PostgreSQL, Redis, Docker, Docker Hub, GitHub Actions, Kubernetes, and Argo CD.

## Demonstration steps
1. Open https://github.com/umanisarga2025-collab/three-tier-aws-deployment
2. Open the Actions tab and show the successful Docker image build and push workflow.
3. Explain that the image is published to Docker Hub as umanisarga/three-tier-app:1.0 and :latest.
4. When a Kubernetes cluster is available, run kubectl get nodes and kubectl get pods -n three-tier.
5. Check application health using kubectl run health-test -n three-tier --restart=Never --image=curlimages/curl --command -- curl -sS --max-time 10 http://nginx/health
6. Inspect the result with kubectl logs health-test -n three-tier.
7. Check GitOps using kubectl get applications -n argocd.

## Monitoring status
Prometheus and Grafana configuration is documented, but a live installation and dashboard have not yet been verified.

## Conclusion
The project demonstrates container image automation, Kubernetes deployment, and GitOps without requiring AWS.
