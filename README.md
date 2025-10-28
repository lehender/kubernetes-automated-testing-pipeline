# 🚀 Kubernetes Automated Testing Pipeline 🚀

This project demonstrates a full **CI/CD pipeline** for a containerized Python microservice using **Flask**, **Pytest**, **Docker**, **Kubernetes**, and **GitHub Actions**.

Each code commit triggers automated tests, builds a Docker image, and publishes it to the **GitHub Container Registry (GHCR)** — ready for deployment to a Kubernetes cluster. The deployment includes health and readiness probes, enabling continuous validation of application health in a live environment.

---

### 🧩 Features 🧩
- ✅ Flask API with `/health` and `/api/v1/ping` endpoints  
- ✅ Unit testing via **Pytest** (runs automatically on every push)  
- ✅ CI/CD pipeline using **GitHub Actions**  
- ✅ Containerized with **Docker Buildx** and published to **GHCR**  
- ✅ Kubernetes manifests for Deployment and Service with probes  

---

### 🐳 Docker Image 🐳
Pull the prebuilt image:
```bash
docker pull ghcr.io/lehender/k8s-testing-pipeline:latest
```

---

### ⚙️ Stack ⚙️
| Category | Tools |
|-----------|-------|
| Language  | Python 3.12 |
| Framework | Flask |
| Testing   | Pytest |
| CI/CD     | GitHub Actions |
| Container | Docker, Buildx |
| Orchestration | Kubernetes |
| Registry | GitHub Container Registry (GHCR) |

---

### 🧠 Project Goals 🧠
This repository serves as a compact demonstration of modern DevOps practices — showing how testing, containerization, and deployment automation can be seamlessly integrated using open-source tooling.

---

#### 👤 Author 
**Levi Henderson**  
[GitHub](https://github.com/lehender) • [LinkedIn](https://linkedin.com/in/levi-a-henderson)
