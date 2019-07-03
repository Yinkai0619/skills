#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/4 下午5:12
'''

'''
随机生成100个验证码，每个验证码由6个元素构成:
1 要求使用random模块
2 验证码由字母和数字构成
3 要求验证码中的每个元素为一种颜色
提示 颜色可以用数字来表示:一般都是3个 (0, 255)之间的数字来构成的
demo:
Z (19, 157, 229)
2 (239, 10, 145)
Z (145, 142, 244)
M (231, 58, 7)
T (202, 19, 72)
F (182, 136, 237)
要求生成 png 或者jpg 格式的图片，关于如何生成图片 请搜索下python PIL生成图片
'''


def generate_verification_code(n=5):
    '''
    定义验证码生成器，生成n个验证吗
    :param n:
    :return: code
    '''
    import random
    import string

    for i in range(n):
        code = random.sample(string.ascii_lowercase, 2) + random.sample(string.ascii_uppercase, 2) + random.sample(string.digits, 2)
        random.shuffle(code)
        code = ''.join(code)
        yield code

def set_color(string):  #随机挑选一种颜色对字符进行着色，背景色使用黑色
    '''
    格式： 开头部分：\033[显示方式; 前景色; 背景色m + str + 结尾部分：\033[0m
    前景色            背景色           颜色
    ---------------------------------------
    30                40              黑色
    31                41              红色
    32                42              绿色
    33                43              黃色
    34                44              蓝色
    35                45              紫红色
    36                46              青蓝色
    37                47              白色


    显示方式           意义
    -------------------------
    0                终端默认设置
    1                高亮显示
    4                使用下划线
    5                闪烁
    7                反白显示
    8                不可见
    '''
    import random

    length = len(string)
    color_str = ''
    color_num = 38 - 31
    if length <= color_num:    #定义颜色列表，排除黑色。 当字符数量超出颜色数量时重复使用颜色
        color_id = random.sample((range(31, 38)), length)
    else:
        color_id = list(range(31, 38))
        random.shuffle(color_id)
        color_id = color_id * (length // (len(color_id) - 1))

    for i in range(length):
        color_str += "\033[0;{c};40m{s}\033[0m".format(c = color_id[i], s = string[i])
    return color_str

verification_code = generate_verification_code(100)
for code in verification_code:
    print(set_color(code))
