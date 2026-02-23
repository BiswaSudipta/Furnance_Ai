# 🔥 FurnaceAI – Blast Furnace Digital Twin

### 🏭 AI-Powered Blast Furnace Temperature & Efficiency Prediction System

🌐 **Live Application (Streamlit Cloud)**
👉 **[https://furnanceai-bhy2dsfpqpyk8kxykh2xy3.streamlit.app/](https://furnanceai-bhy2dsfpqpyk8kxykh2xy3.streamlit.app/)**

---

## 🎥 Demo

<p align="center">
  <img src="Furnance_Ai_UI.png" alt="FurnaceAI Dashboard Demo" width="90%">
</p>

---

## 🧠 What is this project?

**FurnaceAI** is an **AI-driven industrial digital twin system** that predicts **Blast Furnace Hot Metal Temperature**, calculates **Operational Efficiency**, and provides **Real-Time Risk Alerts**.

This project simulates real-world **blast furnace monitoring systems** used in integrated steel plants by combining:

* 🔬 A **physics-informed industrial dataset**
* 🤖 A **machine learning regression model**
* 📊 A **real-time prediction dashboard**
* ☁️ A **cloud-deployed Streamlit application**

The goal is to demonstrate how **Machine Learning can optimize metallurgical processes** and reduce operational risk in heavy industries.

---

## ✨ Key Features

* 🔥 Hot Metal Temperature Prediction
* ⚡ Furnace Efficiency Score (0–100)
* 🚨 Real-Time Risk Classification

  * 🟢 Stable
  * 🟡 Warning
  * 🔴 Critical
* 📈 Model Feature Importance Visualization
* 🏭 Industrial-Grade Input Parameters
* 🧠 Physics-Informed Synthetic Dataset
* ☁️ Deployed on Streamlit Cloud
* 📱 Clean & Interactive Control Room UI

---

## 🛠️ Tech Stack

### 🤖 Machine Learning

<p>
<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Joblib-FF6F00?style=for-the-badge"/>
</p>

### 📊 Frontend & Deployment

<p>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit_Cloud-FF4B4B?style=for-the-badge"/>
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github"/>
<img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
</p>

---

## 📊 Problem Statement

In blast furnace operations, unstable hot metal temperature leads to:

* Increased fuel consumption
* Reduced furnace productivity
* Slag-metal separation inefficiencies
* Higher CO₂ emissions
* Increased refractory damage risk

Manual monitoring is reactive and slow.

This project solves that by:

* Simulating realistic furnace states
* Training a machine learning model
* Providing instant temperature predictions
* Alerting operators before instability occurs

---

## 🧠 Modeling Approach

* Supervised **Regression Model**
* Algorithm: **Random Forest Regressor**
* Hyperparameter tuning using **GridSearchCV**
* Dataset Size: **15,000 Industrial Operational States**
* 10 Furnace Operating Parameters as Inputs
* Target: **Hot Metal Temperature (°C)**

---

## 📈 Model Output

The system produces:

### 🔥 1. Predicted Hot Metal Temperature

Continuous regression output in °C

### ⚡ 2. Efficiency Score (0–100)

[
Efficiency = 100 - |T - 1475| \times 0.2
]

### 🚨 3. Risk Indicator

* 🟢 Stable → 1450–1500 °C
* 🟡 Warning → 1420–1450 or 1500–1520 °C
* 🔴 Critical → Outside safe range

---

## 📥 Input Parameters

| Category       | Parameter             |
| -------------- | --------------------- |
| Raw Material   | Iron Ore Fe %         |
| Fuel           | Coke Rate             |
| Fuel           | PCI Rate              |
| Thermal        | Hot Blast Temperature |
| Pressure       | Blast Pressure        |
| Moisture       | Moisture %            |
| Slag Chemistry | Basicity (CaO/SiO₂)   |
| Gas Chemistry  | Oxygen %              |
| Gas Chemistry  | CO %                  |
| Gas Chemistry  | CO₂ %                 |

---

## 📂 Project Structure

```text
Furnance_Ai/
│
├── app.py
├── blast_furnace_scaler.pkl
├── blast_furnace_industrial_dataset.csv
├── Furnance_Ai_UI.png
├── requirements.txt
├── README.md
├── LICENSE
│
└── blast_furnace_model.pkl (Stored separately due to 123MB size)
```

> Note: `blast_furnace_model.pkl` is stored externally due to file size limitations.

---

## ⚙️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Furnance_Ai.git
cd Furnance_Ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Model File

Download `blast_furnace_model.pkl` and place it inside the project root directory.

### 4️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## ☁️ Live Deployment

The application is deployed on **Streamlit Cloud**.

👉 [https://furnanceai-bhy2dsfpqpyk8kxykh2xy3.streamlit.app/](https://furnanceai-bhy2dsfpqpyk8kxykh2xy3.streamlit.app/)

---

## 🎯 Industrial Use Cases

* Steel Plant Furnace Monitoring
* Process Optimization Systems
* Energy Efficiency Analytics
* Industrial Digital Twin Simulation
* Metallurgical AI Research
* Smart Manufacturing Systems

---

## 🚀 Future Enhancements

* Time-Series LSTM Forecasting
* SHAP Explainability Dashboard
* Real-Time Sensor Integration
* Multi-Page Industrial Analytics
* Model Retraining Pipeline
* Performance Monitoring System

---

## 👨‍💻 Author

**Sudipta Biswas**
B.Tech – Metallurgical & Materials Engineering
AI | Data Science | Industrial ML

---

## 📄 License

This project is licensed under the **MIT License**.

---

### ⭐ If you found this project valuable, consider giving it a star!

