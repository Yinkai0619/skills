#!/usr/bin/env python

from contextlib import contextmanager

@contextmanager
def foo():
    print('enter')
    try:
        yield 'abc'
    finally:
        print('exit')


with foo() as f:
    print('---------------')
    raise IndexError()
    print(f)
    print('---------------')
