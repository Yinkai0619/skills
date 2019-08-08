#!/usr/bin/env python
import inspect

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

def add(x, y):
    return x + y

foo = partial(add, 4)
print(inspect.signature(foo))
print(foo(5))
