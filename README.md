# Breakdown by part

## Cloning the repository
git clone https://github.com/DGDejo/food_delivery_time_prediction.git

The entire assignment is inside model_pipeline.

## Part 1: SQL
All SQL analysis are located in the sql/ folder.
sql_insights.md contains reasoning and business interpretation.
sql_queries.sql contains the raw queries used.

## Part 2: Modeling
Core modeling code is located in the `model/` directory:
- `train_model.py`: trains the final model and saves it under `model/experiments/ridge/` so it can be loaded and used by `predict.py`.
- `predict.py`: loads the serialized model and returns predictions based on new data.
- `preprocessing.py`: defines all transformation logic used in the pipeline.
- Utility modules (`model_utils.py`, `config.py`, `data_loader.py`) help structure the code in a clean, modular, and maintainable way.
- `test_predict.py`: provides basic test coverage to verify prediction functionality.

Notebooks and Reporting
- notebooks/: Used for exploration, prototyping, and visualizations.
- reports/: Markdown summaries and findings throughout the modeling process.

## Part 3: API Prototype
Located in api_main.py inside the model/ folder.
Built using FastAPI to serve real-time delivery time predictions.
