# Prometheus and Grafana

This directory contains lightweight Helm values for the
prometheus-community/kube-prometheus-stack chart.

## Prerequisites

- A working Kubernetes cluster with sufficient resources.
- Helm 3 or newer.
- The Prometheus Community Helm repository.

## Install

From the repository root:

    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update

Create a local values file outside Git containing a strong Grafana password,
then install using that local file:

    helm install monitoring prometheus-community/kube-prometheus-stack \
      --namespace monitoring --create-namespace \
      --values monitoring/values.yaml \
      --set grafana.adminPassword='REPLACE_WITH_A_STRONG_PASSWORD' \
      --timeout 10m

Replace the example password before installation. Never commit real passwords
or tokens to Git.

## Verify

    kubectl get pods -n monitoring
    kubectl get svc -n monitoring

## Open Grafana

    kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80

Open http://localhost:3000 and sign in as admin with the password supplied
during installation. In remote labs, use the lab's port-forwarding feature
for port 3000 if available.

## Notes

The chart installs Prometheus, Grafana, and Kubernetes monitoring components.
Resource availability in small lab clusters may be insufficient. Wait for
pods to become ready and inspect pod events/logs if they remain pending or
restart.
