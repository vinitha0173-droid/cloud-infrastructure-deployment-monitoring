
# Cloud Infrastructure Deployment & Monitoring Capstone

## Project Overview

CloudMonitor is a containerized Python application deployed using Render with monitoring support through Prometheus and Grafana.

The project demonstrates cloud deployment, Docker containerization, application health checks, metrics collection, and monitoring dashboards.

## Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- Render
- Prometheus
- Grafana

## Project Architecture

User
  |
  v
Render Cloud Platform
  |
  v
Docker Container
  |
  v
Flask Application
  |
  +---- /health
  |
  +---- /metrics
  |
  +---- /info

Monitoring:
Prometheus ---> Grafana Dashboard

## Application Endpoints

| Endpoint | Description |
|----------|-------------|
| / | Application home |
| /health | Health check |
| /metrics | Prometheus metrics |
| /info | Application information |

## Docker Setup

Build the Docker image:

docker build -t cloudmonitor .

Run the application:

docker run -p 5000:5000 cloudmonitor

## Docker Compose

Start all monitoring services:

docker compose up -d --build

Services:

- Application: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Grafana Configuration

Grafana is configured with Prometheus as its data source.

The dashboard displays:

- Application health
- Total HTTP requests
- HTTP request rate

Default local Grafana login:

Username: admin
Password: admin

Change the default password after first login.

## Cloud Deployment

The application is configured for deployment using Render.

Deployment steps:

1. Connect the GitHub repository to Render.
2. Select Docker as the runtime.
3. Select the Free instance plan.
4. Configure environment variables.
5. Deploy the application.
6. Verify the live application using the health endpoint.

## Monitoring

Prometheus collects application metrics.

Grafana Cloud provides hosted dashboards, metrics visualization, and alerting.

## Expected Outcome

- Dockerized application
- Cloud deployment
- Public application endpoint
- Application health monitoring
- Prometheus metrics
- Grafana monitoring dashboard

## Author

Vinitha
