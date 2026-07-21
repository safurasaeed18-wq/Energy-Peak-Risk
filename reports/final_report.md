# Energy Peak Risk Prediction

## Executive Summary
This project predicts household energy consumption using machine learning models. The goal is to estimate power demand and identify potential peak energy usage to support better energy management.

## Problem Statement
High electricity demand during peak hours increases operational costs and stress on the power grid. The objective is to predict Global Active Power using historical household electricity consumption data.

## Dataset
- Dataset: Individual Household Electric Power Consumption
- Rows: 2,075,259
- Features: 9 original columns
- Target: Global_active_power

## Data Preprocessing
- Removed missing values
- Converted data types
- Feature selection
- Train (70%), Validation (15%), Test (15%)

## Models Used
- Dummy Regressor
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

## Results

| Model | MAE | RMSE | R² |
|------|------|------|------|
| Dummy Regressor | 0.8087 | 1.0556 | -0.0246 |
| Linear Regression | 0.0247 | 0.0366 | 0.9988 |
| Random Forest | 0.0241 | 0.0372 | 0.9987 |
| Gradient Boosting | 0.0201 | 0.0306 | 0.9991 |

## Best Model
Gradient Boosting Regressor achieved the best performance with the highest R² score and the lowest prediction error.

## Deployment
A Streamlit application was developed to demonstrate the project.

## Conclusion
Machine learning can accurately predict household energy consumption. The developed model can assist in forecasting electricity demand and identifying potential peak usage periods.