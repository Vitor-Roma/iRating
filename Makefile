all:
	docker-compose up --build
	docker-compose -f docker-compose-worker.yml up --build
build:
	python3 manage.py makemigrations
	docker exec irating pip3 install --upgrade pip
	docker exec irating pip3 install -r requirements.txt
	docker exec irating python3 manage.py migrate

test:
	docker exec irating python3 manage.py test --noinput

run:
	docker-compose up

worker-up:
	docker-compose -f docker-compose-worker.yml up

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
	docker attach -it irating

enter:
	docker exec -it irating /bin/bash

search:
	docker exec -it irating python3 manage.py search_index --rebuild

log:
	docker-compose logs irating -f --tail 100

worker-log:
	docker-compose logs worker -f --tail 100