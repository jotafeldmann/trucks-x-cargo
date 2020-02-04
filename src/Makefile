include .env
ARGS := --cargos-csv=./input/cargo.csv --trucks-csv=./input/trucks.csv
DOCKER_APP_NAME := trucksxcargo
PYTHON_RUN := python main.py $(ARGS)
PYTHON_RUN_DEBUG := $(PYTHON_RUN) --debug on
# To use Docker:
# export USE_DOCKER=true
# or add USE_DOCKER=true from .env
# To stop:
# export -n USE_DOCKER
# or remove USE_DOCKER=true from .env
USE_DOCKER := $(USE_DOCKER)

ifeq ($(USE_DOCKER), true)
	DOCKER_COMMAND := docker run -t --name $(DOCKER_APP_NAME) --rm $(DOCKER_APP_NAME)
endif

.PHONY: dev
dev:
	$(DOCKER_COMMAND) $(PYTHON_RUN_DEBUG)

csv:
	$(DOCKER_COMMAND) $(PYTHON_RUN) > routes.csv

dev/watch:
	$(DOCKER_COMMAND) rerun --interactive --verbose "make tests; make lint"

docker/build:
	docker build --force-rm  -t $(DOCKER_APP_NAME) .

docker/on:
	echo "USE_DOCKER=true" > .env

docker/off:
	echo "USE_DOCKER=false" > .env

env:
	pipenv shell

env/exit:
	echo "Type exit"

.PHONY: install
install:
	$(DOCKER_COMMAND) pipenv install --system --dev --skip-lock

lint:
	$(DOCKER_COMMAND) flake8 .

lint/fix:
	$(DOCKER_COMMAND) autopep8 --global-config .flake8 --in-place --aggressive --aggressive --recursive .

run:
	$(DOCKER_COMMAND) $(PYTHON_RUN)

run/maxcargo:
	$(DOCKER_COMMAND) $(PYTHON_RUN_DEBUG) --max-cargo 2

run/remote:
	$(DOCKER_COMMAND) $(PYTHON_RUN_DEBUG) --remote google

run/kdtree:
	$(DOCKER_COMMAND) $(PYTHON_RUN_DEBUG) --algorithm kdtree

.PHONY: tests
tests:
	$(DOCKER_COMMAND) python -m pytest