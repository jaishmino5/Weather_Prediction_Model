import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("Temperature_Prediction_Model")

# Streamlit UI
st.title("Temperature Prediction App")

# User Input
hour = st.number_input("Hour", min_value=0, max_value=23, step=1)
minute = st.number_input("Minute", min_value=0, max_value=59, step=1)
second = st.number_input("Second", min_value=0, max_value=59, step=1)

# Predict Button
if st.button("Predict Temperature"):
    # Prepare input
    input_data = np.array([[hour, minute, second]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"Predicted Temperature: {prediction:.2f}°C")
