#!/usr/bin/env python

import time
import datetime
import contextlib
from functools import wraps, update_wrapper

@contextlib.contextmanager
def add(x, y):  # add == timeit(add) == wrapper(x, y) == add(x, y)
    """This is a add function."""
    start = datetime.datetime.now()
    try:
        yield x + y
    finally:
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s'.format(add.__name__, delta), 'by TimeIt')
    time.sleep(1)
        

if __name__ == '__main__':
    with add(4, 5) as f:
       time.sleep(1)
       print(f)
