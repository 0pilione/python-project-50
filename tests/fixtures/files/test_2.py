import json


def path1():
    n = dict(json.load(open('tests/fixtures/file2.json')))
    return n
