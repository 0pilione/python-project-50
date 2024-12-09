def stylish(diff, level=0):
    r = []
    for n in diff:
        if n['status'] == 'added':
           r.append(f'\n{"    " * level + "  + "}{n["key"]}: {stylish_2(n["value"], level)}')
        if n['status'] == 'unupdated':
            r.append(f'\n{"    " * level + "   "}{n["key"]}: {stylish_2(n["value"], level)}')
        if n['status'] == 'deleted':
            r.append(f'\n{"    " * level + "  - "}{n["key"]}: {stylish_2(n["value"], level)}')
        if n['status'] == 'changed':
            r.append(f'\n{"    " * level + "  - "}{n["key"]}: {stylish_2(n["old_value"], level)}')
            r.append(f'\n{"    " * level + "  + "}{n["key"]}: {stylish_2(n["new_value"], level)}')
        if n['status'] == 'nested':
            level += 1
            r.append(f'\n{"    " * level}{n["key"]}:')
            r.append(f'{stylish(n["value"], level)}')
            level -= 1
    r.append(f'\n{"    " * level}{"}"}')
    b = ' '.join(r)
    level -= 1
    return '{' + b
    

def stylish_2(node, level):
    result = ''
    if type(node) == list:
        level += 1
        m = stylish(node, level)
        level -= 1
        return  m
    if type(node) == dict:
        level +=1
        for key, value in node.items():
            n = stylish_2(value, level)
            result += f'\n    {"    " * level}{key}: {n}'
        return '{' + result + '\n' + '    ' * level + '}'
    else:
        return node
