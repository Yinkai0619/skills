import threading
import logging

logging.basicConfig(level=logging.INFO)

def do(event:threading.Event, interval:int):
    while not event.wait(interval):     # 等待3秒后返回False
        logging.info("do sth.")

e = threading.Event()
threading.Thread(target=do, args=(e, 3)).start()

e.wait(10)  # 主线程10秒后执行set置True，当轮询到工作线程后工作线程立即退出
e.set()

print("The main threading is exit.")
