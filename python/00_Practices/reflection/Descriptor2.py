#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/11/24 下午10:23
'''

from functools import partial


class StaticMethod:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        # print(self, instance, owner)
        return self.fn


class ClassMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        # print(self, instance, owner)
        # return self.fn(owner)
        return partial(self.fn, owner)


class A:
    @StaticMethod
    def foo():      # foo = StaticMethod(foo) => StaticMethod的实例
        print("static method called.")

    @ClassMethod
    def bar(cls):   # bar = ClassMethod(bar)(cls)
        print("class method called.")

    @classmethod
    def mtd(cls):
        print("mtd called")


if __name__ == '__main__':
    a = A()
    # a.foo()
    # a.bar()
    A.bar()
    # a.mtd()
    # A.mtd()