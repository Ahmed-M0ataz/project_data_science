# Data Science Project: Predicting House Power Consumption

## Introduction

This data science project aims to predict the power consumption of a house using various features such as temperature, humidity, and weather conditions. The project involves data import, data exploration, analysis, data visualization, and the development of a machine learning model for power consumption prediction.

## Dataset

The dataset used for this project contains the following columns:

1. **date:** Time in the format year-month-day hour:minute:second.
2. **Appliances:** Energy use in Wh.
3. **lights:** Energy use of light fixtures in the house in Wh.
4. **T1:** Temperature in the kitchen area, in Celsius.
5. **RH_1:** Humidity in the kitchen area, in %.
6. **T2:** Temperature in the living room area, in Celsius.
7. **RH_2:** Humidity in the living room area, in %.
8. **T3:** Temperature in the laundry room area, in Celsius.
9. **RH_3:** Humidity in the laundry room area, in %.
10. **T4:** Temperature in the office room, in Celsius.
11. **RH_4:** Humidity in the office room, in %.
12. **T5:** Temperature in the bathroom, in Celsius.
13. **RH_5:** Humidity in the bathroom, in %.
14. **T6:** Temperature outside the building (north side), in Celsius.
15. **RH_6:** Humidity outside the building (north side), in %.
16. **T7:** Temperature in the ironing room, in Celsius.
17. **RH_7:** Humidity in the ironing room, in %.
18. **T8:** Temperature in teenager room 2, in Celsius.
19. **RH_8:** Humidity in teenager room 2, in %.
20. **T9:** Temperature in parents' room, in Celsius.
21. **RH_9:** Humidity in parents' room, in %.
22. **To:** Temperature outside (from Chievres weather station), in Celsius.
23. **Pressure:** Pressure (from Chievres weather station), in mm Hg.
24. **RH_out:** Humidity outside (from Chievres weather station), in %.
25. **Wind speed:** Wind speed (from Chievres weather station), in m/s.
26. **Visibility:** Visibility (from Chievres weather station), in km.
27. **Tdewpoint:** Dew point (from Chievres weather station), in °C.
28. **rv1:** Random variable 1, nondimensional.
29. **rv2:** Random variable 2, nondimensional.

## Project Steps

### 1. Data Import

- The dataset was imported, and the necessary libraries were used to manipulate and analyze the data.

### 2. Data Exploration

- Exploratory Data Analysis (EDA) was performed to gain insights into the dataset.
- Descriptive statistics, data distribution, and data quality checks were conducted.

### 3. Data Analysis

- Correlations between different features and power consumption were analyzed.
- Patterns and trends in the data were identified.

### 4. Data Visualization

- Data visualizations such as histograms, scatter plots, and heatmaps were created to illustrate findings from the analysis.

### 5. Machine Learning Model

- A machine learning model was developed to predict house power consumption.
- Features were selected and preprocessed as needed.
- Model evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) were used to assess model performance.

### 6. Model Tuning

- Hyperparameter tuning was performed to optimize the model's performance.
- Techniques like Grid Search Cross-Validation were used to find the best hyperparameters.

## Conclusion

This data science project successfully analyzed and predicted house power consumption based on various factors. The machine learning model's performance was optimized through hyperparameter tuning, and the project provides valuable insights into energy usage patterns.

## Acknowledgments

We would like to acknowledge the source of the dataset and any external libraries or resources used during the project.
