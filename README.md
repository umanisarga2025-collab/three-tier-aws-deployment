# Three-Tier AWS Application

A Dockerized three-tier web application deployed on AWS EC2 using Amazon ECR.

## Architecture

```text
User / Internet
       |
       v
AWS EC2 Public Endpoint
       |
       v
Nginx (Port 80)
Presentation / Web Tier
       |
       v
Flask Application (Port 5000)
Application Tier
       |
       +------------------+
       |                  |
       v                  v
     Redis            PostgreSQL
       Data Tier
