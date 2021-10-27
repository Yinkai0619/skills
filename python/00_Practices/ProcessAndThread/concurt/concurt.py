import logging
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

logging.basicConfig(
    level=logging.INFO,
    format="%(process)d %(processName)s %(thread)s %(message)s")


def worker(n):
    logging.info("begin to work{}".format(n))
    time.sleep(random.randint(2, 8))
    logging.info("finished {}".format(n))
    return random.randint(1, 10)


def calc():
    sum = 0
    for _ in range(1000000000):
        sum += 1


if __name__ == "__main__":

    # executor = ThreadPoolExecutor(3)    # 创建线程执行器(线程池)，并指定数量（创建游泳池，并划分泳道）
    # executor = ProcessPoolExecutor(3)    # 创建进程执行器(进程池)，并指定数量（创建游泳池，并划分泳道）

    fs = []  # 用于收集Future对象

    with ProcessPoolExecutor(max_workers=3) as executor:
        # print(type(executor), "~~~~~~~~~~~~~~~~~~~~~")
        for i in range(6):  # 总任务数
            f = executor.submit(worker, i)  # 向执行器提交要执行的工作函数
            # f = executor.submit(calc)      # 向执行器提交要执行的工作函数
            fs.append(f)

        while True:
            time.sleep(2)
            flag = True  # 所有任务完成标记

            for f in fs:
                flag = flag and f.done()  # 只要有一个工作线程还没有完成任务，flag就为False
                if not flag:
                    break
            # print(threading.enumerate())

            if flag:
                # logging.info("the all task is finished.")
                # for f in fs:
                #     logging.info("{} result = {}".format(f, f.result()))
                # executor.shutdown()     # 手动关闭执行器
                break

        logging.info("the all task is finished.")
        for f in fs:  # 输出工作结果
            logging.info("{} result = {}".format(f, f.result()))
            # print(type(f), '============================')

    print('=' * 30, "END", '=' * 30)