ARGS := --cargos-csv=./../input/cargo.csv --trucks-csv=./../input/trucks.csv
RUN_PYTHON := python main.py $(ARGS)
RUN_PYTHON_DEBUG := $(RUN_PYTHON) --debug on

csv:
	$(RUN_PYTHON) > routes.csv

dev:
	$(RUN_PYTHON_DEBUG)

dev/watch:
	rerun --interactive --verbose "make tests; make lint"

env:
	pipenv shell

env/exit:
	echo "Type exit"

install:
	pipenv install --system --dev --skip-lock

lint:
	flake8 .

lint/fix:
	autopep8 --global-config .flake8 --in-place --aggressive --aggressive --recursive .

run:
	$(RUN_PYTHON)

run/maxcargo:
	$(RUN_PYTHON_DEBUG) --max-cargo 2

run/remote:
	$(RUN_PYTHON_DEBUG) --remote google

run/kdtree:
	$(RUN_PYTHON_DEBUG) --algorithm kdtree

.PHONY: tests
tests:
	python -m pytest