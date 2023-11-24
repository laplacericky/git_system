#!/usr/bin/env python3
import argparse,sys
import subprocess
from lib_io import limited_lines

def ls_tree():
    return subprocess.run(['git', 'ls-tree', '--full-tree', '--name-only', '-r', 'HEAD'], stdout = subprocess.PIPE, text = True, check = True).stdout.splitlines()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices = ['ls'] )
    parser.add_argument('target', nargs='*')
    parser.add_argument('-n', '--head', type=int, default = 10)
    parser.add_argument('-a','--all',action='store_true')
    args = parser.parse_args()

    match args.mode:
        case 'ls':
            assert not args.target

    match args.mode:
        case 'ls':
            result = ls_tree()

    match args.mode:
        case 'ls':
            start = 0
            end = args.head
            step = 1

    if args.all:
        for x in result:
            print(x)
    else:
        print(limited_lines(result, start, end, step, more_info = True))


if __name__ == '__main__':
    assert sys.version_info[0] >= 3 and sys.version_info[1] >= 11
    main()
