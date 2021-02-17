import datetime
import logging
from threading import Thread

logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(1000000000):
        sum += 1


if __name__ == "__main__":
    t1 = Thread(target=calc)
    t2 = Thread(target=calc)
    t3 = Thread(target=calc)
    t4 = Thread(target=calc)
    t5 = Thread(target=calc)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)     # 8593518080 255.23941
