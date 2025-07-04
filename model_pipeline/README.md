# Delivery Time Prediction API

A basic FastAPI service that provides delivery time predictions based on input features such as distance, weather, traffic level, and more. 
The model is pre-trained and loaded to return predictions via a simple POST request.

## How to Run the API Locally

1. Clone the repository
- git clone https://github.com/DGDejo/food_delivery_time_prediction.git

2. Install Dependencies

- cd food_delivery_time_prediction/model_pipeline
- pip install -r requirements.txt

3. Navigate to the model folder
- cd model

## Create and Activate Virtual Environment

## Run the API

uvicorn api_main:app --reload

## Check Documentation

If running locally, use http://127.0.0.1:8000/redoc

## Test the Endpoint

- Once the server is running at http://127.0.0.1:8000, you can test it using curl, Postman
- Sample Request:
    {
    "Distance_km": 7.2,
    "Weather": "Rainy",
    "Traffic_Level": "High",
    "Time_of_Day": "Morning",
    "Vehicle_Type": "Scooter",
    "Preparation_Time_min": 15,
    "Courier_Experience_yrs": 3
    }
- Sample Response:
    {
    "predicted_delivery_time": 53.40
    }
