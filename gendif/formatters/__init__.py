from gendif.formatters.formater_json import formater_json
from gendif.formatters.formater_plain import plain
from gendif.formatters.formater_stylish import stylish


def diff_formaters(diff, format_name):
    if format_name == 'stylish':
        return stylish(diff)
    elif format_name == 'plain':
        return plain(diff)
    elif format_name == 'formater_json':
        return formater_json(diff)