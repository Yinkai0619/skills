#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/7 下午2:38
'''


def inc1():
    for x in range(10):
        yield x

def inc2():
    yield from range(10)


def counter(n):
    yield from range(n)

def inc3(n):
    yield from counter(n)

n = inc3(10)
# n = counter(10)

for i in n:
    print(i)