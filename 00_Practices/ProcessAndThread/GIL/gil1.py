import datetime
import logging

""" 在一个线程内运行50亿次累加运算，观察用时 """

logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(1000000000):
        sum += 1


if __name__ == "__main__":
    for _ in range(5):
        calc()

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)         # 8597917184 256.089637
