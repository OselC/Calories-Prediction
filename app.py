import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("linear_regression_model.pkl")

st.title("Calories Burned Prediction")
st.write("Predict calories burned during exercise using a Linear Regression model.")

# User inputs
gender = st.selectbox("Gender", ["male", "female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
height = st.number_input("Height (cm)", min_value=120.0, max_value=220.0, value=170.0)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
duration = st.number_input("Exercise Duration (minutes)", min_value=1.0, max_value=300.0, value=30.0)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40.0, max_value=200.0, value=120.0)
body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)

# Create input dataframe (must match training columns exactly)
input_data = pd.DataFrame({
    "Gender": [gender],
    "Age": [age],
    "Height": [height],
    "Weight": [weight],
    "Duration": [duration],
    "Heart_Rate": [heart_rate],
    "Body_Temp": [body_temp]
})

if st.button("Predict Calories"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Calories Burned: {prediction[0]:.2f} cal")
