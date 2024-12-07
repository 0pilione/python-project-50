import argparse
import json

import yaml
from gendif.scripts.twofiles import generate_diff

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
   
first = parser.add_argument('first_file')
second = parser.add_argument('second_file')
formater = parser.add_argument('--format', '-f', help='set format of output', default="stylish")

args = parser.parse_args()

first = args.first_file
second = args.second_file
formater = args.format

def main(): 
   if first.endswith('json') and second.endswith('json'):
      opened_first = dict(json.load(open(first)))
      opened_second = dict(json.load(open(second)))
      return  generate_diff(opened_first, opened_second, formater)
   if first.endswith('yml') and second.endswith('yml'):
      opened_first_2 = dict(yaml.safe_load(open(first)))
      opened_second_2 = dict(yaml.safe_load(open(second)))
      return  generate_diff(opened_first_2, opened_second_2, formater)
   else:
      return 'uncorrect type of files'


if __name__ == '__main__':
    main()