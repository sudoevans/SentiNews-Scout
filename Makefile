# Variables
PYTHON := python3
PIP := pip3
FLASK_APP := app.py

# Virtual environment variables
VENV := venv
VENV_ACTIVATE := $(VENV)/bin/activate

# Dependencies
REQUIREMENTS := requirements.txt

# Targets
.PHONY: help install run clean

help:
	@echo "Available targets:"
	@echo "  install    Install project dependencies"
	@echo "  run        Run the Flask app"
	@echo "  clean      Clean up the virtual environment"

install: $(VENV_ACTIVATE) $(REQUIREMENTS)
	$(VENV_ACTIVATE) && $(PIP) install -r $(REQUIREMENTS)

$(VENV_ACTIVATE): $(VENV)
	$(PYTHON) -m venv $(VENV)

run: install
	$(VENV_ACTIVATE) && $(FLASK_APP) run

clean:
	rm -rf $(VENV)

$(VENV):
	$(PYTHON) -m venv $(VENV)