#!/usr/bin/env python

import threading
import time

def worker():
    #print(list(s))
    time.sleep(30)
    print('I am working.')
    print('Finish')

#t = threading.Thread(target=worker, args='abc', name='worker1')
t = threading.Thread(target=worker, name='worker1')

t.start()
time.sleep(30)
print('===end===')
