#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2021/2/6 下午3:05
'''

import logging
import random
import time
from threading import Event, Thread, Condition

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = Event()
        self.cond = Condition()

    def produce(self, count=10):
        for _ in range(count):
            self.data = random.randint(0, 100)
            time.sleep(1)  # 模拟生产者生产时间
            with self.cond:
                # self.cond.notify_all()
                self.cond.notify(2)

    def consume(self):
        while True:
            with self.cond:
                self.cond.wait()
                # self.event.wait(0.5)  # 模拟消费者处理时间
                data = self.data
                logging.info(data)
                # self.data = None


if __name__ == '__main__':
    d = Dispatcher()
    p = Thread(target=d.produce, name="producer", args=(5,))
    for i in range(5):
        Thread(target=d.consume, name="consumer-{}".format(i)).start()      # 在生产者-消费者模型中，通常优先启动消费者

    p.start()

    print("=======================END=========================")
