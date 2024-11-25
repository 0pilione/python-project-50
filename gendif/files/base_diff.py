def diff(d1, d2):
    keys1 = d1.keys()
    keys2 = d2.keys()
    unique_keys = set()
    unique_keys.update(keys1)
    unique_keys.update(keys2)
    all_keys = list(unique_keys)
    all_keys.sort()
    b = []
    for key in all_keys:
        for key in all_keys:
            if type(key) == dict:
                if key in keys1 and key in keys2:
                    if d1[key] == d2[key]:
                        b.append({'key': key, 'status': 'unupdated', 'value':d1[key]})
                        if d1[key] != d2[key]:
                            b.append({'key': key, 'status': 'changed', 'old_value': d1[key], 'new_value': d2[key]})
                            if type(d1[key]) == dict and type(d2[key]) == dict:  
                                b.append({'key': key, 'status': 'nested', 'value': diff(d1[key], d2[key])})
                        
            if key in keys1 and key not in keys2:   
                b.append({'key': key, 'status': 'deleted', 'value': d1[key]})

            if key not in keys1 and key in keys2:   
                b.append({'key': key, 'status': 'added', 'value': d2[key]})
    return b