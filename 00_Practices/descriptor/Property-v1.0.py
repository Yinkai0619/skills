#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/3/22 下午2:16
'''

class Property:
    def __init__(self, fget, fset = None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        # instance == a;  owner == A
        if instance is not None:
            return self.fget(instance)
        else:
            return self

    def __set__(self, instance, value):
        # instance == a; value == 100
        if instance is not None and callable(self.fset):
        # instance._data = value
            self.fset(instance, value)

    def setter(self, fset):
        self.fset = fset
        return self


class A:
    def __init__(self, data):
        self._data = data

    @Property   # data == Property(data) ==> Property实例
    def data(self):
        return self._data

    @data.setter   # data == data.setter(data) == Property实例.setter(data) ==> data == Property实例
    def data(self, value):
        self._data = value

if __name__ == '__main__':
    a = A(10)
    print(a.data)

    a.data = 100
    print(a.data)
