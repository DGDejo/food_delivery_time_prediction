# Breakdown by exam part

## Part 1: SQL
All SQL analysis are located in the sql/ folder.
sql_insights.md contains reasoning and business interpretation.
sql_queries.sql contains the raw queries used.

## Part 2: Modeling
Core modeling code is located in model/:
- train_model.py, predict.py, preprocessing.py, etc.
- Utility modules help structure the pipeline in a clean, modular way.
- test_predict.py includes minimal test coverage for predictions.

Notebooks and Reporting
- notebooks/: Used for exploration, prototyping, and visualizations.
- reports/: Markdown summaries and findings throughout the modeling process.

## Part 3 (Optional): API Prototype
Located in api_main.py inside the model/ folder.
Built using FastAPI to serve real-time delivery time predictions.
