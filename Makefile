app_name = rishat_test_project
loc_services := postgres backend
docker_compose := docker compose -f docker-compose.yml

#build
build:
	$(docker_compose) build $(c)

rebuild:
	$(docker_compose) up -d --build --force-recreate $(c)
	docker image prune -f

up:
	$(docker_compose) up -d $(c)

up-loc:
	$(docker_compose) up -d $(loc_services) $(c)

start:
	$(docker_compose) start $(c)

down:
	$(docker_compose) down $(c)

reup:
	$(docker_compose) down $(c)
	$(docker_compose) up -d $(c)

reup-loc:
	$(docker_compose) down $(c)
	$(docker_compose) up -d $(loc_services) $(c)

destroy:
	$(docker_compose) down --rmi all -v $(c)

stop:
	$(docker_compose) stop $(c)

restart:
	$(docker_compose) restart $(c)

#logs
logs:
	$(docker_compose) logs --tail=1000 -f $(c)

app-logs:
	$(docker_compose) logs --tail=1000 -f backend $(c)

#bash
app-bash:
	docker exec -it $(app_name)_backend bash $(c)

db-bash:
	docker exec -it $(app_name)_postgres bash $(c)

#migrations
migrations:
	docker exec -it $(app_name)_backend python -m app.manage makemigrations

migrate:
	docker exec -it $(app_name)_backend python -m app.manage migrate

psql:
	docker exec -it $(app_name)_postgres psql -U postgres

#utils
install-req:
	pip install -e ""

install-local:
	pip install -e ".[dev]"