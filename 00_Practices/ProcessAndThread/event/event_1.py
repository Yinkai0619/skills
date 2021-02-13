import threading
import time

"""
老板等待工人生产杯子
"""
"""
# 传统方法：
#  
cups = []
flag = False

def worker(count=10):
    global flag
    while True:
        print("I am working.")
        time.sleep(0.5)
        cups.append(1) 

        if len(cups) >= count:
            flag = True
            break
    print(cups)


def boss(check_time):
    global flag
    while True:
        time.sleep(check_time)
        print("Boss is wating.")
        if flag:
            print("Good Job.")
            break

threading.Thread(target=worker, name="worker", args=(10,)).start()
threading.Thread(target=boss, name="boss", kwargs={'check_time':1}).start()
 """

# 使用Event类方法：

cups = []
e = threading.Event()


def worker(e: threading.Event, count=10):
    while True:
        print("I am working.")
        time.sleep(0.5)
        cups.append(1)

        if len(cups) >= count:
            e.set()
            break
    print(cups)


def boss(e: threading.Event, check_time):
    print("Boss is waiting.")
    e.wait()  # 线程阻塞，至到e置为True (e.set())
    print("Good Job.")


threading.Thread(target=worker, name="worker", args=(e, 10,)).start()
threading.Thread(target=boss, name="boss", kwargs={'check_time': 1, 'e': e}).start()
