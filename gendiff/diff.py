from gendiff.builder import diff
from gendiff.formaters import select_formater
from gendiff.parse import parse_file


def generate_diff(dict1, dict2, format_name='stylish'):
    '''generates a diff with two prepared files and the selected format.'''
    file1 = parse_file(dict1)
    file2 = parse_file(dict2)
    dif = diff(file1, file2)
    formater = select_formater(format_name)
    return formater(dif)
