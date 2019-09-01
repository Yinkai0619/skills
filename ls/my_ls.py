#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/9/1 上午10:34
'''

import argparse
from pathlib import Path
import stat

parser = argparse.ArgumentParser(
    prog='ls',
    description='List information about the FILEs (the current directory by default).',
    add_help=True
)
parser.add_argument('path', nargs='?', default='.',
                    help='file path')
parser.add_argument('-l', dest='list', action='store_true',
                    help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true',
                    help='do not ignore entries starting with .')

args = parser.parse_args(('/tmp', '-l'))  # '/tmp'.split()
# parser.print_help()
print('-'*80)
# print(args)
# print(args.all, args.list, args.path)

def _get_file_type(p: Path):
    if p.is_dir():
        return 'd'
    elif p.is_block_device():
        return 'b'
    elif p.is_char_device():
        return 'c'
    elif p.is_fifo():
        return 'p'
    elif p.is_socket():
        return 's'
    elif p.is_symlink():
        return 'l'
    else:
        return '-'

def _get_mode_str1(mode: int):
    mode_str = 'rwx' * 3
    mstr = ''
    mode = mode & 0o777

    for i, c in enumerate(bin(mode)[-9:]):
        if c:
            mstr += mode_str[i]
        else:
            mstr += '-'
    return mstr


def _get_mode_str2(mode: int):  # 位移
    mode_str = 'rwx' * 3
    mstr = ''

    for i in range(8, -1, -1):
        mstr += mode_str[8-i] if mode >> i & 1 else '-'
    return mstr



def list_dir(p: str, detail=False):
    path = Path(p)

    for file in path.iterdir():
        if detail:  # -rw-rw-r-- 1 yinkai yinkai  12 8月  17 23:04 f11.txt
            st = file.stat()
            # print(st)   # os.stat_result(st_mode=17407, st_ino=1206151, st_dev=28, st_nlink=1, st_uid=0, st_gid=0, st_size=4, st_atime=1567344808, st_mtime=1567344809, st_ctime=1567344809)
            # mode = _get_mode_str2(st.st_mode)
            mode = stat.filemode(st.st_mode)
            # t = _get_file_type(file)
            # print(t+mode, file)
            print(mode, file)
        else:
            print(file.name)

if args.list:
    list_dir(args.path, detail=True)
else:
    list_dir(args.path)
