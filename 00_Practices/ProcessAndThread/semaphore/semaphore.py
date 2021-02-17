from threading import BoundedSemaphore, Lock, RLock, Semaphore, Thread, Barrier, Event, main_thread
import logging
import random

"""
模拟连接池。因为资源有限，且开启一个连接成本高，所以，使用连接池。
连接池应该有容量（总数），有一个工厂方法可以获取连接，能够把不用的连接返回，供其他调用者使用。
"""

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class Conn:
    """
    连接
    """

    def __init__(self, name) -> None:
        self.name = name


class Pool:
    """
    连接池
    """

    def __init__(self, count: int) -> None:
        self.count = count
        # 池中是连接对象的列表
        self.pool = [self._connect("conn-{}".format(x))
                     for x in range(self.count)]
        self.sema = BoundedSemaphore(count)

    def _connect(self, conn_name):
        # 创建连接的方法，返回一个名称
        return Conn(conn_name)

    def get_conn(self):
        # 从连接池中拿走一个连接，先取得令牌再取资源
        self.sema.acquire()
        return self.pool.pop()

    def return_conn(self, conn: Conn):
        # 向池中归还一个连接，先归还资源再归还令牌
        self.pool.append(Conn)
        self.sema.release()


if __name__ == "__main__":
    # 初始化连接池
    pool = Pool(3)

    def worker(pool: Pool):
        conn = pool.get_conn()
        logging.info(conn)
        # 模拟使用了一段时间
        Event().wait(random.randint(1, 4))
        pool.return_conn(conn)

    for i in range(6):
        Thread(target=worker, name="worker-{}".format(i), args=(pool,)).start()
