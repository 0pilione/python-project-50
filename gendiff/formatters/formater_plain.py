def plain(diff, path=''):
    result = []
    for node in diff:
        name = f'{path}{node["key"]}.'
        if node['status'] == 'added':
            result.append(f"Property '{name[:-1]}' was added with value: {plain_2(node['value'])}")  # noqa: E501
        elif node['status'] == 'deleted':
            result.append(f"Property '{name[:-1]}' was removed")
        elif node['status'] == 'changed':
            result.append(f"Property '{name[:-1]}' was updated. From {plain_2(node['old_value'])} to {plain_2(node['new_value'])}")  # noqa: E501
        elif node['status'] == 'nested':
            result.append(f'{plain(node["value"], path=name)}')
    final_result = '\n'.join(result)
    return final_result


def plain_2(node):
    if isinstance(node, str):
        return f"'{node}'"
    elif isinstance(node, dict) or isinstance(node, list):
        return "[complex value]"
    elif isinstance(node, bool):
        return str(node).lower()
    elif node is None:
        return 'null'
    else:
        return node
