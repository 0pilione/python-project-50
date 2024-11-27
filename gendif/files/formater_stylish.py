def stylish(diff, level=0):
    r = []
    r.append(f'{"{"}')
    for n in diff:
        if n['status'] == 'added':
           r.append(f'{"    " * level + "+ "}{n["key"]}: {stylish_2(n["value"], level)}')
        if n['status'] == 'unupdated':
            r.append(f'{"    " * level}{n["key"]}: {stylish_2(n["value"], level)}')
        if n['status'] == 'deleted':
            r.append(f'{"    " * level + "- "}{n["key"]}: {stylish_2(n["value"], level)}')
        if n['status'] == 'changed':
            r.append(f'{"    " * level + "- "}{n["key"]}: {stylish_2(n["old_value"], level)}')
            r.append(f'{"    " * level + "+ "}{n["key"]}: {stylish_2(n["new_value"], level)}')
        if n['status'] == 'nested':
            r.append(f'{"    " * level}{n["key"]}:')
            level += 1
            r.append(f'{"    " * level}{stylish(v, level)}')
            level -= 1

    r.append(f'{"    " * level}{"}"}')
    b = '\n'.join(r)
    return b

def stylish_2(node, level):
    if type(node) == list:
        level += 1
        m = stylish(node, level)
        level -= 1
        return m
    if type(node) == dict:
        level +=1
        for key, value in node.items():
            return f'{"{"}\n    {"    " * level}{key}: {value}\n{"    " * level}{"}"}'
    else:
        return node