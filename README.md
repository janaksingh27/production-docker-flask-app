# Production-Ready Dockerized Flask Application

A production-focused Flask application containerized using Docker and optimized with advanced Docker best practices.

## 🚀 Features

- Multi-stage Docker build
- Python 3.12 slim base image
- Docker image optimization
- `.dockerignore` implementation
- Environment variable configuration
- Docker HEALTHCHECK
- Non-root user execution
- CPU and memory resource limits
- Container restart policy
- Docker logs and troubleshooting
- Git version control

## 📁 Project Structure

```text
.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Dockerfile.single-stage
├── README.md
├── app.py
└── requirements.txt
