from __future__ import annotations
import numpy as np

class AdalineGD:

    def __init__(
            self,
            eta: float = 0.01,
            epoch: int = 50,
            seed: int = 1
        ) -> None:
        # 学習率
        self.eta = eta
        # データセットの訓練回数
        self.epoch = epoch
        # 乱数シード
        self.random_state = np.random.RandomState(seed)
        # 重み
        self.weight: np.ndarray
        # バイアスユニット
        self.bias: np.float64
        # 各エポックにおけるMSE誤差関数の値
        self.losses: list[float]

    def fit(self, x: np.ndarray, y: np.ndarray) -> AdalineGD:
        # 標準偏差0.01の正規分布から乱数を生成
        self.weight = self.random_state.normal(loc = 0.0, scale = 0.01, size = x.shape[1])
        self.bias = np.double(0.)
        self.losses = []

        for _ in range(self.epoch):
            net_input = self.net_input(x)
            output = self.activation(net_input)

            errors = y - output
            self.weight += self.eta * 2.0 * x.T.dot(errors) / x.shape[0]
            self.bias += self.eta * 2.0 * errors.mean()
            loss = (errors ** 2).mean()
            self.losses.append(loss)

        return self
    

    def net_input(self, x: np.ndarray) -> float:
        # 総入力を計算
        return np.dot(x, self.weight) + self.bias
    
    def activation(self, x: np.ndarray) -> np.ndarray:
        # 線形活性化関数の出力を計算
        return x

    def predict(self, x: np.ndarray) -> np.ndarray:
        # 1ステップ後のクラスラベルを返す
        return np.where(self.activation(self.net_input(x)) >= 0.5, 1, 0)