from pathlib import Path

import pytest
import yaml


def path2():
    file = Path('tests/fixtures/nested_file2.yml')
    m = dict(yaml.safe_load(open(file)))
    return m

def faled_path_1():
    file = Path('tests/fixtures/nested_file2.jpg')
    return file