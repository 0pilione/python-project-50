def diff(d1, d2):
    if type(d1) == dict and type(d2) == dict:
        keys1 = d1.keys()
        keys2 = d2.keys()
        unique_keys = set()
        unique_keys.update(keys1)
        unique_keys.update(keys2)
        all_keys = list(unique_keys)
        all_keys.sort()
        d = {}
        b = []
        for key in all_keys:
            if key in keys1 and key in keys2:
               
               if d1[key] == d2[key] and type(d1[key]) != dict:
                   b.append({'key': key, 'value': d1[key], 'status': 'unupdated'})
               if d1[key] == d2[key] and type(d1[key]) == dict:
                   b.append({'key': key, 'value': diff(d1[key], d1[key]), 'status': 'unupdated'})
                   
               if d1[key] != d2[key]:
                  if type(d1[key]) == dict and type(d2[key]) == dict:
                      b.append({'key': key, 'status': 'nested', 'value': diff(d1[key], d2[key])})
                  else:
                      b.append({'key': key, 'status': 'changed', 'value': d2[key], 'old_value': d1[key], 'new_value': d2[key]})
                  
            if key not in keys1 and key in keys2 and type(d2[key]) != dict:
               b.append({'key': key, 'value': d2[key], 'status': 'added'})
            if key not in keys1 and key in keys2 and type(d2[key]) == dict:
               b.append({'key': key, 'value': diff(d2[key], d2[key]), 'status': 'added'})
               
            if key in keys1 and key not in keys2 and type(d1[key]) != dict:
              b.append({'key': key, 'value': d1[key], 'status': 'deleted'})
            if key in keys1 and key not in keys2 and type(d1[key]) == dict:
               b.append({'key': key, 'value': diff(d1[key], d1[key]), 'status': 'deleted'})
        return b