import streamlit as st
import requests

url = 'https://taxifare.lewagon.ai/predict'

# Streamlit interface
st.title('Taxi Fare Predictor')

# Input fields for user
pickup_datetime = st.text_input('Pickup Date and Time', '2024-05-30 12:34:56')
pickup_longitude = st.number_input('Pickup Longitude', -73.985428)
pickup_latitude = st.number_input('Pickup Latitude', 40.748817)
dropoff_longitude = st.number_input('Dropoff Longitude', -73.985428)
dropoff_latitude = st.number_input('Dropoff Latitude', 40.748817)
passenger_count = st.number_input('Passenger Count', 1)

if st.button('Predict Fare'):
    # Create API parameters
    api_params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count,
    }

    # Send GET request to the API
    response = requests.get(url, params=api_params)

    if response.status_code == 200:
        # Display the response from the API
        fare = response.json().get('fare', 'No fare returned')
        st.success(f'Predicted Fare: ${fare}')
    else:
        st.error('Error in API request')
