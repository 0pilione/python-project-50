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
	pip install pytest pytest-cov
	make lint
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
