from predict import predict_delivery_time
import pandas as pd

def run_manual_test():
    "Simple test for prediction.py"
    sample = pd.DataFrame([{
        "Distance_km": 10,
        "Weather": "Clear",
        "Traffic_Level": "Low",
        "Time_of_Day": "Morning",
        "Vehicle_Type": "Bike",
        "Preparation_Time_min": 10,
        "Courier_Experience_yrs": 2.0
    }])
    
    pred = predict_delivery_time(sample)
    print("Prediction:", pred)
    assert len(pred) == 1 and isinstance(pred[0], float)
    print("Test passed.")

if __name__ == "__main__":
    run_manual_test()
