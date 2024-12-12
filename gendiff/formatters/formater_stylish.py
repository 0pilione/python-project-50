
def stylish(diff, level=0):
    result = ''
    for node in diff:
        if node['status'] == 'added':
            result += f'\n{"    " * level + "  + "}{node["key"]}: '
            result += f'{stylish_2(node["value"], level)}'
        elif node['status'] == 'unupdated':
            result += f'\n{"    " * level + "    "}{node["key"]}: '
            result += f'{stylish_2(node["value"], level)}'
        elif node['status'] == 'deleted':
            result += f'\n{"    " * level + "  - "}{node["key"]}: '
            result += f'{stylish_2(node["value"], level)}'
        elif node['status'] == 'changed':
            result += f'\n{"    " * level + "  - "}{node["key"]}: '
            result += f'{stylish_2(node["old_value"], level)}'
            result += f'\n{"    " * level + "  + "}{node["key"]}: '
            result += f'{stylish_2(node["new_value"], level)}'
        else:
            level += 1
            result += f'\n{"    " * level}{node["key"]}: '
            result += f'{stylish(node["value"], level)}'
            level -= 1
    result += f'\n{"    " * level}{"}"}'
    level -= 1
    return '{' + result


def stylish_2(node, level):
    result = ''
    if isinstance(node, list):
        level += 1
        new_node = stylish(node, level)
        level -= 1
        return str(new_node)
    if isinstance(node, dict):
        level += 1
        for key, value in node.items():
            new_value = stylish_2(value, level)
            result += f'\n    {"    " * level}{key}: {new_value}'
        return '{' + result + '\n' + '    ' * level + '}'
    if isinstance(node, bool):
        return str(node).lower()
    if node is None:
        node = 'null'
        return node
    else:
        return node
