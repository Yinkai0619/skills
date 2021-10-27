import datetime
import logging
import multiprocessing
""" 
使用进程池，在进程池中启动5个进程，并行完成50亿次累加运算，观察用时。
"""

logging.basicConfig(level=logging.INFO,
                    format="%(process)d %(processName)s %(message)s")

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(10000000):
        sum += 1
    return sum


if __name__ == "__main__":

    pool = multiprocessing.Pool(5)

    for _ in range(5):
        pool.apply_async(calc,
                         callback=lambda x: logging.info("Sum={}".format(x)))

    pool.close()
    pool.join()

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)
