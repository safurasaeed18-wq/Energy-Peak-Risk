from src.data import load_data


def test_data_loading():
    df = load_data("data/raw/household_power_consumption.txt")

    assert len(df) > 0
    assert "Global_active_power" in df.columns

    print("✅ All tests passed.")


if __name__ == "__main__":
    test_data_loading()