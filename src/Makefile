RUN_PYTHON := python main.py
RUN_PYTHON_DEBUG := $(RUN_PYTHON) --debug on

env:
	pipenv shell

env/exit:
	echo "Type exit"

.phony: run
run:
	$(RUN_PYTHON_DEBUG)

run/remote:
	$(RUN_PYTHON_DEBUG) --remote google

run/kdtree:
	$(RUN_PYTHON_DEBUG) --algorithm kdtree