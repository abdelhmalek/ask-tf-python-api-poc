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
	$(call venv, uvicorn app:app --host 0.0.0.0 --port 5001)

.PHONY: run-dev
run-dev:
	@echo "Running the API server in development mode with hot reload..."
	$(call venv, uvicorn app:app --host 0.0.0.0 --port 5001 --reload)

.PHONY: test
test:
	@echo "Running tests..."
	$(call venv, python -m unittest discover -s tests)

.PHONY: functional-test
functional-test:
	@echo "Running Cucumber tests..."
	$(call venv, behave)

.PHONY: up
up:
	docker-compose up --build --remove-orphans --force-recreate

.PHONY: dup
dup:
	docker-compose up -d --build --remove-orphans --force-recreate

.PHONY: down
down:
	docker-compose down --volumes