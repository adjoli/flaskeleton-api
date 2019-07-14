container=app

up:
	docker-compose up -d

up-debug:
	docker-compose up

build:
	docker-compose rm -vsf
	docker-compose down -v --remove-orphans
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

run:
	docker-compose run {container} /bin/bash

jumpin:
	docker-compose run {container} bash

test:
	docker-compose run {container} pytest ./tests/

test-file:
	docker-compose run {container} pytest ./tests/ --group $(FILE)

tail-logs:
	docker-compose logs -f {container}
