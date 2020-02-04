include .env
ARGS := --cargos-csv=./input/cargo.csv --trucks-csv=./input/trucks.csv
DOCKER_APP_NAME := trucksxcargo
DOCKER_COMMAND :=
INSTALL_COMMAND := pipenv run pipenv install --system --dev --skip-lock
PYTHON_RUN := python main.py $(ARGS)
PYTHON_RUN_DEBUG := $(PYTHON_RUN) --debug on
TEST_COMMAND := python -m pytest
LINT_COMMAND := flake8 .
USE_DOCKER_VAR := USE_DOCKER
USE_DOCKER_VAR_TRUE := $(USE_DOCKER_VAR)=true
USE_DOCKER_VAR_FALSE:= $(USE_DOCKER_VAR)=false
DOCKER_COMMAND := docker run --rm -it -v $(pwd):/$(DOCKER_APP_NAME) --name $(DOCKER_APP_NAME) -e "$(USE_DOCKER_VAR_FALSE)" $(DOCKER_APP_NAME)
LOCAL_COMMAND := pipenv run
# To use Docker:
# make docker/on
# export USE_DOCKER=true
# or add USE_DOCKER=true from .env
# To stop:
# make docker/off
# export -n USE_DOCKER
# or remove USE_DOCKER=true from .env

ifeq ($($(USE_DOCKER_VAR)), true)
	PLAFTORM_COMMAND := $(DOCKER_COMMAND)
	INSTALL_COMMAND := make docker/build
else
	PLAFTORM_COMMAND := $(LOCAL_COMMAND)
	INSTALL_COMMAND := $(INSTALL_COMMAND)
endif

default:
	make run

csv:
	$(PLAFTORM_COMMAND) $(PYTHON_RUN) > routes.csv

dev/watch:
	$(PLAFTORM_COMMAND) rerun --interactive --verbose "$(TEST_COMMAND); $(LINT_COMMAND)"

.PHONY: dev
dev:
	$(PLAFTORM_COMMAND) $(PYTHON_RUN_DEBUG)

docker/build:
	docker build --build-arg "WORKDIR=$(DOCKER_APP_NAME)"  --force-rm  -t $(DOCKER_APP_NAME) .

docker/on:
	echo "$(USE_DOCKER_VAR_TRUE)" > .env

docker/off:
	echo "$(USE_DOCKER_VAR_FALSE)" > .env

.PHONY: env
env: 
	pipenv shell

env/exit:
	echo "Type exit"

.PHONY: install
install:
	$(INSTALL_COMMAND)
	
lint:
	$(PLAFTORM_COMMAND) $(LINT_COMMAND)

lint/fix:
	$(PLAFTORM_COMMAND) autopep8 --global-config .flake8 --in-place --aggressive --aggressive --recursive .

run:
	$(PLAFTORM_COMMAND) $(PYTHON_RUN)

run/maxcargo:
	$(PLAFTORM_COMMAND) $(PYTHON_RUN_DEBUG) --max-cargo 2

run/remote:
	$(PLAFTORM_COMMAND) $(PYTHON_RUN_DEBUG) --remote google

run/kdtree:
	$(PLAFTORM_COMMAND) $(PYTHON_RUN_DEBUG) --algorithm kdtree

.PHONY: tests
tests:
	$(PLAFTORM_COMMAND) $(TEST_COMMAND)