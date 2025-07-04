## 1. Chosen Model

After evaluating multiple regression models using cross-validation, I selected Ridge Regression as the final model due to its strong performance and robust generalization.

In contrast, more complex models like **Random Forest** and **XGBoost** showed signs of overfitting and slightly worse test set performance.

## 2. Modeling Approach

The modeling pipeline was structured using pipelines and transformers to ensure modularity and reproducibility.

- **Numerical features**: `Distance_km`, `Preparation_Time_min`, `Courier_Experience_yrs`
  - Passed through without scaling.
- **Categorical features**: `Weather`, `Traffic_Level`, `Time_of_Day`, `Vehicle_Type`
  - Encoded using **OneHotEncoder(drop='first')** to avoid multicollinearity from dummy variables.

The full pipeline was wrapped in a Pipeline object and used for both training and evaluation.

## 3. Metric Choice

- **Primary metric**: **Mean Absolute Error (MAE)**  
  MAE was chosen because it is intuitive (measured in minutes) and not heavily penalized by outliers. This way it would be easier for the Ops team to respond more intelligently 

- **Secondary metrics**: **Root Mean Squared Error (RMSE)** and **R² score**
  Used for model comparison.

## 4. Cross-Validation Strategy

Due to the relatively small dataset (1,000 rows), I opted to use Repeated K-Fold Cross-Validation instead of a simple train-test split to maximize the use of available data and reduce variance in evaluation.

- This results in 15 different train/validation splits, improving reliability of model evaluation.
- All scores reported (MAE, RMSE, R²) reflect average performance across these repeated folds.

## 5. Hyperparameter Tuning

To tune the regularization strength alpha for Ridge regression, I used **RidgeCV**, which automatically selects the best alpha using internal cross-validation across predefined values.

## 6. Model Comparison

To validate the performance of Ridge regression, I also tested other commonly used regression models:

- **Random Forest Regressor**
- **XGBoost Regressor**
- **Linear Regression**

| Model               | MAE (Train) | MAE (Test) | MAE (CV) | RMSE (Test) | R² (Test) |
|---------------------|-------------|------------|----------|-------------|-----------|
| Ridge               | 6.47        | 6.38       | 6.60     | 9.59        | 0.787     |
| Linear Regression   | 6.46        | 6.37       | 6.60     | 9.57        | 0.788     |
| Random Forest       | 4.35        | 7.28       | 7.52     | 10.69       | 0.736     |
| XGBoost             | 5.74        | 6.74       | 7.07     | 9.96        | 0.771     |

- Ridge and Linear Regression performed equally well, but Ridge adds robustness through L2 regularization, making it more stable for future unseen data.
- Random Forest and XGBoost showed lower training errors, but worse generalization on both test and cross-validation, suggesting overfitting.

The complete model experimentation is available in the notebook:
**Full notebook**: [notebooks/model.ipynb](../notebooks/model.ipynb)

## 7. Multicollinearity Check

I checked for multicollinearity among the input features using the **Variance Inflation Factor (VIF)**.

- All VIF values were below commonly accepted thresholds (VIF < 5).

Therefore, multicollinearity was not a concern in this dataset, and Ridge regularization was used as an additional safety layer to stabilize coefficients and improve generalization.

## 8. Final Notes

Ridge regression not only performed best in cross-validation but also aligns well with the project goals:

- Predictive performance is solid (MAE of aproximately 6.4 minutes).
- The model is fast and interpretable.
- Regularization ensures resilience if the dataset changes over time.

This makes it a strong candidate for integration into operational forecasting or optimization tools.
