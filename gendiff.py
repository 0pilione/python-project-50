import argparse
from gendif.files import twofiles

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
   
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('--format', '-f', help='set format of output')

args = parser.parse_args()

m = json.load(open('//wsl.localhost/Ubuntu/home/kotyabrina/python-project-50/files/file1.json'))
n = json.load(open('//wsl.localhost/Ubuntu/home/kotyabrina/python-project-50/files/file2.json'))

g = dict(m)
d = dict(n)

def main():
    (g, d)


if __name__ == '__main__':
    main()