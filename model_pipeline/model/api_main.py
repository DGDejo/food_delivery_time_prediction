from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from predict import predict_delivery_time

app = FastAPI()

class DeliveryInput(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: int
    Courier_Experience_yrs: float

class DeliveryOutput(BaseModel):
    predicted_delivery_time: float

@app.post("/predict", response_model=DeliveryOutput)
def predict(input_data: DeliveryInput):
    df = pd.DataFrame([input_data.model_dump()])
    pred = predict_delivery_time(df)
    return {"predicted_delivery_time": round(pred[0], 2)}
