## Feature-Driven Error Patterns

### `Courier_Experience_yrs`

- Although the model gave it a positive coefficient (+8.80), this is counterintuitive.
- This may reflect:
  - More experienced couriers may be assigned to harder deliveries.
  - Unmodeled interactions (e.g., experience × traffic).
  - Bias in the simulated data.

### `Weather = Rainy`

- The model assigned a strong negative coefficient (−11.06) to `Weather_Rainy`.
- I would expect rain to increase delivery time, so this is likely:
  - Simulated patterns where rain is associated with fewer or shorter deliveries.
  - Or a side-effect of how the one-hot encoding structured the base categories.

## Root Causes of Model Limitations

- **Lack of non-linear interactions**: Ridge cannot model relationships like `distance × traffic`, or `experience × time_of_day`
- **Low sample size in edge cases**: Very few deliveries in snow/rain or at long distances hurt generalization.
- **Synthetic data structure**: As this is simulated data, some learned correlations may be artifacts rather than real-world relationships.

## Recommendations

- Add interaction features (e.g. `Distance × Traffic`) to improve handling of congestion-related delays
- Increase sample size for rare edge cases (snowy days, long distances).
- Group or bin courier experience levels to reduce noise and overfitting in linear models.

## Final Thoughts

The Ridge model performs well in general, but its linear nature limits performance under certain conditions (long distances, severe weather, high experience). 
The model could work better in future iterations with better feature engineering or data augmentation.
