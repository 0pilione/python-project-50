from gendiff.formatters.__init__ import diff_formaters
from gendiff.base_diff import diff
from gendiff.parse import parserr

def generate_diff(dict1, dict2, format_name='stylish'):
    file1 = parserr(dict1)
    file2 = parserr(dict2)
    dif = diff(file1, file2)
    return diff_formaters(dif, format_name)
