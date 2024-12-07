import json
from pathlib import Path

import pytest


def path():
    file = Path('gendif/files/file1.json')
    n = dict(json.load(open(file)))
    return n


