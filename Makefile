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
	pip install pytest
	poetry run pytest

check:
	pytest

test-coverage:
	poetry run pytest

