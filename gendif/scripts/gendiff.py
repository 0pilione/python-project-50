import argparse
from  gendif.files.twofiles import generate_diff
import json

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
   
m = parser.add_argument('first_file')
n = parser.add_argument('second_file')
parser.add_argument('--format', '-f', help='set format of output')

args = parser.parse_args()

m = args.first_file
n = args.second_file

g = dict(json.load(open(m)))
d = dict(json.load(open(n)))


def main():
   return  generate_diff(g, d)


if __name__ == '__main__':
    main()
