.PHONY: help

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

install-pipenv:
	pip install Pipenv

install-dev: install-pipenv ## Install dev dependencies
	pipenv install --dev

install: install-pipenv ## Install the dependencies
	pipenv install

flake:
	flake8 .

lint: flake ## Run code lint

test: clean lint ## Run tests
	python manage.py test
