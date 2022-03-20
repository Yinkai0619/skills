#!/usr/bin/env python
import os
from functools import partial

os.system("clear")

class StaticMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        print(self, instance, owner)
        return self.fn


class ClassMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        print(self, instance, owner)
        return partial(self.fn, owner)


class A:
    @StaticMethod   # foo == StaticMethod(foo)
    def foo():
        print('static method called.')

    @ClassMethod    # bar == ClassMethod(bar)
    # @classmethod
    def bar(cls):
        print('class method called.')


a = A()
# a.foo()     # des = a.foo; des()
a.bar()      # a.__class__
# A.bar()