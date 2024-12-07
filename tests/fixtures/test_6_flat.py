import json
from pathlib import Path

import pytest


def path2():
    file = Path('gendif/files/flat_file2.json')
    n = dict(json.load(open(file)))
    return n