-include .env

init:
	docker-compose build

run:
	docker-compose up web

generate_migrations:
	$(eval message ?= *)
	docker-compose run --rm web alembic revision --autogenerate -m "$(message)"

migrate:
	docker-compose run --rm web alembic upgrade head

psql:
	docker-compose run --rm db psql -h db -U $(POSTGRES_USER) $(POSTGRES_DB)