import json
from pathlib import Path


def path():
    file = Path('/testsfixtures/flat_file1.json')
    n = dict(json.load(open(file)))
    return n