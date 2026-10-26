# Troubleshooting Guide

## GitHub Actions failure
Inspect the failed step in GitHub Actions. Verify DOCKERHUB_USERNAME and DOCKERHUB_TOKEN secrets. Never expose secret values.

## Pod Pending
Run kubectl describe pod POD_NAME -n three-tier and kubectl get events -n three-tier --sort-by=.lastTimestamp.
Check resource shortages, image issues, and volume events.

## CrashLoopBackOff
Run kubectl logs POD_NAME -n three-tier --previous and kubectl describe pod POD_NAME -n three-tier.
Check startup errors, environment variables, dependency connectivity, probes, and resource limits.

## ImagePullBackOff
Run kubectl describe pod POD_NAME -n three-tier. Verify the image name, tag, registry access, and pull credentials if required.

## Application health failure
Run kubectl get pods,services -n three-tier and kubectl logs deployment/app -n three-tier.
Check PostgreSQL and Redis readiness, Service endpoints, and application configuration.

## Argo CD OutOfSync or Degraded
Run kubectl get applications -n argocd and kubectl describe application three-tier-app -n argocd.
Check the repository URL, branch, manifest path, namespace, and application conditions.

## Kubernetes API timeout
Run kubectl get --raw=/readyz?verbose and kubectl get nodes. Inspect control-plane health before retrying installations.

## Monitoring problems
Run helm list -A and kubectl get pods -n monitoring. Inspect events and available CPU/memory.
