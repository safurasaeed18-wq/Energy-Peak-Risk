import pandas as pd


def load_data(filepath):
    """
    Load household power consumption dataset.
    """

    df = pd.read_csv(
        filepath,
        sep=";",
        low_memory=False,
        na_values="?"
    )

    return df


if __name__ == "__main__":
    df = load_data("../data/raw/household_power_consumption.txt")
    print(df.head())
    print(df.shape)