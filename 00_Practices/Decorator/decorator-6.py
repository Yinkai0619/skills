#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/21 上午11:14
'''

import datetime
import time
from functools import update_wrapper, wraps

def logger(duration):
    def _logger(fn):
        # @copy_properties(fn)
            # copy_properties(fn)(wrapper)
            # wrapper = copy_properties(fn)(wrapper) = _copy(wrapper) = wrapper
        @wraps(fn) # wrapper = wraps(fn)(wrapper)
        def wrapper(*args, **kwargs):
            '''This is wrapper function.

            '''
            # before 功能增强
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            # after 功能增强
            delta = (datetime.datetime.now() - start).total_seconds()
            print("Function {} took {}s.".format(fn.__name__, delta))
            print("So slow! ") if delta > duration else print("So fast! ")
            print("=" * 50)
            return ret
        return wrapper
    return _logger


@logger(3)  # 装饰器语法，把装饰器下边的标识符提上来，作为该装饰器函数的参数，并且将返回值重新覆盖给该标识符
def sub(x, y):
    # time.sleep(6)
    return x - y


@logger(3)  # @logger 等价于： add = logger(add) => wrapper(x, y)
    # add = logger(3)(add) = _logger(add) = wrapper(x, y)
def add(x, y):
    """This is add function.
    x:
    y:
    return:
    """
    time.sleep(5)
    return x + y


ret1 = add(5, 4)  # => add = logger(add)(5, 4) => wrapper(5, 4)
ret2 = sub(5, 4)
print('Result = {}'.format(ret1))
print('Result = {}'.format(ret2))

# print("==============")
# print(help(add))
