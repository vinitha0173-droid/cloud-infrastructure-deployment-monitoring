# Cloud Infrastructure Deployment & Monitoring Capstone

## Project Overview

**CloudMonitor** is a containerized Flask application deployed on Render and monitored using Grafana Cloud.

This project demonstrates cloud application deployment, containerization, health monitoring, Prometheus metrics collection, and email alert notifications.

## Live Application

- **Application URL:** https://cloud-infrastructure-deployment.onrender.com
- **Health Check:** https://cloud-infrastructure-deployment.onrender.com/health
- **Application Status:** Live and Healthy

## Technologies Used

- Python 3.11
- Flask
- Docker
- Render
- Prometheus
- Grafana Cloud
- GitHub

## Project Structure

```text
cloud-infrastructure-deployment-monitoring/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── render.yaml
├── prometheus.yml
├── docker-compose.yml
│
├── grafana/
│   ├── provisioning/
│   │   ├── datasources/
│   │   │   └── prometheus.yml
│   │   └── dashboards/
│   │       └── dashboard.yml
│   │
│   └── dashboards/
│       └── cloud-monitoring-dashboard.json
│
└── README.md
```

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Application status and information |
| `/health` | Health check endpoint |
| `/metrics` | Prometheus metrics (Bearer authentication required) |
| `/info` | Application uptime information |

## Deployment

The application is containerized using Docker and deployed on Render.

Deployment configuration is maintained in `render.yaml`.

### Deployment URL

https://cloud-infrastructure-deployment.onrender.com

## Monitoring and Observability

Grafana Cloud is used to monitor the deployed application.

Prometheus metrics are collected through a Grafana Cloud Metrics Endpoint scrape job.

**Configured monitoring:**
- Application status monitoring
- Total application request counter
- Metrics scraping at one-minute intervals
- Bearer token authentication
- Grafana dashboard visualization
- Email alert notifications

### Grafana Dashboard

Dashboard name: **CloudMonitor Dashboard 2**

Configured panels:

1. Application Status (`app_status`)
2. Total Requests (`app_requests_total`)

### Alert Configuration

Alert rule: `CloudMonitor App Status Alert`

- Metric: `app_status`
- Condition: Below 1
- Evaluation interval: 1 minute
- Pending period: 1 minute
- Notification: Email

The alert is currently in **Normal** state because the application is healthy.

Email contact point testing was successful.

## Security

- Metrics endpoint protected using Bearer token authentication.
- Authentication token stored as an environment variable.
- Secrets must not be committed to the GitHub repository.
- Render and Grafana use the same updated metrics token.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/vinitha0173-droid/cloud-infrastructure-deployment-monitoring.git
cd cloud-infrastructure-deployment-monitoring
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variable

Set a secure `METRICS_TOKEN` environment variable before starting the application.

### 4. Run the application

```bash
python main.py
```

Application runs locally on port 5000 by default.

## Docker

Build the Docker image:

```bash
docker build -t cloudmonitor .
```

Run the container:

```bash
docker run -p 10000:10000 -e PORT=10000 -e METRICS_TOKEN=your_secure_token cloudmonitor
```

## Project Outcome

Successfully deployed a containerized Flask application on Render and configured Grafana Cloud monitoring with Prometheus metrics, dashboard visualizations, and email alert notifications.

The project demonstrates a basic end-to-end cloud deployment and monitoring workflow.

## Author

**Vinitha K**

GitHub: https://github.com/vinitha0173-droid
