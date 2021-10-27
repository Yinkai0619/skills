#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/12/5 下午9:54
'''

import threading
import time


def show_thread_info():
    print("Current Thread = {}".format(threading.current_thread()))
    print("Main Thread = {}".format(threading.main_thread()))
    print("Active Count = {}".format(threading.active_count()))
    # print("activeCount = {}".format(threading.activeCount()))
    print("Enumerate = {}".format(threading.enumerate()))
    print("Thread ID = {}".format(threading.get_ident()))


def worker(x, y):
    count = 0
    while True:
        time.sleep(1)
        print("I'm working.")
        # print("y: {}".format(y))
        show_thread_info()
        print("Finish")
        print("The count is: {}\n".format(count))
        count += 1
        if count > x:
            # raise Exception("Thread Error.")
            break


class MyThread(threading.Thread):
    def start(self) -> None:
        print("Start~~~~~~~~~~~~~~~")
        super().start()

    def run(self) -> None:
        print("Run~~~~~~~~~~~~~~~")
        super().run()


# t = threading.Thread(target=worker, name="worker1", args=(5,), kwargs={'y': 100})
# t = threading.Thread(target=worker, name="worker_1", kwargs={'y': 100, 'x': 5})
t = MyThread(name="worker2", target=worker, kwargs={'y': 200, 'x': 3})


if __name__ == '__main__':
    # show_thread_info()

    # t.start()
    t.run()
    # while True:
    #     time.sleep(1)
    #     if t.is_alive():
    #         print("{}: {} is alive.".format(t.name, t.ident))
    #     else:
    #         print("{}: {} is dead.".format(t.name, t.ident))
    #         t.start()

    # print("===END===")
