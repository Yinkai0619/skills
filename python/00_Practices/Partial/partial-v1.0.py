#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/28 上午11:11
'''

from functools import partial

def add(x: int, y:int) ->int:
    return x + y

newadd = partial(add, y=5)
print(newadd(4))

newadd = partial(add, x=4, y=5)
print(newadd())

