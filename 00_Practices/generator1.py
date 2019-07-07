#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/7 下午12:30
'''

def inc():
    def counter():
        i = 0
        while True:
            i += 1
            yield i

    c = counter()

    # def _inc():
    #     return next(c)
    #
    # return _inc

    return lambda : next(c)

g = inc()
print(g())
print(g())
print(g())
