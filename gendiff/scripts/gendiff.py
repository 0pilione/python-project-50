from gendiff import generate_diff
from gendiff.cli import parse_arguments


def main():
    '''generates diff from two files.'''
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
