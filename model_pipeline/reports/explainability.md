## 1. Overview

To better understand how the Ridge regression model makes its predictions, I analyzed the feature importance using:

- **Model coefficients**: extracted from the fitted Ridge model.
- **Bar chart** showing the top 10 absolute coefficients.

This allows for clear interpretability and supports operational decisions based on the model.

## 2. Methodology

The feature importances were extracted using the following steps:

1. The final model  was accessed via .best_estimator_
2. The fitted OneHotEncoder provided the names of the transformed categorical features.
3. Coefficients from Ridge were aligned with the full feature set.
4. A DataFrame was constructed to sort and visualize the top contributors.

## 3. Interpretation

the top influential features based on this dataframe were:
- `Weather_Rainy`: Rainy weather decreases predicted time.
- `Courier_Experience_yrs`: More experienced couriers lead to longer delivery times, counterintuitively.
- `Distance_km`: longer distances increase delivery time.
- `Time_of_Day_Night`: Night deliveries are generally slower.
- `Preparation_Time_min`: Longer prep time contributes to overall delay.

## 4. Summary

Distance_km and Preparation_Time_min behave as expected and are strong predictors.

Some encoded categorical features (Weather_Rainy, Time_of_Day_Night) contribute meaningful adjustments.

The model is interpretable and aligned with operational logic, though certain patterns (courier experience) may need further investigation.