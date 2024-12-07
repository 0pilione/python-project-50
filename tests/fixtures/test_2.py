import json

import pytest


def path1():
    n = dict(json.load(open('gendif/files/file2.json')))
    return n
