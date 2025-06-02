.PHONY: setup \
        lint \
        mypy \
        test \
        db-current \
        db-downgrade \
        db-history \
        db-revision \
        db-show \
        db-upgrade \
        db-seed \
        run \
        help

# Detect Git Bash on Windows
IS_GIT_BASH := $(shell uname -s | grep -i "mingw" > /dev/null && echo 1 || echo 0)

ifeq ($(OS),Windows_NT)
    ifeq ($(IS_GIT_BASH),1)
        ACTIVATE=source venv/Scripts/activate
    else
        ACTIVATE=. venv\Scripts\activate
    endif
    PIP=venv/Scripts/pip.exe
    PYTHON=venv/Scripts/python.exe
    POETRY=venv/Scripts/poetry.exe
    ALEMBIC=venv/Scripts/alembic.exe
else
    ACTIVATE=. venv/bin/activate
    PIP=venv/bin/pip
    PYTHON=venv/bin/python
    POETRY=venv/bin/poetry
    ALEMBIC=venv/bin/alembic
endif

venv:  ## Create virtual environment
	python -m venv venv
	export POETRY_VIRTUALENVS_PATH=./venv

setup: venv  ## Project setup
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install poetry
	$(POETRY) install

lint:  ## Run linter
	$(ACTIVATE) && ruff format --config ./pyproject.toml . && ruff check --fix --config ./pyproject.toml .

mypy:  ## Run mypy
	$(ACTIVATE) && mypy ./

test:  ## Run tests
	$(POETRY) run pytest $(filter-out $@,$(MAKECMDGOALS)) -s

db-upgrade:  ## Apply migrations
	$(ALEMBIC) upgrade head

db-current:  ## Show current migration
	$(ALEMBIC) current

db-revision:  ## Create new db revision
	$(ALEMBIC) revision --autogenerate -m "$(filter-out $@,$(MAKECMDGOALS))"

db-show:  ## Show head migration
	$(ALEMBIC) show head

db-history:  ## Show migration history
	$(ALEMBIC) history

db-downgrade:  ## Downgrade by one migration
	$(ALEMBIC) downgrade -1

db-seed: ## Seeding database
	$(PYTHON) seed.py

run:  ## Run main.py
	$(PYTHON) main.py

help:  ## Display help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
