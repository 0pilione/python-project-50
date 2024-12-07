from pathlib import Path

import pytest
import yaml


def path():
    file = Path('gendif/files/nested_file1.yml')
    m = dict(yaml.safe_load(open(file)))
    return m

def faled_path():
    file = Path('gendif/files/nested_file1.jpg')
    return file