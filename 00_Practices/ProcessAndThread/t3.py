import threading
import time

def work():
    time.sleep(10)
    print("work")

def foo():
    time.sleep(2)
    print("foo")

def bar():
    t = threading.Thread(target=work, name="work", daemon=True)
    t.start()
    # t.join()    # 如果在此调用t.join()，则会等待线程t，当线程执行完毕后再继续执行；如果不调用t.join()，因为t为daemon线程，当主线程执行完毕后会直接退出，所以t线程未必会执行。
    time.sleep(5)
    print("bar")

t1 = threading.Thread(target=foo, name="foo", daemon=True)
t2 = threading.Thread(target=bar, name="bar", daemon=True)

t1.start()
t2.start()
t2.join()   # 主线程在此等待t2线程的执行，当t2执行完毕后主线程才会继续向后执行

time.sleep(1)

print("main thread exits.")


