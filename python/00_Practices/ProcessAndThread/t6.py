#!/usr/bin/env python
from threading import Timer


def add(x, y):
    print(x + y)


t = Timer(5, function=add, args=(4, 5))
t.start()

print("main thread.")
