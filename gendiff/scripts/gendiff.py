from gendiff import generate_diff
from gendiff.parse_1 import parsearguments


args = parsearguments()
first = args.first_file
second = args.second_file
formater = args.format


def main():   
    print(generate_diff(first, second, formater))


if __name__ == '__main__':
    main()
