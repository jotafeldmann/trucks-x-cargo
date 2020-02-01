LINT_COMMAND := flake8 .
RUN_PYTHON := python main.py
RUN_PYTHON_DEBUG := $(RUN_PYTHON) --debug on
TESTS_COMMAND := python -m pytest

dev/watch:
	rerun --interactive --verbose "$(TESTS_COMMAND); $(LINT_COMMAND)"

env:
	pipenv shell

env/exit:
	echo "Type exit"

lint:
	$(LINT_COMMAND)

lint/fix:
	autopep8 --global-config .flake8 --in-place --aggressive --aggressive --recursive .

run:
	$(RUN_PYTHON_DEBUG)

run/remote:
	$(RUN_PYTHON_DEBUG) --remote google

run/kdtree:
	$(RUN_PYTHON_DEBUG) --algorithm kdtree

tests:
	$(TESTS_COMMAND)