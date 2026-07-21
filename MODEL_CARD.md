# MODEL CARD

## Model Name

Gradient Boosting Regressor

## Problem Type

Regression

## Target Variable

Global_active_power

## Input Features

- Global_reactive_power
- Voltage
- Global_intensity
- Sub_metering_1
- Sub_metering_2
- Sub_metering_3
- Hour
- Day
- Month
- Year
- DayOfWeek
- Weekend
- Other engineered features

## Evaluation Metrics

- MAE: 0.0201
- RMSE: 0.0306
- R² Score: 0.9991

## Intended Use

Predict household electricity demand to help identify potential peak electricity usage.

## Limitations

- Trained on data from one household.
- Does not include weather or occupancy information.
- Performance may decrease on unseen environments.

## Ethical Considerations

Predictions should support human decision-making and not be the sole basis for operational decisions.