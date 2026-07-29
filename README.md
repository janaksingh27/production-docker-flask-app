# 🚀 Production Docker Flask App with Jenkins CI/CD

A production-ready Flask application containerized with Docker and automated using Jenkins Pipeline.

---

## 📌 Project Overview

This project demonstrates a complete CI pipeline using:

- Python Flask
- Docker
- Multi-stage Dockerfile
- Jenkins Pipeline
- GitHub Webhook
- Docker Hub
- Automatic Docker Image Build
- Automatic Docker Image Push

---

## 🛠️ Tech Stack

- Python 3.12
- Flask
- Docker
- Jenkins
- GitHub
- Docker Hub

---

## 📁 Project Structure

```
.
├── Dockerfile
├── Dockerfile.single-stage
├── Jenkinsfile
├── app.py
├── requirements.txt
├── README.md
└── .dockerignore
```

---

## ⚙️ Jenkins Pipeline

Pipeline Stages:

- Git Checkout
- Docker Build
- Docker Hub Login
- Docker Image Push

---

## 🔄 CI Workflow

```
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Webhook
    │
    ▼
Jenkins Pipeline
    │
    ▼
Git Checkout
    │
    ▼
Docker Build
    │
    ▼
Docker Hub Login
    │
    ▼
Docker Push
    │
    ▼
Success
```

---

## 🐳 Build Docker Image

```bash
docker build -t janaksingh/production-docker-flask-app:v1 .
```

---

## ▶️ Run Container

```bash
docker run -d \
  --name production-app \
  -p 5000:5000 \
  janaksingh/production-docker-flask-app:v1
```

---

## 🌐 Docker Hub Repository

Repository:

```
janaksingh/production-docker-flask-app
```

Image:

```
janaksingh/production-docker-flask-app:v1
```

---

## ✅ Features

- Multi-stage Docker Build
- Optimized Docker Image
- Non-root User
- Health Check
- Docker Image Optimization
- Jenkins Pipeline as Code
- GitHub Webhook Integration
- Automatic Docker Build
- Automatic Docker Hub Push
- CI Pipeline

---

## 📷 Jenkins Pipeline Result

- Jenkins Build: ✅ SUCCESS
- Docker Build: ✅ SUCCESS
- Docker Hub Login: ✅ SUCCESS
- Docker Push: ✅ SUCCESS

---

## 👨‍💻 Author

Janak Singh

GitHub:
https://github.com/janaksingh27
