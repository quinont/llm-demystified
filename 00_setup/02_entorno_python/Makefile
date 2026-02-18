VENV = venv
PYTHON_VERSION ?= python3
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: install lint test format run clean

install:
	$(PYTHON_VERSION) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

active:
	@echo por favor, ejecute:
	@echo source $(VENV)/bin/activate

lint:
	$(VENV)/bin/flake8 src  --max-line-length 90

format:
	$(PYTHON) -m black .

clean:
	rm -rf __pycache__ .pytest_cache/
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -f report.xml .coverage coverage.xml
