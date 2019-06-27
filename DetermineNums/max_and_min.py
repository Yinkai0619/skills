#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/6/27 下午9:57
'''

# 编写一个函数，能够至少接收2个参数，返回最大值和最小值

def mm(x, y, *args):

    # if x > y:
    #     max = x
    #     min = y
    # else:
    #     max = y
    #     min = x
    #
    # for i in args:
    #     if i > max: max = i
    #     if i < min: min = i
    # return max, min
    return max(x, y, *args), min(x, y, *args)


print(*mm(*range(10)))