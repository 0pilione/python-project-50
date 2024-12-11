from pathlib import Path


def path():
    file = Path('tests/fixtures/nested_file1.yml')
    return file


def faled_path():
    file = Path('tests/fixtures/nested_file1.jpg')
    return file