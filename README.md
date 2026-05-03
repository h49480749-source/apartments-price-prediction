# 🏢 **Apartments Price Prediction**

✨ This project demonstrates a **real-world Machine Learning system** — starting from **raw data collection** all the way to **production deployment**.

🎯 **Goal:**
Provide customers interested in apartments in **5th Settlement** with clear insights into:

* 💰 *How much they will pay*
* 🏠 *What they will get*

---

## 📊 **Data Collection**

📥 I collected this dataset from **4000+ advertisements** on **Dubbizle** using a custom web scraping script.

### 🔹 **Collected Features**

* 💵 Apartment price
* 📍 Location
* 📐 Area (m²)
* 🛏️ Number of Bedrooms & Bathrooms
* 💳 Payment options *(Cash, Installments)*
* 🏗️ Status *(Ready, Off-plan)*
* 🔑 Ownership *(Primary, Resale)*

### 🏡 **Amenities**

* 🏊 Pool
* 🚗 Covered parking
* 🌳 Private Garden
* 🔥 Natural Gas
* ☎️ Landline
* 🔐 Security
* 💧 Water meter
* ⚡ Electricity meter
* 🌅 Balcony
* 🍳 Built-in Kitchen Appliances

---

## ⚙️ **Project Workflow**

After collecting the data, the following steps were performed:

### 🔬 **Data Analysis & Experimentation**

* 📓 Used Jupyter Notebooks for:

  * 📊 Data Analysis & Visualization
  * 🧪 Model Experimentation & Fine-tuning

### 🗂️ **Data Versioning**

* 📦 Managed using **DVC**
* ☁️ Remote storage on **Dagshub**

### 🔧 **Processing & Training**

* 🧹 Data preprocessing
* 🧠 Model training
* 🏷️ Model versioning & registration using **MLflow** *(hosted on Dagshub)*

### 🚀 **Deployment Pipeline**

* ⚡ Built prediction API using **FastAPI**
* 🔄 API dynamically loads the latest model from MLflow
* 🌐 Created a **Streamlit Web App** to consume the API
* 🐳 Dockerized the FastAPI service

---

## 🔁 **CI/CD Automation**

⚙️ Implemented a full CI/CD pipeline using **GitHub Actions**:

* 🔄 Automates the entire workflow
* 📦 Builds & pushes Docker image to **AWS ECR**
* 🚀 Deploys container on **AWS ECS**

---

## 📈 **Model Performance**

🎯 Final model achieves:

> 🟢 **78% Accuracy**
