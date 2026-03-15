import streamlit as st
import joblib
import pandas as pd

model = joblib.load("../models/energy_model.pkl")

st.title("Energy Consumption Prediction")

temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
square = st.number_input("Square Footage")
occupancy = st.number_input("Occupancy")
hvac = st.number_input("HVAC Usage")
lighting = st.number_input("Lighting Usage")
renewable = st.number_input("Renewable Energy")
day = st.number_input("Day Of Week")
holiday = st.selectbox("Holiday",[0,1])
hour = st.number_input("Hour")
month = st.number_input("Month")

if st.button("Predict"):

    data = pd.DataFrame({
        "Temperature":[temperature],
        "Humidity":[humidity],
        "SquareFootage":[square],
        "Occupancy":[occupancy],
        "HVACUsage":[hvac],
        "LightingUsage":[lighting],
        "RenewableEnergy":[renewable],
        "DayOfWeek":[day],
        "Holiday":[holiday],
        "Hour":[hour],
        "Month":[month]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Energy Consumption: {prediction[0]}")
