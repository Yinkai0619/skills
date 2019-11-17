#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/11/9 下午6:04
'''

import threading
import time
from queue import Queue

q = Queue()
def add(x,y):
    # time.sleep(3)
    # print(x+y)
    while True:
        print('Entering "t" thread.')
        cmd = q.get()
        if cmd == 'quit':
            break
        print(cmd)
        print('-'*30)

t = threading.Thread(target=add, args=(4,5))
t.start()

while True:
    cmd = input('>>>')
    if cmd == 'quit':
        q.put(cmd)
        break
    else:
        q.put(cmd)
    print('+'*30)


