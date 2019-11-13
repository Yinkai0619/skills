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
        yield {'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))), 'value': random.randint(1, 100)}
        time.sleep(seconds)

s = source()

# items = [next(s) for _ in range(3)]
# items = next(s)
# print(items)

def avg_handler(iterable):
    return sum(map(lambda item: item['value'], iterable)) / len(iterable)

# ret = avg_handler(items)
# print('{:.2f}'.format(ret))

def window(iterator, handler, width:int, interval:int):
    buffer = list()
    current = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    # start = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    start = current
    delta = datetime.timedelta(seconds = width - interval)
    while True:
        data = next(iterator)
        if data:
            buffer.append(data)
            current = data['datetime']
        print(current, start)

        if (current - start).total_seconds() > interval:
            print('='*60)
            print('Average: {:.2f}'.format(handler(buffer)))
            start = current

        # 清除过期数据
        # print('length of buffer: ', len(buffer))
        buffer = [x for x in buffer if x['datetime'] > current - delta]

window(s, avg_handler, 10, 5)