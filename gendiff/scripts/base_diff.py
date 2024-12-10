def diff(d1, d2):
    keys1 = d1.keys()
    keys2 = d2.keys()
    unique_keys = set()
    unique_keys.update(keys1)
    unique_keys.update(keys2)
    all_keys = list(unique_keys)
    all_keys.sort()
    result = []
    for key in all_keys:
        if key in keys1 and key in keys2:
               
            if d1[key] == d2[key]:
                result.append({'key': key, 'value': str(d1[key]).lower(), 'status': 'unupdated'})
            elif type(d1[key]) == dict and type(d2[key]) == dict:
                result.append({'key': key, 'status': 'nested', 'value': diff(d1[key], d2[key])})
            else:
                result.append({'key': key, 'status': 'changed', 'old_value': str(d1[key]).lower, 'new_value': str(d2[key]).lower()})
                  
        elif key in keys2:
            result.append({'key': key, 'value': str(d2[key]).lower(), 'status': 'added'})
        else:
            result.append({'key': key, 'value': str(d1[key]).lower(), 'status': 'deleted'})
    return result
