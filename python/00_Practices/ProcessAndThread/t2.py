import threading
import logging

def worker():
    for x in range(100):
        # print("{} is running.\n".format(threading.current_thread().name), end='')     # 改造低码: 因为字符串不可分割，所以可以将换行符与打印内容整合为同一字符串
        logging.warning("{} is running.".format(threading.current_thread().name))       # 替换函数或方法: 使用线程安全的函数来替代不安全的函数，推荐方法

for x in range(1, 5):
    name = "worker-{}".format(x)
    t = threading.Thread(target=worker, name=name)
    t.start()
