# ===================================================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import gdown

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="FurnaceAI - Blast Furnace Digital Twin",
    layout="wide",
    page_icon="🔥"
)

st.title("🔥 FurnaceAI – Blast Furnace Digital Twin")
st.markdown("AI-Based Hot Metal Temperature & Efficiency Prediction System")
st.markdown("---")

st.write("✅ App Loaded Successfully")

# -----------------------------
# Model Download from Google Drive
# -----------------------------
MODEL_PATH = "blast_furnace_model.pkl"
SCALER_PATH = "blast_furnace_scaler.pkl"

MODEL_URL = "https://drive.google.com/uc?id=1-XpxYiuB2THJ-pQ45ZdY7eyXC7Oyk5sg"

@st.cache_resource
def load_model():
    # Download model only if not exists
    if not os.path.exists(MODEL_PATH):
        #st.info("⬇ Downloading AI model... Please wait (first run only)")
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler

try:
    model, scaler = load_model()
    st.success("✅ Model Loaded Successfully")
except Exception as e:
    st.error(f"❌ Model Loading Error: {e}")
    st.stop()

# -----------------------------
# Industrial Logic Functions
# -----------------------------
def calculate_efficiency(temp):
    score = 100 - abs(temp - 1475) * 0.2
    return max(0, min(100, score))

def risk_indicator(temp):
    if 1450 <= temp <= 1500:
        return "🟢 Stable"
    elif (1420 <= temp < 1450) or (1500 < temp <= 1520):
        return "🟡 Warning"
    else:
        return "🔴 Critical"

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("⚙ Furnace Operating Parameters")

Fe = st.sidebar.slider("Iron Ore Fe %", 55.0, 68.0, 60.0)
Coke = st.sidebar.slider("Coke Rate (kg/tHM)", 300.0, 600.0, 450.0)
PCI = st.sidebar.slider("PCI Rate (kg/tHM)", 100.0, 250.0, 180.0)
HBT = st.sidebar.slider("Hot Blast Temperature (°C)", 900.0, 1200.0, 1050.0)
Pressure = st.sidebar.slider("Blast Pressure (bar)", 2.0, 4.0, 3.0)
Moisture = st.sidebar.slider("Moisture %", 2.0, 8.0, 4.0)
Basicity = st.sidebar.slider("Slag Basicity (CaO/SiO₂)", 1.0, 1.4, 1.2)
O2 = st.sidebar.slider("Oxygen Enrichment %", 21.0, 28.0, 23.0)
CO = st.sidebar.slider("CO %", 18.0, 28.0, 22.0)
CO2 = st.sidebar.slider("CO₂ %", 18.0, 25.0, 21.0)

# -----------------------------
# Prediction Button
# -----------------------------
if st.sidebar.button("🚀 Predict Furnace Condition"):

    input_data = pd.DataFrame([{
        "Fe_percent": Fe,
        "Coke_rate": Coke,
        "PCI_rate": PCI,
        "Hot_blast_temp": HBT,
        "Blast_pressure": Pressure,
        "Moisture_percent": Moisture,
        "Basicity": Basicity,
        "Oxygen_percent": O2,
        "CO_percent": CO,
        "CO2_percent": CO2
    }])

    try:
        input_scaled = scaler.transform(input_data)
        predicted_temp = model.predict(input_scaled)[0]
    except Exception as e:
        st.error(f"Prediction Error: {e}")
        st.stop()

    efficiency = calculate_efficiency(predicted_temp)
    risk = risk_indicator(predicted_temp)

    st.markdown("## 📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="🔥 Hot Metal Temperature (°C)",
        value=round(predicted_temp, 2)
    )

    col2.metric(
        label="⚡ Efficiency Score",
        value=round(efficiency, 2)
    )

    if "Stable" in risk:
        col3.success(f"Risk Status: {risk}")
    elif "Warning" in risk:
        col3.warning(f"Risk Status: {risk}")
    else:
        col3.error(f"Risk Status: {risk}")

    st.markdown("---")
    st.subheader("📈 Efficiency Visualization")
    st.progress(int(efficiency))

    st.markdown("---")
    st.subheader("📌 Model Feature Importance")

    try:
        importances = model.feature_importances_
        feature_names = input_data.columns

        importance_df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importances
        }).sort_values(by="Importance", ascending=False)

        st.bar_chart(importance_df.set_index("Feature"))
    except:

        st.info("Feature importance not available for this model type.")
