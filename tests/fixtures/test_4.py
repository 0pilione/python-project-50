import pytest
import yaml


def path1():
    n = dict(yaml.safe_load(open('gendif/files/file4.yml')))
    return n