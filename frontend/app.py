import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="AI Tax Navigator", layout="wide")

st.title("🧠 AI Current Tax Regime Navigator")

income = st.number_input("Annual Income", min_value=0)
deductions = st.number_input("Total Deductions", min_value=0)
hra_claimed = st.checkbox("Claiming HRA?")

if st.button("Analyze"):

    payload = {
        "income": income,
        "deductions": deductions,
        "hra_claimed": hra_claimed
    }

    response = requests.post(BACKEND_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        st.subheader("📊 Tax Comparison")
        st.json(result)

        if result["risks"]:
            st.error("⚠ Compliance Risks Detected!")

    else:
        st.error("Backend error")