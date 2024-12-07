from gendif.scripts.twofiles import generate_diff
from tests.fixtures.test_7_nested import faled_path, path
from tests.fixtures.test_8_nested import faled_path_1, path2


def test1():
    result = generate_diff(path(), path2())
    file = open('gendif/files/nested_yml_result.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result

def test2():
    result = generate_diff(path(), path2(), 'plain')
    file = open('gendif/files/nested_yml_result_plain.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result
            
def test3():
    result = generate_diff(path(), path2(), 'formater_json')
    file = open('gendif/files/nested_yml_result_json.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result
            
def test4():
    result = generate_diff(path(), path2(), 'formater_json')
    file = open('gendif/files/result_flat.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result
            
def test5():
    result = generate_diff(path(), path2(), 'plain')
    file = open('gendif/files/flat_json_result.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result
            
def test6():
    result = generate_diff(path(), path2())
    file = open('gendif/files/uncorrect.txt')
    for lines in file:
        lst = []
        if lines in file:
            medium_result = lst.append(lines)
            expected_result = ' '.join(medium_result)
            assert result == expected_result