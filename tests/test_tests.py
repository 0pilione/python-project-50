from gendiff import generate_diff

from tests.fixtures.files.test_7_nested import path
from tests.fixtures.files.test_8_nested import path2


def test1():
    result = generate_diff(path(), path2())
    file = open('tests/fixtures/nested_yml_result.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result


def test2():
    result = generate_diff(path(), path2(), 'plain')
    file = open('tests/fixtures/nested_yml_result_plain.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result


def test3():
    result = generate_diff(path(), path2(), 'formater_json')
    file = open('tests/fixtures/nested_yml_result_json.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result


def test4():
    result = generate_diff(path(), path2(), 'formater_json')
    file = open('tests/fixtures/result_flat.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result


def test5():
    result = generate_diff(path(), path2(), 'plain')
    file = open('tests/fixtures/flat_json_result.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result


def test6():
    result = generate_diff(path(), path2())
    file = open('tests/fixtures/uncorrect.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result
