from gendiff.formatters.formater_json import formater_json
from gendiff.formatters.formater_plain import plain
from gendiff.formatters.formater_stylish import stylish


def diff_formaters(diff, format_name):
    if format_name == 'stylish':
        return stylish(diff)
    elif format_name == 'plain':
        return plain(diff)
    elif format_name == 'json':
        return formater_json(diff)
