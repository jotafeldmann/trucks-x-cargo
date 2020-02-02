LINT_COMMAND := flake8 .
RUN_PYTHON := python main.py
RUN_PYTHON_DEBUG := $(RUN_PYTHON) --debug on
TESTS_COMMAND := python -m pytest

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

lint:
	$(LINT_COMMAND)

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
	$(TESTS_COMMAND)