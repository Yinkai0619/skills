import datetime
import logging
# from threading import Thread
import multiprocessing

logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(1000000000):
        sum += 1


if __name__ == "__main__":
    ps = list()

    for i in range(5):
        p = multiprocessing.Process(target=calc, name="p-{}".format(i))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()


    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)     # 8666242560 76.749764
