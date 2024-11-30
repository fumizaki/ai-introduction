import pandas as pd


def get_dataframe() -> pd.DataFrame:
    return pd.read_csv('dataset/Iris.csv', header=0, encoding='utf-8')


def get_mean(df: pd.DataFrame, key: str) -> float:
    return df[key].mean()


