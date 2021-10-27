#!/usr/bin/env python

from threading import Lock, RLock, Thread
import logging


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

lock = Lock()
print(1, lock)     # <unlocked _thread.lock object at 0x7fb59af8bde0>
lock.acquire()
print(2, lock)     # <locked _thread.lock object at 0x7fb59af8bde0>

print('='*50)

rlock = RLock()
print(3, rlock)      # <unlocked _thread.RLock object owner=0 count=0 at 0x7fb59afc4db0>
rlock.acquire()
rlock.acquire(False)    # 非阻塞，成功获取锁，返回True
rlock.acquire(timeout=3)   # 阻塞，延迟3秒。成功获取锁，返回True
print(4, rlock)    # <locked _thread.RLock object owner=140417967343232 count=3 at 0x7fb59afc4db0>
print('-'*50)
rlock.release()
rlock.release()
print(5, rlock)    # <locked _thread.RLock object owner=140417967343232 count=1 at 0x7fb59afc4db0>
# rlock.release()
# rlock.acquire(False)
print(6, rlock)    # <unlocked _thread.RLock object owner=0 count=0 at 0x7f3121375db0>

print('='*50)


def sub(lock:RLock):
    logging.info("~~~~~~~~~~~~~~ In sub thread ~~~~~~~~~~~~~~")
    # lock.acquire()
    print(10, lock.acquire(blocking=False))      # 10 False
    logging.info("~~~~~~~~~~~~~~ End sub thread ~~~~~~~~~~~~~~")
    print(9, lock)  # 9 <locked _thread.RLock object owner=140049733064448 count=1 at 0x7f5fdeca7c00>


# sub(rlock)

# print(7, rlock)     # 7 <locked _thread.RLock object owner=140685111821952 count=1 at 0x7ff3cd07cc00>
Thread(target=sub, name="subthread", args=(rlock,)).start()
print(8, rlock)

print("="*30, "END", "="*30)
