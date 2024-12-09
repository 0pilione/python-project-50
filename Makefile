install:
	poetry install

gendiff:
	poetry run diff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

check:
	make lint
	pip install pytest pytest-cov
	pytest tests/test_test.py --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
