import argparse
import json
from gendiff import generate_diff
from gendiff.parse import parserr

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
   
first = parser.add_argument('first_file')
second = parser.add_argument('second_file')
formater = parser.add_argument('--format', '-f', help='set format of output', default="stylish")

args = parser.parse_args()

first = args.first_file
second = args.second_file
formater = args.format


def main(): 
      return generate_diff(first, second, formater)


if __name__ == '__main__':
    main()
