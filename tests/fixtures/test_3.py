from pathlib import Path

import pytest
import yaml


def path():
    n = Path('gendif/files/file3.yml')
    m = dict(yaml.safe_load(open(n)))
    return m