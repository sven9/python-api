build:
	docker-compose build

up:
	docker-compose up

shell:
	docker exec -it python_api bash

down:
	docker-compose down

lint:
	pre-commit run --all-files

run-tests:
	mkdir -p ${REPORTS_DIR}/coverage
	docker exec -it -e DATABASE_URI=sqlite:///:memory: python_api pytest -s --cov=python_api --cov-report html:${REPORTS_DIR}/coverage tests/

setup-pre-commit:
	git config --bool flake8.strict true
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type commit-msg

REPORTS_DIR=./reports

quality-reports:
	mkdir -p ${REPORTS_DIR}/quality
	radon cc -a -o SCORE --md -O ${REPORTS_DIR}/quality/cyclomatic-complexity.md .
	radon mi . > ${REPORTS_DIR}/quality/maintainability-index.txt
	radon raw -s . > ${REPORTS_DIR}/quality/raw-metrics.txt
	radon hal . > ${REPORTS_DIR}/quality/halstead-complexity.txt
