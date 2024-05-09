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

check:
	pytest
	make lint

test-coverage:
	pytest

