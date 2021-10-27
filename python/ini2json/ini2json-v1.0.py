#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/27 16:32
'''


def ini2json(src):
    '''
    将ini格式文件转换成json格式文件

    :param src:
    :return:
    '''
    from configparser import ConfigParser
    from pathlib import Path
    import json

    if type(src) != 'pathlib.PosixPath':
        src = Path(src)

    target_file = src.with_suffix('.json')

    if src.exists() and src.suffix == '.ini':
        temp = dict()

        ini_file = ConfigParser()
        ini_file.read(src, encoding='utf-8')
        for section in ini_file.sections():
            temp[section] = dict(ini_file.items(section))

        with open(target_file, 'w', encoding='utf-8') as tf:
            json.dump(temp, tf)
    else:
        return '{} is an invalid ini file.'.format(str(src))


filename = 'my.ini'
ini2json(filename)
