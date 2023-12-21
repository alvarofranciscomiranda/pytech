build:
	docker build --tag pytech:latest .

run:
	docker run --name populate pytech:latest --env-file .env

all:
	build; run