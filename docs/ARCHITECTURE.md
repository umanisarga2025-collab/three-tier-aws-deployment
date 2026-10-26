# Three-Tier DevOps Project Architecture

## Overview

This project demonstrates containerization, CI automation, Kubernetes deployment,
and GitOps using a Flask web application with PostgreSQL and Redis.

## Request flow

User / Client
    |
    v
Nginx reverse proxy (Service port 80)
    |
    v
Flask application (Service port 5000)
    |                         |
    v                         v
PostgreSQL (5432)             Redis (6379)

## Components

- Nginx: receives HTTP requests and proxies them to the Flask application.


cat >> README.md <<'EOF'

## Project documentation

- [Architecture and CI/GitOps flow](docs/ARCHITECTURE.md)
- [Final assignment demonstration script](docs/DEMO.md)
- [Troubleshooting guide](docs/TROUBLESHOOTING.md)
- [Prometheus and Grafana setup](monitoring/README.md)

## Project completion status

- [x] Docker Hub image publishing workflow configured.
- [x] GitHub Actions workflow previously verified successful.
- [x] Kubernetes application health previously verified.
- [x] Argo CD synchronization previously verified.
- [x] Project configuration and documentation committed to GitHub.
- [ ] Prometheus and Grafana installation and dashboard verification.
