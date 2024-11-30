from __future__ import annotations
import numpy as np


class Perceptron:

    def __init__(
            self,
            eta: float = 0.01,
            epoch: int = 50,
            random_seed: int = 1
        ) -> None:
        # 学習率
        self.eta = eta
        # データセットの訓練回数
        self.epoch = epoch
        # 乱数シード
        self.random_seed = random_seed
        # 重み
        self.weight: np.ndarray
        # バイアスユニット
        self.bias: np.float64
        # 各エポックにおける誤分類の回数
        self.errors: list[int]


    def fit(self, training: np.ndarray, target: np.ndarray) -> Perceptron:
        random_state = np.random.RandomState(self.random_seed)
        # 標準偏差0.01の正規分布から乱数を生成
        self.weight = random_state.normal(loc = 0.0, scale = 0.01, size = training.shape[1])
        self.bias = np.double(0.)
        self.errors = []

        for _ in range(self.epoch):
            error = 0
            for training_i, target_i in zip(training, target):
                delta = self.eta * (target_i - self.predict(training_i))
                self.weight += delta * training_i
                self.bias += delta
                error += int(delta != 0.0)
            self.errors.append(error)
        return self

    def net_input(self, x: np.ndarray) -> float:
        # 総入力を計算
        return np.dot(x, self.weight) + self.bias

    def predict(self, x: np.ndarray) -> np.ndarray:
        # 1ステップ後のクラスラベルを返す
        return np.where(self.net_input(x) >= 0.0, 1, 0)