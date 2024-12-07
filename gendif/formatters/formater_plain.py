def plain(diff, path=''):
    r = []
    for n in diff:
        name = f'{path}{n["key"]}.'
        if n['status'] == 'added':
           r.append(f"\nProperty '{name[:-1]}' was added with value: {plain_2(n['value'])}")
        elif n['status'] == 'deleted':
           r.append(f"\nProperty '{name[:-1]}' was removed")
        elif n['status'] == 'changed':
           r.append(f"\nProperty '{name[:-1]}' was updated. From {plain_2(n['old_value'])} to {plain_2(n['new_value'])}")
        elif n['status'] == 'nested':
           r.append(f'{plain(n["value"], path=name)}')
    b = ' '.join(r)
    return b




def plain_2(node):
    r = []
    if type(node) == list:
        return f'[complex value]'
    else:
        if type(node) == str:
            return f"'{node}'"
        if type(node) == dict:
            return f"[complex value]"
        if type(node) == bool:
            return str(node).lower()
        if node == None:
            return 'null'
        if type(node) == int:
            return str(node)
