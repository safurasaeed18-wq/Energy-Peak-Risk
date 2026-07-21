import joblib
import pandas as pd

from sklearn.ensemble import GradientBoostingRegressor


def train_model(X_train, y_train):

    model = GradientBoostingRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


if __name__ == "__main__":

    print("Training module is ready.")