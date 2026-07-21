import joblib
import pandas as pd


def predict(model, X):
    """
    Make predictions using a trained model.
    """
    return model.predict(X)


if __name__ == "__main__":
    print("Prediction module is ready.")