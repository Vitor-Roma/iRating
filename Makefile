all:
	docker-compose up --build -d
	docker-compose -f docker-compose-worker.yml up --build -d
build:
	docker exec -i irating python3 manage.py migrate

migrations:
	docker exec irating python3 manage.py makemigrations

test:
	docker exec irating python3 manage.py test --noinput

run:
	docker-compose down --remove-orphans
	docker-compose up -d
	docker-compose -f docker-compose-worker.yml up -d


worker-run:
	docker-compose -f docker-compose-worker.yml up -d

down:
	docker-compose down --remove-orphans


worker-down:
	docker-compose -f docker-compose-worker.yml down

scrap-ifood:
	docker exec irating python3 manage.py ifood

coverage:
	docker exec irating coverage run manage.py test
	docker exec irating coverage report
	docker exec irating coverage html

attach:
	docker attach irating

enter:
	docker exec -it irating /bin/bash

search:
	docker exec -it irating python3 manage.py search_index --rebuild
