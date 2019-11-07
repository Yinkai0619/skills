#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/11/7 下午9:36
'''

import time
import datetime
import random

def source(seconds=1):
    while True:
        yield {'datetime:': datetime.datetime.now(), 'value': random.randint(1, 100)}
        time.sleep(seconds)

s = source()

items = [next(s) for _ in range(3)]
# items = next(s)
print(items)

def handler(iterable):
    return sum(map(lambda item: item['value'], iterable)) / len(iterable)

ret = handler(items)
print('{:.2f}'.format(ret))