import threading
import time
import logging

FORMAT = "%(asctime)s %(threadName)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class A:
    def __init__(self):
        self.x = 0


a = threading.local()


def work():
    a.x = 0
    for _ in range(100):
        time.sleep(0.0001)
        a.x += 1
    logging.info(a.x)


for i in range(5):
    threading.Thread(name="worker-{}".format(i), target=work).start()

print("main thread.")
