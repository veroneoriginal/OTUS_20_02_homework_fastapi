# Запустить линтер
lint:
	pylint $(shell git ls-files '*.py' | grep -v 'migrations/')

# Запустить всё в Docker
up_docker:
	@docker compose -f docker-compose.yaml up --build

# docker compose down