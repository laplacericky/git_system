#!/usr/bin/env python3
import argparse,sys
import subprocess
from lib_io import limited_lines

def ls_all():
    r = subprocess.run(['git','log','--all','--pretty=format:','--name-status'], stdout = subprocess.PIPE, text = True, check = True).stdout.splitlines()
    r = [ x for x in r if x != '' and x.split()[0] != 'M']
    deleted_files = [ x.split()[1] for x in r if x.split()[0] == 'D']
    return [ x for x in r if not (x.split()[0] == 'A' and x.split()[1] in deleted_files)]

def ls_tree():
    return subprocess.run(['git', 'ls-tree', '--full-tree', '-r', '--format=%(objectmode) %(objecttype) %x09%(path)', 'HEAD'], stdout = subprocess.PIPE, text = True, check = True).stdout.splitlines()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices = ['ls','lsall'] )
    parser.add_argument('target', nargs='*')
    parser.add_argument('-n', '--head', type=int, default = 10)
    parser.add_argument('-a','--all',action='store_true')
    args = parser.parse_args()

    match args.mode:
        case 'ls':
            assert not args.target
            worker_func = ls_tree
        case 'lsall':
            assert not args.target
            worker_func = ls_all

    result = worker_func()

    if args.all:
        for x in result:
            print(x)
    else:
        start = 0
        end = args.head
        step = 1
        print(limited_lines(result, start, end, step, more_info = True))


if __name__ == '__main__':
    assert sys.version_info[0] >= 3 and sys.version_info[1] >= 11
    main()
