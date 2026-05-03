# 🏢 Apartments Price Prediction Workflow

An end-to-end **MLOps pipeline** for predicting apartment prices, built with modern data engineering and deployment practices.
This project automates everything from **data versioning → preprocessing → model training → experiment tracking → containerization → deployment on AWS ECS**.

---

## 🚀 Overview

This repository implements a **fully automated machine learning workflow** using:

* 🔄 **DVC** for data versioning
* 📊 **MLflow** for experiment tracking
* 🤖 **Python** for data preprocessing & modeling
* 🐳 **Docker** for containerization
* ☁️ **AWS (ECR + ECS)** for deployment
* ⚙️ **GitHub Actions** for CI/CD

Every push to `main` triggers a complete pipeline — no manual intervention required.

---

## 🧠 Workflow Architecture

```text
          ┌──────────────┐
          │   GitHub     │
          │   Push/PR    │
          └──────┬───────┘
                 ↓
        ⚙️ GitHub Actions CI/CD
                 ↓
      📥 Pull Data (DVC + Dagshub)
                 ↓
      🧹 Data Cleaning & Processing
                 ↓
      🧠 Model Training (MLflow)
                 ↓
      🐳 Docker Build
                 ↓
      📦 Push to AWS ECR
                 ↓
      🚀 Deploy on AWS ECS
```

---

## 📂 Project Structure

```bash
.
├── src/
│   ├── Data_Cleaning.py     # Data preprocessing pipeline
│   ├── Modelling.py         # Model training & logging
│
├── .github/workflows/
│   └── main.yml             # CI/CD pipeline
│
├── Dockerfile               # Container definition
├── requirements.txt         # Dependencies
├── dvc.yaml (optional)      # DVC pipeline (if used)
└── README.md
```

---

## ⚙️ CI/CD Pipeline Breakdown

Your GitHub Actions workflow performs:

### 1️⃣ Environment Setup

* Python 3.8 environment
* Dependency installation

### 2️⃣ Data Versioning (DVC)

* Connects to **Dagshub remote**
* Pulls dataset automatically

### 3️⃣ Data Processing

* Runs:

```bash
python src/Data_Cleaning.py
```

### 4️⃣ Experiment Tracking (MLflow)

* Tracks:

  * Parameters
  * Metrics
  * Model artifacts

### 5️⃣ Model Training

```bash
python src/Modelling.py
```

### 6️⃣ Containerization

* Builds Docker image

### 7️⃣ Deployment (AWS)

* Pushes image to **Amazon ECR**
* Triggers **ECS service update**

---

## 🔐 Required Secrets

Set these in **GitHub → Settings → Secrets → Actions**

### 🔹 Dagshub / DVC

* `DAGSHUB_USERNAME`
* `DAGSHUB_TOKEN`

### 🔹 MLflow

* `MLFLOW_TRACKING_URI`

### 🔹 AWS

* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_REGION`
* `AWS_ACCOUNT_ID`

---

## 🐳 Docker Usage (Local)

Build and run locally:

```bash
docker build -t apartments-api .
docker run -p 8001:8001 apartments-api
```

---

## ☁️ Deployment Details

* **ECR Repository:** `apartments-price-prediction`
* **ECS Cluster:** `apartments-prediction-cluster`
* **Service:** `apartments-prediction-service`

Deployment is triggered automatically on every push.

---

## 📈 Key Features

✅ Fully automated ML pipeline
✅ Data versioning with DVC
✅ Experiment tracking with MLflow
✅ Reproducible workflows
✅ Production-ready deployment
✅ Scalable cloud infrastructure

---

## ⚠️ Notes & Best Practices

* Ensure ECS task definition uses the correct **container port (8001)**
* If service fails:

  * Check **CloudWatch logs**
  * Verify **security groups & inbound rules**
* Always version your data before training (`dvc push`)

---

## 💡 Future Improvements

* 🔹 Add model monitoring (drift detection)
* 🔹 Implement API endpoint (FastAPI)
* 🔹 Add unit & integration tests
* 🔹 Introduce feature store
* 🔹 Blue/Green deployment for zero downtime

---

## 👨‍💻 Author

**Hamza**
Final-year Communications Engineering Student
Passionate about **AI, MLOps, and scalable systems**

---

## ⭐ Final Thought

This project is more than a model —
it’s a **production-grade ML system** that reflects real-world industry workflows.

If it helped you or inspired you, consider giving it a ⭐
