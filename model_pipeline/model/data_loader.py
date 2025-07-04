from pathlib import Path
import pandas as pd
import kagglehub

DATASET_ID   = "denkuznetz/food-delivery-time-prediction"
CSV_FILENAME = "Food_Delivery_Times.csv"

def download_dataset() -> Path:
    path = kagglehub.dataset_download(DATASET_ID)
    return Path(path) / CSV_FILENAME

def load_data() -> pd.DataFrame:
    csv_path = download_dataset()
    df = pd.read_csv(csv_path)
    return df
