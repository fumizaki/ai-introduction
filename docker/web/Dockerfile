FROM python:3.11.9-bookworm

WORKDIR /web

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Poetryをダウンロードしてインストール
RUN curl -sSL https://install.python-poetry.org | python -

# Pathを通す
ENV PATH /root/.local/bin:$PATH
# 仮想環境をたてない
RUN poetry config virtualenvs.create false

# アプリケーションの依存関係をインストール
COPY ./app/web/pyproject.toml ./app/web/poetry.lock .
RUN poetry install

COPY ./app/web .

CMD ["bash", "-c", "streamlit run main.py"]
