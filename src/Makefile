include .env
ARGS := --cargos-csv=./input/cargo.csv --trucks-csv=./input/trucks.csv
DOCKER_APP_NAME := trucksxcargo
PYTHON_RUN := python main.py $(ARGS)
PYTHON_RUN_DEBUG := $(PYTHON_RUN) --debug on
TEST_COMMAND := python -m pytest
LINT_COMMAND := flake8 .
USE_DOCKER_VAR := USE_DOCKER
USE_DOCKER_VAR_TRUE := $(USE_DOCKER_VAR)=true
USE_DOCKER_VAR_FALSE:= $(USE_DOCKER_VAR)=false
# To use Docker:
# export USE_DOCKER=true
# or add USE_DOCKER=true from .env
# To stop:
# export -n USE_DOCKER
# or remove USE_DOCKER=true from .env

ifeq ($($(USE_DOCKER_VAR)), true)
	DOCKER_COMMAND := docker run -e "$(USE_DOCKER_VAR_FALSE)" -v $(pwd):/$(DOCKER_APP_NAME) -it --name $(DOCKER_APP_NAME) --rm $(DOCKER_APP_NAME)
else
	unexport DOCKER_COMMAND
endif

.PHONY: dev
dev:
	$(DOCKER_COMMAND) $(PYTHON_RUN_DEBUG)

csv:
	$(DOCKER_COMMAND) $(PYTHON_RUN) > routes.csv

dev/watch:
	$(DOCKER_COMMAND) rerun --interactive --verbose "$(TEST_COMMAND); $(LINT_COMMAND)"

docker/build:
	docker build --force-rm  -t $(DOCKER_APP_NAME) .

docker/on:
	echo "$(USE_DOCKER_VAR_TRUE)" > .env

docker/off:
	echo "$(USE_DOCKER_VAR_FALSE)" > .env

env:
	pipenv shell

env/exit:
	echo "Type exit"

.PHONY: install
install:
	$(DOCKER_COMMAND) pipenv install --system --dev --skip-lock

lint:
	$(DOCKER_COMMAND) $(LINT_COMMAND)

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
	$(DOCKER_COMMAND) $(TEST_COMMAND)