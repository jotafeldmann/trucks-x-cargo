ARGS := --cargos-csv=./input/cargo.csv --trucks-csv=./input/trucks.csv
DOCKER_APP_NAME := trucksxcargo
DOCKER_COMMAND := make docker/run
PYTHON_RUN := python main.py $(ARGS)
PYTHON_RUN_DEBUG := $(PYTHON_RUN) --debug on

.PHONY: dev
dev:
	$(PYTHON_RUN_DEBUG)

csv:
	$(PYTHON_RUN) > routes.csv

dev/watch:
	rerun --interactive --verbose "make tests; make lint"

docker/run:
	docker run -t --name $(DOCKER_APP_NAME) --rm $(DOCKER_APP_NAME) bash -c make dev

docker/build:
	docker build --force-rm  -t $(DOCKER_APP_NAME) .

env:
	pipenv shell

env/exit:
	echo "Type exit"

.PHONY: install
install:
	pipenv install --system --dev --skip-lock

lint:
	flake8 .

lint/fix:
	autopep8 --global-config .flake8 --in-place --aggressive --aggressive --recursive .

run:
	$(PYTHON_RUN)

run/maxcargo:
	$(PYTHON_RUN_DEBUG) --max-cargo 2

run/remote:
	$(PYTHON_RUN_DEBUG) --remote google

run/kdtree:
	$(PYTHON_RUN_DEBUG) --algorithm kdtree

.PHONY: tests
tests:
	python -m pytest