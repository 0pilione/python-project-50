install:
	poetry install

gendif:
	poetry run diff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendif

pytest:
	pip install pytest pytest-cov
	pytest test_test.py --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html

check:
	pytest

test-coverage:
	poetry run pytest

