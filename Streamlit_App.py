import streamlit as st
import numpy as np
import pickle

# Load the model
with open("temperature_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Temperature Prediction App", layout="centered")
st.title("🌡️ Temperature Prediction App")

st.markdown("### Enter time details (24-hour format)")
st.markdown("- **Hour:** 0–23")
st.markdown("- **Minute:** 0–59")
st.markdown("- **Second:** 0–59")

# User Input
col1, col2, col3 = st.columns(3)

with col1:
    hour = st.number_input("Hour (0–23)", min_value=0, max_value=23, step=1, format="%d")

with col2:
    minute = st.number_input("Minute (0–59)", min_value=0, max_value=59, step=1, format="%d")

with col3:
    second = st.number_input("Second (0–59)", min_value=0, max_value=59, step=1, format="%d")

# Predict Button
if st.button("Predict Temperature"):
    # Optional check (good if you switch to text_input in future)
    if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
        st.error("❌ Please enter valid values for Hour (0–23), Minute (0–59), and Second (0–59).")
    else:
        # Prepare input
        input_data = np.array([[hour, minute, second]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Display result
        st.success(f"🌡️ Predicted Temperature: **{prediction:.2f}°C**")
