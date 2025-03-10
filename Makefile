PYTHON_VERSION := $(shell cat .python-version | cut -d '/' -f1)
VENV_NAME := $(shell cat .python-version | cut -d '/' -f3)

venv =  pyenv install -s $(PYTHON_VERSION) && \
				pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME) || true && \
				source $(shell pyenv root)/versions/$(VENV_NAME)/bin/activate && \
				$(1)

ifeq (, $(shell which pyenv))
	venv = $(1)
endif

.PHONY: install
install:
	@echo "Installing python packages..."
	$(call venv, pip install -r requirements.txt)

.PHONY: run
run:
	@echo "Running the API server..."
	$(call venv, python app.py)

.PHONY: run-dev
run-dev:
	@echo "Running the API server in development mode with hot reload..."
	FLASK_ENV=development $(call venv, python app.py)
