import pytest
import json


def path1():
    n = dict(json.load(open('/home/kotyabrina/python-project-50/gendif/files/file2.json')))
    return n
