from pathlib import Path

import pytest
import yaml


def path():
    file = Path('tests/fixtures/nested_file1.yml')
    return file

def faled_path():
    file = Path('tests/fixtures/nested_file1.jpg')
    return file