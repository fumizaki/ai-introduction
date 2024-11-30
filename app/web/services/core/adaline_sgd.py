from __future__ import annotations
import numpy as np

class AdalineSGD:

    def __init__(
            self,
            eta: float = 0.01,
            epoch: int = 50,
            shuffle: bool = True,
            seed: int = 1
        ) -> None:
        # 学習率
        self.eta = eta
        # データセットの訓練回数
        self.epoch = epoch
        # 循環回避のためにエポックごとに訓練データをシャッフルするか否か
        self.shuffle = shuffle
        # 重み
        self.weight: np.ndarray
        # 重みの初期化フラグ
        self.w_initialized = False
        # バイアスユニット
        self.bias: np.float64
        # 各エポックにおけるMSE誤差関数の値
        self.losses: list[float]
        # 乱数シードから
        self.random_state = np.random.RandomState(seed)

    def fit(self, x: np.ndarray, y: np.ndarray) -> AdalineSGD:
        self._initialize_weights(x.shape[1])
        self.losses = []

        for _ in range(self.epoch):
            if self.shuffle:
                x, y = self._shuffle(x, y)

            losses = []
            for x_i, y_i in zip(x, y):
                # 特徴量x_iと目的変数yを使った重みの更新と損失値の計算
                losses.append(self._update_weights(x_i, y_i))
            # 訓練データの平均損失値の計算
            avg_loss = np.mean(losses)
            self.losses.append(avg_loss)

        return self
    

    def _shuffle(self, x: np.ndarray, y: np.ndarray):
        r = self.random_state.permutation(len(y))
        return x[r], y[r]
    
    def _initialize_weights(self, size):
        self.weight = self.random_state.normal(loc = 0.0, scale = 0.01, size = size)
        self.bias = np.double(0.)
        self.w_initialized = True

    def _update_weights(self, x: np.ndarray, y: np.ndarray):
        output = self.activation(self.net_input(x))
        error = y - output
        self.weight += self.eta * 2.0 * x * error
        self.bias += self.eta * 2.0 * error
        loss = error ** 2
        return loss


    def net_input(self, x: np.ndarray) -> float:
        # 総入力を計算
        return np.dot(x, self.weight) + self.bias
    
    def activation(self, x: np.ndarray) -> np.ndarray:
        # 線形活性化関数の出力を計算
        return x

    def predict(self, x: np.ndarray) -> np.ndarray:
        # 1ステップ後のクラスラベルを返す
        return np.where(self.activation(self.net_input(x)) >= 0.5, 1, 0)