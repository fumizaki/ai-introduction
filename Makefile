.PHONY: docker-up docker-down docker-free

# デフォルトの環境を local に設定
ENV ?= local

# Dockerコンテナ起動
docker-up:
	docker compose -f compose.${ENV}.yml up -d --build

# Dockerコンテナ削除
docker-down:
	docker compose -f compose.${ENV}.yml down --rmi all

# Dockerコンテナ解放
docker-free:
	docker system prune
