.PHONY: docker-up docker-down docker-free


# Dockerコンテナ起動
docker-up:
	docker compose -f compose.yml up -d --build

# Dockerコンテナ削除
docker-down:
	docker compose -f compose.yml down --rmi all

# Dockerコンテナ解放
docker-free:
	docker system prune
