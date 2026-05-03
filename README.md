# 🏢 Apartments Price Prediction
This project demonstrates a **real-world ML system** starting from raw data collection all the way to production deployment.
The goal from this project is to provide customers interested in apartments in 5th settlement with insights to understand what they will get and how much they will pay.

I collected this data from more than four thousands advertisments on (Dubbizle) using a custom web scraping script. 
### 🔹 What is collected?

* Apartment price 
* Location 
* Area (m²) 
* Number of Bedrooms and Bathrooms
* Payment options (Cash, Installments)
* Status (Ready, off-plan)
* Ownership (Primary, Resale)
* Amenities (Pool, Covered parking, Private Garden, Natural Gas, Landline, Security, Water meter, electricity meter, Balcony, Built-in Kitchen Appliances)

After collecting the data , I did the following steps :
* using jupyter notebooks to perform data analysis and data visualization to understand the impact of each feature on the property price, Models Experimentation and fine-tuning to pick the best model with best parameters.
* Data versioning on remote storage on dagshub using DVC.
* Data preprocessing 
* Model training, versioning and registration using mlflow setup on remote repository on dagshub
* Building API for predictions using fastapi library which pulls the latest model version from mlflow setup on dagshub
* Building Streamlit web app to consume the api
* Dockerize the fastapi
* Using github actions to create CI/CD pipeline that automates all the previous steps in addition to pushing the container to a container reqistery on Amazon cloud (AWS ECR) and deploying the container on ( AWS ECS )
* At the end I have a model that can predict Apartments prices with 78 % Accuracy.




## Github Actions Workflow Architecture

          ┌──────────────┐
          │   GitHub     │
          │   Push       │
          └──────┬───────┘
                 ↓
        ⚙️ GitHub Actions CI/CD
                 ↓
      📥 Pull data from (DVC + Dagshub)
                 ↓
      🧹 Data Cleaning & Processing
                 ↓
      🧠 Model Training and versioning with (MLflow)
                 ↓
      🐳 Docker Build
                 ↓
      📦 Push to AWS ECR
                 ↓
      🚀 Deploy on AWS ECS
