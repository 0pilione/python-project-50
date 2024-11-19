def s(d1, d2):
    keys1 = d1.keys()
    keys2 = d2.keys()
    unique_keys = set()
    unique_keys.update(keys1)
    unique_keys.update(keys2)
    all_keys = list(unique_keys)
    all_keys.sort()
    d = {}
    for key in all_keys:
        for key in all_keys:
            if key in keys1 and key in keys2:
                if d1[key] == d2[key]:
                    d.update({key: {'unupdated': d1[key]}})
                if d1[key] != d2[key]:
                    d.update({key: {'changed': (d1[key], d2[key])}})
                    if type(d1[key]) == dict and type(d2[key]) == dict:  
                        d.update({key: {'nested': s(d1[key], d2[key])}})
            if key in keys1 and key not in keys2:   
                d.update({key: {'deleted': d1[key]}})
            if key not in keys1 and key in keys2:   
                d.update({key: {'added': d2[key]}})

    
    return d