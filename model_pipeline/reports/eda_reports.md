## Dataset Description

The dataset contains **simulated delivery records** with relevant features that potentially influence delivery times, such as weather conditions, traffic level, distance, and preparation time. It includes **1,000 rows** with the following variables:

- **Numerical features**:  
  `Distance_km`, `Preparation_Time_min`, `Courier_Experience_yrs`, `Delivery_Time_min` (target)

- **Categorical features**:  
  `Weather`, `Traffic_Level`, `Time_of_Day`, `Vehicle_Type`

## Missing Data

I identified **30 missing values** in each of the following columns:

- `Weather` 
- `Traffic_Level`
- `Time_of_Day` 
- `Courier_Experience_yrs`

The missing values were **dispersed across different rows** (i.e., not concentrated in the same 30 records). I applied imputation based on the data type:

- **Categorical features**: Imputed using the **mode**.
- **Numerical feature (`Courier_Experience_yrs`)**:  
  After confirming a fairly uniform distribution across the values (0–9 years), I decided to impute missing values using the **median**, which is more robust to potential outliers.

## Outliers

Using the interquartile range method, I detected 6 outliers in the target variable `Delivery_Time_min`, representing just 0.6% of the dataset.

I also checked for outliers in the other numeric features (`Distance_km`, `Preparation_Time_min`, `Courier_Experience_yrs`) and no significant outliers were found.

Given that the detected outliers in the target might represent legitimate cases (long distances or difficult traffic scenarios), I chose to retain them in the dataset.

## Feature Relationships

An initial **correlation analysis** and **scatter plots** revealed the following:

- `Distance_km` has the strongest positive correlation with `Delivery_Time_min`.
- `Preparation_Time_min` is also moderately correlated with the target.
- Visualizations like the scatterplot between `Distance_km` and `Delivery_Time_min` confirmed a **linear trend**, supporting its relevance in modeling.

## Initial Assumptions

- The features **`Distance_km`**, **`Preparation_Time_min`**, and **`Traffic_Level`** are expected to be the **most influential** factors in predicting delivery time.

---------

The complete exploratory analysis, data cleaning steps, and code used to generate the figures in this report are available in the notebook:
**Full notebook**: [notebooks/EDA.ipynb](../notebooks/EDA.ipynb)
