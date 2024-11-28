import pandas as pd


def get_dataframe() -> pd.DataFrame:
    data = {
        "sepal_length": [5.1, 4.9, 4.7, 4.6, 5.0],
        "sepal_width": [3.5, 3.0, 3.2, 3.1, 3.6],
        "petal_length": [1.4, 1.4, 1.3, 1.5, 1.4],
        "petal_width": [0.2, 0.2, 0.2, 0.2, 0.2],
        "species": ["setosa", "setosa", "setosa", "setosa", "setosa"],
    }
    return pd.DataFrame(data)


def get_mean_petal_length() -> float:
    df = get_dataframe()
    return df["petal_length"].mean()


