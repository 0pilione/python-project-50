from gendif.files.twofiles import generate_diff
from tests.fixtures.test_1 import path
from tests.fixtures.test_2 import path1


def test1():
    res = generate_diff(path(), path1())
    b = open('tests/ress.txt')
    for lines in b:
        j = []
        if lines in b:
            u = j.append(lines)
            o = ' '.join(u)
            assert res == o

