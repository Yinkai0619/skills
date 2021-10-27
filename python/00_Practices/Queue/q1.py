#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/11/8 下午10:11
'''

from queue import Queue

q = Queue(5)
for i in range(5):
    q.put(i+1)

while True:
    a = input('>>>')
    print('queue is full: {}'.format(q.full()))
    if not q.full():
        q.put_nowait(a)
    else:
        while not q.empty():
            print(q.get())
    print('='*30)




