import json


def formater_json(diff):
    result = ''
    for n in diff:
        result += json.dumps(n, indent=4)
    return result