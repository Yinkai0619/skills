#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2021/1/19 下午9:56
'''

"""
将数字先减50次，再加50次。在c1个线程中，将此过程执行c2次。
"""
import threading
from threading import Thread, Lock


class Counter:
    def __init__(self):
        self._val = 0
        self.lock = Lock()

    @property
    def value(self):
        return self._val

    def inc(self):
        self.lock.acquire()     # 获取锁，保证以下计算的原子性，方法1：
        try:
            self._val += 1  # 等价：self._val = self._val + 1, 为两条语句, 有可能会被多线程打断，为线程不安全
        finally:
            self.lock.release()

    def dec(self):
        with self.lock:    # 获取锁，保证以下计算的原子性， 加锁方法2 (推荐):
            self._val -= 1  # 等价：self._val = self._val - 1, 为两条语句，线程不安全


def run(c: Counter, count=100):  # c为线程不安全对象
    for _ in range(count):
        for i in range(-50, 50):
            if i < 0:
                c.dec()
            else:
                c.inc()


c = Counter()
c1 = 10  # 线程数
c2 = 1000

threads = []  # 线程容器
for _ in range(c1):
    t = Thread(target=run, args=(c, c2))
    t.start()
    threads.append(t)

# 保证主线程打印最终结果，方法1：
# for t in threads:
#     t.join()        # join所有工作线程，保证主线程中的print语句打印最终结果
# print(c.value)      # 此语句在主线程中执行，当计算的次数较多时，程序执行的时间会比较长。此语句被调度执行时会将未完成的计算结果打印出来。


# 保证主线程打印最终结果，方法2：
e = threading.Event()
while not e.wait(1):
    if threading.active_count() == 1:  # 当活动线程仅剩主线程时执行以下语句
        print(c.value)
        e.set()
    else:
        print(threading.enumerate())

print("====== END ======")
