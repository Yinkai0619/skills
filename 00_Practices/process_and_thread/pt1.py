#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/4/8 下午10:21
'''

import threading
import time

def showthreadinfo():
    print('Current thread = {}'.format(threading.current_thread()))
    print('Main thread = {}'.format(threading.main_thread()))
    print('Active count = {}'.format(threading.active_count()))

def worker(x = 3):
    count = 0
    print('-'*30)
    showthreadinfo()
    while True:
        time.sleep(1)
        print('I am working.')
        # print('Finish')
        count += 1
        if count > x:
            # raise Exception('Thread error.')
            break

class MyThread(threading.Thread):
    def start(self) -> None:
        print('Start~~~~~~~~~~~~~')
        super().start()

    def run(self) -> None:
        print('Run~~~~~~~~~~~~~')
        super().run()


t = MyThread(target=worker, name='worker1')
# showthreadinfo()
# t.start()
t.run()
print(t.ident)

# while True:
#     time.sleep(1)
#     if t.is_alive():
#         print('{} {} alive.'.format(t.name, t.ident))
#     else:
#         print('{} {} dead.'.format(t.name, t.ident))
#         t.start()
#     break
#
#
# print('=====end=====')
