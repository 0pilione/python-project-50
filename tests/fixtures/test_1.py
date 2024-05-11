import pytest
import json

def path():
    m = dict(json.load(open('gendif/files/file1.json')))
    return m


