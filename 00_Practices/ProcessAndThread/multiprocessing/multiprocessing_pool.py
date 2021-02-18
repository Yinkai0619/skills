import datetime
import logging
import multiprocessing

logging.basicConfig(level=logging.INFO, format="%(process)d %(processName)s %(message)s")

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(10000000):
        sum += 1
    return sum


if __name__ == "__main__":
    # ps = list()

    # for i in range(5):
    #     p = multiprocessing.Process(target=calc, name="p-{}".format(i))
    #     p.start()
    #     ps.append(p)

    # for p in ps:
    #     p.join()


    pool = multiprocessing.Pool(5)

    for _ in range(5):
        pool.apply_async(calc, callback=lambda x: logging.info("Sum={}".format(x)))
        # pool.apply(calc)

    pool.close()
    pool.join()



    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)     # 140192006715008 104.407929
