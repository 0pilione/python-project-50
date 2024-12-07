import json
from pathlib import Path

import pytest


def path():
    file = Path('gendif/files/flat_file1.json')
    n = dict(json.load(open(file)))
    return n