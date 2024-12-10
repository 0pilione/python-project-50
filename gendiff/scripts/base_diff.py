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
                result.append({'key': key, 'value': d1[key]), 'status': 'unupdated'})
            elif type(d1[key]) == dict and type(d2[key]) == dict:
                result.append({'key': key, 'status': 'nested', 'value': diff(d1[key], d2[key])})
            else:
                result.append({'key': key, 'status': 'changed', 'old_value': d1[key]), 'new_value': d2[key])})
                  
        elif key in keys2:
            result.append({'key': key, 'value': d2[key], 'status': 'added'})
        else:
            result.append({'key': key, 'value': d1[key]), 'status': 'deleted'})
    return result
