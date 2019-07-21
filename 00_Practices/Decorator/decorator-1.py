#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/21 上午11:14
'''


def sub(x, y):
    return x - y

def a(x, y, *args, m, n, **kwargs):
    pass


def logger1(fn, *args, **kwargs):
    print("Call function {}. x = {}, y = {}\n".format(fn.__name__, args[0], args[1]))
    ret = fn(*args, **kwargs)
    return ret

def add(x, y):
    return x + y

def logger2(fn):
    print(id(add), id(fn))
    def inner(*args, **kwargs):
        print("Call function {}. x = {}, y = {}\n".format(fn.__name__, *args))
        ret = fn(*args, **kwargs)
        return ret
    return inner


# print('Result = {}'.format(logger(add, 5, 4)))
# print('Result = {}'.format(logger(sub, 5, 4)))
# print('Result = {}'.format(logger(a, 5, 4, 3, m=2, n=1, k=0)))

add = logger2(add)
ret = add(5,4)
print('Result = {}'.format(ret))
# print('Result = {}'.format(logger2(add)(5,4)))
