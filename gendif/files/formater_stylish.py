def stylish(diff, level=0):
    result = '{\n'
    for n in diff:
        if n['status'] == 'added':
            result += f'{"    " * level + " + "}{n["key"]}: {n["value"]}\n'
         
        if n['status'] == 'unupdated':
            
            result += f'   {"    " * level}{n["key"]}: {n["value"]}\n'
        if n['status'] == 'deleted':
           
            result += f'{"    " * level + " - "}{n["key"]}: {n["value"]}\n'
        if n['status'] == 'changed':
            
           
            result += f'''{"    " * level + " - "}{n["key"]}: {n["old_value"]}\n
            {"    " * level + " + "}{n["key"]}: {n["new_value"]}\n'''
        if n['status'] == 'nested':
            
            result += f'   {"    " * level}{n["key"]}: {"{"}\n'
            level += 1
            stylish(n['value'], level)
            
            result += f'{"    " * level}{"}"}\n'
            level -= 1
    result += '\n}'
    return result