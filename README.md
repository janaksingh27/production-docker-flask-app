# Production-Ready Dockerized Flask Application

A lightweight Flask application containerized using Docker with production-focused practices.

## Features

- Lightweight Python 3.12-slim base image
- Docker image optimization
- pip cache disabled using `--no-cache-dir`
- Container healthcheck
- CPU and memory resource limits
- Non-root user for better security
- Docker logs and container troubleshooting practice

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
└── .gitignore
