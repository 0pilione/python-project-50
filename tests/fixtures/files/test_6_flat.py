import json
from pathlib import Path


def path2():
    file = Path('tests/fixtures/flat_file2.json')
    n = dict(json.load(open(file)))
    return n