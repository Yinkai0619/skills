import datetime
import logging
from threading import Thread

""" 
在5个线程内运行50亿次累加运算，观察用时，与在同一个线程内运行耗时几乎相同。
所以，对于CPU密集型程序，由于GIL的存在，使用多线程没有意义。因为，GIL保证CPython进程中只有一个线程执行字节码。
"""

logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(1000000):
        sum += 1


if __name__ == "__main__":
    ts = []
   
    for i in range(5):
        t = Thread(target=calc, name="t{}".format(i))
        t.start()
        ts.append(t)
    
    for t in ts:
        t.join()

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)     # 8593518080 255.23941
