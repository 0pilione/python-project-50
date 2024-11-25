def stylish(diff, level=0):
    result = '{\n'
    if type(diff) == dict:
        if diff['child']['status'] == 'added':
            result += f'{"    " * level + " + "}{diff["child"]["key"]}: {diff["child"]["value"]}'
        if diff['child']['status'] == 'unupdated':
            result += f'   {"    " * level}{diff["child"]["key"]}: {diff["child"]["value"]}'
        if diff['child']['status'] == 'deleted':
            result += f'{"    " * level + " - "}{diff["child"]["key"]}: {diff["child"]["value"]}'
        if diff['child']['status'] == 'changed':
            result += f'''{"    " * level + " - "}{diff["child"]["key"]}: {diff["child"]["old_value"]}\n
            {"    " * level + " + "}{diff["child"]["key"]}: {diff["child"]["new_value"]}'''
        if diff['child']['status'] == 'nested':
            result += f'   {"    " * level}{diff["child"]["key"]}: {"{"}'
            level += 1
            stylish(diff['child']['value'], level)
            result += f'{"    " * level}{"}"}'
            level -= 1
    return result