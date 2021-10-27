#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2021/1/17 下午9:49
'''

"""
需求：组织10个工人生产1000个杯子
"""

import logging
import time
from threading import Thread, Lock

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

cups = []
lock = Lock()


def worker(count: int):
    logging.info("I'm work for you.")
    flag = False
    while True:
        lock.acquire()      # 获取锁
        if len(cups) >= count:
            flag = True
        
        if not flag:
            time.sleep(0.001)
            cups.append(1)

        lock.release()      # 释放锁

        if flag:
            break


    logging.info("I finished. cups = {}".format(len(cups)))


for i in range(1, 11):
    Thread(name="worker-{}".format(i), target=worker, args=(1000,)).start()
