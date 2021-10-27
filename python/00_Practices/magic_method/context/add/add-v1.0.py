#!/usr/bin/env python

import time
import datetime
from functools import wraps

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s'.format(fn.__name__, delta))
        return ret
    return wrapper


#@timeit
def add(x, y):  # add == timeit(add) == wrapper(x, y) == add(x, y)
    """This is a add function."""
    time.sleep(2)
    return x + y


class TimeIt:
    def __init__(self, fn):
        self.__fn = fn

    def __enter__(self):
        self.start = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print('{} took {}s'.format(self.__fn.__name__, delta), 'with TimeIt')

    def __call__(self, *args, **kwargs):
        return self.__fn(*args, **kwargs)
        

if __name__ == '__main__':
    #print(add(4,5))

    with TimeIt(add) as f:
        print(f(4, 5))
