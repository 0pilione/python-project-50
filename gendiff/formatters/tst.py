import json

with open('//wsl.localhost/Ubuntu/home/kotyabrina/python-project-50/gendif/files/file1.json') as f:
    text1 = f.read()
with open('//wsl.localhost/Ubuntu/home/kotyabrina/python-project-50/gendif/files/file2.json') as k:
    text2 = k.read()


file1 = json.loads(text1)
file2 = json.loads(text2)

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
        if key in keys1 and key in keys2:
               
            if d1[key] == d2[key]:
                if type(d1[key]) != dict:
                    b.append({'key': key, 'value': d1[key], 'status': 'unupdated'})
                else:
                    b.append({'key': key, 'value': diff(d1[key], d1[key]), 'status': 'unupdated'})
                   
            else:
                if type(d1[key]) == dict and type(d2[key]) == dict:
                    b.append({'key': key, 'status': 'nested', 'value': diff(d1[key], d2[key])})
                else:
                    b.append({'key': key, 'status': 'changed', 'old_value': d1[key], 'new_value': d2[key]})
                  
        elif key not in keys1 and key in keys2:
            #if type(d2[key]) != dict:
            b.append({'key': key, 'value': d2[key], 'status': 'added'})
            #else:
                #b.append({'key': key, 'value': diff(d2[key], d2[key]), 'status': 'added'})
               
        else:
           #if type(d1[key]) != dict:
           b.append({'key': key, 'value': d1[key], 'status': 'deleted'})
           #else:
               #b.append({'key': key, 'value': diff(d1[key], d1[key]), 'status': 'deleted'})
    return b

print(diff(file1, file2))
