import streamlit as st
import requests
from datetime import datetime

# App title
st.title("Taxi Fare Predictor")

# Introduction
st.markdown('''
This application predicts the taxi fare for a ride in New York City.
Fill in the ride details, and we'll provide an estimated fare using our AI-powered model.
''')

# Input fields
st.header("Enter Ride Details")
pickup_datetime = st.text_input("Pickup Date and Time (YYYY-MM-DD HH:MM:SS)", value=str(datetime.now()))
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)

# API URL
api_url = 'https://taxifare.lewagon.ai/predict'

# Prediction logic
if st.button("Get Fare Prediction"):
    # Constructing the payload
    payload = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    try:
        # API call
        response = requests.get(api_url, params=payload)
        response_data = response.json()

        # Displaying the result
        fare = response_data.get("fare", "Error")
        st.success(f"The predicted fare is: ${fare:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown('''
**Note:** The predictions are provided by a machine learning model and may not always reflect the actual fare.
''')
