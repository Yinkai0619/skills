#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/17 13:39
'''

import inspect
import functools
import time

@functools.lru_cache()
def f1(x=3):
    time.sleep(3)
    return x + 1

print(f1(x=4))
# print(f1(x=4))
print(f1(4))
# print(f1())


