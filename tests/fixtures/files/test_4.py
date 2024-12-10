import pytest
import yaml


def path1():
    n = dict(yaml.safe_load(open('tests/fixtures/file4.yml')))
    return n