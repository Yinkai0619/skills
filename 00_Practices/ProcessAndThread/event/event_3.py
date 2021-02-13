from threading import Thread, Event
"""
自实现timer，延迟interval时长后执行函数。
"""


class Timer:
    def __init__(self, interval, func, args=(), kwargs={}) -> None:
        super().__init__()
        self.interval = interval
        self.fn = func
        self.args = args
        self.kwargs = kwargs
        self.event = Event()

    def start(self):
        Thread(target=self._run).start()

    def _run(self):
        # self.event.wait(self.interval)
        # if not self.event.is_set:
        if not self.event.wait(self.interval):
            self.fn(*self.args, **self.kwargs)
            # Thread(target=self.fn, args=self.args, kwargs=self.kwargs).start()

    def cancel(self):
        self.event.set()


def add(x, y):
    print(x + y)


t = Timer(3, add, (4, 5))
t.start()
# t.cancel()

print("main threading is exit.")
