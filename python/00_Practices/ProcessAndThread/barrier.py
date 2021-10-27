from threading import Lock, RLock, Thread, Barrier, Event
import logging
import threading
import time
from typing import Awaitable


FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

barrier = Barrier(3)    # 等待3个线程


def worker(bar: barrier):
    print("I am working. ", bar.n_waiting)
    try:
        bar.wait(1)  # 当等待的线程数不足3个时，在此阻塞
    except threading.BrokenBarrierError:
        print("Broken...................")
    print("finish my job. ", bar.n_waiting)


ts = list()
for i in range(10):
    # if i == 2:
    #     barrier.abort()   # 手动打破屏障

    # if i == 4:
    #     barrier.reset()   # 手动恢复屏障

    t = Thread(target=worker, args=(barrier,))
    t.start()
    time.sleep(1)
    ts.append(t)


while True:
    time.sleep(1)
    print(barrier.n_waiting, barrier.broken)

print("="*30, "END", "="*30)
