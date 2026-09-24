# Three-Tier AWS Application

## Project Purpose

This project demonstrates a three-tier application architecture using Docker and AWS services. The application separates the web, application, and data tiers for better organization and deployment.
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
