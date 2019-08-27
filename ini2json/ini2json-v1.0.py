#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/27 16:32
'''
from configparser import ConfigParser

filename = 'my.ini'
# newfilename

ini_file = ConfigParser()
ini_file.read(filename, encoding='utf-8')
for section, option in ini_file.items():
    # print(type(section), section)
    # print(type(option), option)
    # for k, v in option.items():
    # print('{}-->{}:{}'.format(section, k, v))
    print(ini_file.options(section))