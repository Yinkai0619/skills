#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2021/2/4 下午9:46
'''

'''
非阻塞锁的使用。
构造10个任务，分别提交给5个线程进行处理，处理过程中使用锁，但不释放锁，且不能阻塞处理过程。
结果：任务被某个线程启动后，不会再被其他线程启动，10个任务只会执行一遍。
'''

import logging
import threading
import time

FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(tasks):
    for task in tasks:
        time.sleep(0.001)
        if task.lock.acquire(False):  # 不阻塞，获取锁后返回True，否则返回False
            logging.info('{} {} begin to start'.format(threading.current_thread(), task.name))
            # 此处没有释放锁
        else:
            logging.info('{} {} is working'.format(threading.current_thread(), task.name))


class Task:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()


# 构造10个任务
tasks = [Task('task-{}'.format(x)) for x in range(10)]

# 启动5个线程
for i in range(5):
    threading.Thread(target=worker, name='worker-{}'.format(i), args=(tasks,)).start()
