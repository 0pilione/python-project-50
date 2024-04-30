import pytest
import json

def path():
    m = dict(json.load(open('/home/kotyabrina/python-project-50/gendif/files/file1.json')))
    return m


