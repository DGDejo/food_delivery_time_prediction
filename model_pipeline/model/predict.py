import pandas as pd
import joblib
from config import CAT_COLS, NUM_COLS

def predict_delivery_time(input_data: pd.DataFrame, model_path: str = "ridge/model.joblib") -> pd.Series:
    model = joblib.load(model_path)
    X = input_data[CAT_COLS + NUM_COLS]
    return model.predict(X)