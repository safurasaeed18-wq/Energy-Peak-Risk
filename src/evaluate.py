import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_model(model, X, y):
    """
    Evaluate trained regression model.
    """

    predictions = model.predict(X)

    mae = mean_absolute_error(y, predictions)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    r2 = r2_score(y, predictions)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }


if __name__ == "__main__":
    print("Evaluation module is ready.")