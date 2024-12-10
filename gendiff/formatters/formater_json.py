import json


def formater_json(diff):
    for n in diff:
        return json.dumps(n, indent=4)