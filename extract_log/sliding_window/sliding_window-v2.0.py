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
from queue import Queue
import threading

# 数据生成者
def source(seconds=1):
    while True:
        yield {'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))), 'value': random.randint(1, 100)}
        time.sleep(seconds)


# 数据消费者
def avg_handler(iterable):
    '''
    计算平均值
    :param iterable:
    :return:
    '''
    return sum(map(lambda item: item['value'], iterable)) / len(iterable)


# 滑动窗口控制器
def window(q:Queue, handler, width:int, interval:int):
    buffer = list()
    current = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    # start = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    start = current
    delta = datetime.timedelta(seconds = width - interval)
    while True:
        data = q.get() #next(iterator)
        if data:
            buffer.append(data)
            current = data['datetime']
        print(current, start)

        if (current - start).total_seconds() > interval:
            print('='*60)
            print('Average: {:.2f}'.format(handler(buffer)))
            print(threading.current_thread())
            start = current

        # 清除过期数据
        # print('length of buffer: ', len(buffer))
        buffer = [x for x in buffer if x['datetime'] > current - delta]


# 注册和分发器
def dispatcher(src):
    queues = list()
    threads = list()

    def reg(handler, width, interval):
        q = Queue()
        t = threading.Thread(target=window, args=(q, handler, width, interval))

        queues.append(q)
        threads.append(t)

    def run():
        for t in threads:
            t.start()

        while True:
            data = next(src)
            for q in queues:
                q.put(data)

    return reg, run

s = source()
reg, run = dispatcher(s)
reg(avg_handler, 10, 5)
print(threading.current_thread())
run()
