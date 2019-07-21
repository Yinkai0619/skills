#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/21 上午11:14
'''


def logger(fn):
    def wrapper(*args, **kwargs):
        print("Call function: {}. \nThe args: x = {}, y = {}\n".format(fn.__name__, *args))
        ret = fn(*args, **kwargs)
        return ret
    return wrapper

@logger # 装饰器语法，把装饰器下边的标识符提上来，作为该装饰器函数的参数，并且将返回值重新覆盖给该标识符
def sub(x, y):
    return x - y

@logger # @logger 等价于： add = logger(add) = wrapper(x, y)
def add(x, y):
    return x + y


ret1 = add(5,4) # => add = logger(add)(5, 4) => wrapper(5, 4)
ret2 = sub(5,4)
print('Result = {}'.format(ret1))
print('Result = {}'.format(ret2))
