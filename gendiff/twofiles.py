import json

m = json.load(open('//wsl.localhost/Ubuntu/home/kotyabrina/python-project-50/files/file1.json'))
n = json.load(open('//wsl.localhost/Ubuntu/home/kotyabrina/python-project-50/files/file2.json'))

g = dict(m)
d = dict(n)

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

if __name__ == '__main__':
    print(generate_diff())