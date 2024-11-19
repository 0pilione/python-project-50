from base_diff import diff


def stylish(diff, level=0):
    for key, value in diff.items():
        if type(value) == dict:
            for key1, value1 in value.items():
                if key1 == 'nested':
                    print(f'   {"    " * level}{key}: {"{"}  ')
                    level += 1
                    stylish(value1, level)
                    print(f'{"    " * level}{"}"}')
                    level -= 1
                if key1 == 'added':
                    print(f'{"    " * level + " + "}{key}: {value1}')
                if key1 == 'unupdated':
                    print(f'   {"    " * level}{key}: {value1}')
                if key1 == 'deleted':
                    print(f'{"    " * level + " - "}{key}: {value1}')
                if key1 == 'changed':
                    print(f'{"    " * level + " - "}{key}: {value1[0]}\n{"    " * level + " + "}{key}: {value1[1]}')
                if type(value1) == dict: