
def stylish(diff, level=0):
    r = ''
    for n in diff:
        if n['status'] == 'added':
           r += f'\n{"    " * level + "  + "}{n["key"]}: {stylish_2(n["value"], level)}'
        if n['status'] == 'unupdated':
            r += f'\n{"    " * level + "    "}{n["key"]}: {stylish_2(n["value"], level)}'
        if n['status'] == 'deleted':
            r += f'\n{"    " * level + "  - "}{n["key"]}: {stylish_2(n["value"], level)}'
        if n['status'] == 'changed':
            r += f'\n{"    " * level + "  - "}{n["key"]}: {stylish_2(n["old_value"], level)}'
            r += f'\n{"    " * level + "  + "}{n["key"]}: {stylish_2(n["new_value"], level)}'
        if n['status'] == 'nested':
            level += 1
            r += f'\n{"    " * level}{n["key"]}: '
            r += f'{stylish(n["value"], level)}'
            level -= 1
    r += f'\n{"    " * level}{"}"}'
    level -= 1
    return '{' + r
    

def stylish_2(node, level):
    result = ''
    if type(node) == list:
        level += 1
        m = stylish(node, level)
        level -= 1
        return  str(m)
    if type(node) == dict:
        level +=1
        for key, value in node.items():
            n = stylish_2(value, level)
            result += f'\n    {"    " * level}{key}: {n}'
        return '{' + result + '\n' + '    ' * level + '}'
    if isinstance(node, bool):
        return str(node).lower()
    if node is None:
        node = 'null'
        return node
    else:
        return str(node)
