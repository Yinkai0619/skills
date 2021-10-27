#!/usr/bin/env python

import time
import datetime
from functools import wraps, update_wrapper

def timeit(fn):
    @wraps(fn)  # wrapper(*args, **kwargs) == wraps(fn)(wrapper)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('{} took {}s'.format(fn.__name__, delta), 'by timeit' )
        return ret
    return wrapper


class TimeIt:
    '''The doc from TimeIt.'''
    def __init__(self, fn):
        self.__fn = fn
#        self.__doc__ = fn.__doc__
#        self.__name__ = fn.__name__
#        update_wrapper(self, fn)
        wraps(fn)(self)

    def __enter__(self):
        self.start = datetime.datetime.now()
#        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print('{} took {}s'.format(self.__fn.__name__, delta), 'by TimeIt')

    def __call__(self, *args, **kwargs):
#        print('call')
#        self.start = datetime.datetime.now()
        ret = self.__fn(*args, **kwargs)
#        delta = (datetime.datetime.now() - self.start).total_seconds()
#        print('{} took {}s'.format(self.__fn.__name__, delta), 'by TimeIt')
        return ret


#@TimeIt     # add(x, y) == TimeIt(add) == TimeIt().__call__(x, y)
#@timeit
def add(x, y):  # add == timeit(add) == wrapper(x, y) == add(x, y)
    """This is a add function."""
    time.sleep(1)
    return x + y
        

if __name__ == '__main__':
    #print(add(4,5))

#    with TimeIt(add) as f:
#        print(f(4, 5))
    print(add(4,5))
