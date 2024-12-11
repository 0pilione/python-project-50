def plain(diff, path=''):
    r = []
    for n in diff:
        name = f'{path}{n["key"]}.'
        if n['status'] == 'added':
            r.append(f"Property '{name[:-1]}' was added with value: {plain_2(n['value'])}")  # noqa: E501
        elif n['status'] == 'deleted':
            r.append(f"Property '{name[:-1]}' was removed")
        elif n['status'] == 'changed':
            r.append(f"Property '{name[:-1]}' was updated. From {plain_2(n['old_value'])} to {plain_2(n['new_value'])}")  # noqa: E501
        elif n['status'] == 'nested':
            r.append(f'{plain(n["value"], path=name)}')
    b = '\n'.join(r)
    return b


def plain_2(node):
    elif isinstance(node, str):
        return f"'{node}'"
    elif isinstance(node, dict) or isinstance(node, list):
        return "[complex value]"
    elif isinstance(node, bool):
        return str(node).lower()
    elif node is None:
        return 'null'
    else:
        return node
