from gendif.formatters.__init__ import diff_formaters
from gendif.scripts.base_diff import diff


def generate_diff(dict1, dict2, format_name='stylish'):
    dif = diff(dict1, dict2)
    return diff_formaters(dif, format_name)

