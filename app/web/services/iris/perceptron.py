import pandas as pd
import numpy as np
from services.core.perceptron import Perceptron
from services.iris.dataframe import get_dataframe


def get_target(df: pd.DataFrame) -> np.ndarray:
    target = df.iloc[0:100, 5].values
    return np.where(target == 'Iris-setosa', 0, 1)

def get_train(df: pd.DataFrame):
    return df.iloc[0:100, [1, 3]].values


def fit(train: np.ndarray, target: np.ndarray) -> Perceptron:
    perceptron = Perceptron(eta = 0.1, epoch = 10)
    return perceptron.fit(train, target)