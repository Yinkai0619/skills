#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/7 下午2:26
'''


# coroutine

def g1():
    for i in range(5):
        yield i


def g2():
    for i in 'abcde':
        yield i


gen1 = g1()
gen2 = g2()

for i in range(5):
    print(next(gen1))
    print(next(gen2))
