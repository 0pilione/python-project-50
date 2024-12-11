from pathlib import Path

import yaml


def path():
    file = Path('tests/fixtures/nested_file1.yml')
    return file


def faled_path():
    file = Path('tests/fixtures/nested_file1.jpg')
    return file