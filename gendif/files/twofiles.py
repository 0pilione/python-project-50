import json

def generate_diff(dict1, dict2):
   for key, value in dict1.items(): 
       if key in dict2 and key in dict1: 
            if dict2[key] == dict1[key]:
                y = []
                x = '   ' + key + ': ' + str(value) + '\n'
                y.append(x)
            else: 
                l = ' - ' + key + ': ' + str(value) + '\n' + '  + ' + key + ': ' + str(dict2[key]) + '\n'
                y.append(l)
       else: 
            c = ' - ' + key + ': ' + str(value) + '\n'
            y.append(c)
   for key, value in dict2.items(): 
        if key in dict1 and key in dict2 == dict1[key]:
            gg = ' + ' + str(dict1[key]) + ': ' + str(value) + '\n'
            y.append(gg)
        if key in dict2 and key not in dict1:
           dd = ' + ' + key + ': ' + str(value) + '\n'
           y.append(dd)
           hh = ' '.join(y)
           return hh