from pathlib import Path
from typing import Dict

import joblib
import pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline

from preprocessing import build_preprocessor

def build_ridge_pipeline(cv) -> Pipeline:
    
    preprocessor = build_preprocessor()
    ridge = RidgeCV(alphas=[0.01, 0.1, 1, 5, 10, 50, 100], cv=cv, scoring="neg_mean_absolute_error")
    pipe = Pipeline(steps=[("prep", preprocessor), ("reg", ridge)])
    return pipe

def get_artifact_dir() -> Path:
    artifact_dir = Path('ridge') 
    artifact_dir.mkdir(parents=True, exist_ok=True)
    return artifact_dir

def save_model(pipe: Pipeline, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, path)
    print(f"model saved in {path}")

def load_model(path: Path) -> Pipeline:
    return joblib.load(path)

def evaluate(
    pipe: Pipeline,
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    cv,
) -> Dict[str, float]:
    
    pipe.fit(X_train, y_train)

    preds_train = pipe.predict(X_train)
    preds_test = pipe.predict(X_test)

    mae_train = mean_absolute_error(y_train, preds_train)

    mae_cv = -cross_val_score(
        pipe,
        X_train,
        y_train,
        scoring="neg_mean_absolute_error",
        cv=cv,
        n_jobs=-1,
    ).mean()

    mae_test = mean_absolute_error(y_test, preds_test)
    rmse_test = root_mean_squared_error(y_test, preds_test)
    r2_test = r2_score(y_test, preds_test)

    return {
        "mae_train": mae_train,
        "mae_cv": mae_cv,
        "mae_test": mae_test,
        "rmse_test": rmse_test,
        "r2_test": r2_test,
    }
