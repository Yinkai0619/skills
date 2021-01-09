#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/11/27 下午9:34
'''
import inspect

# class person:
#     def __init__(self, name: str, age: int):
#         params = ((name, str), (age, int))
#         if not self.check_data(params):
#             raise TypeError()
#         print("Type is ok.")
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def check_data(params):
#         for k, v in params:
#             if not isinstance(k, v):
#                 return False
#         return True

# 用数据描述器实现类型检查
class TypeCheck:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.data = {}

    def __get__(self, instance, owner):
        if instance is not None:
            print(self.__dict__,"========")
            # return instance.__dict__[self.name]
            # return self.__dict__['name']
            return self.data[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError()
        # setattr(instance,self.name,value)
        # instance.name = value
        # instance.__dict__[self.name] = value
        self.data[self.name] = value

# def typeassert(cls):
#     sig = inspect.signature(cls)
#     params = sig.parameters
#
#     for name, param in params.items():
#         print(param.annotation,"----")
#         # print(name,param,"+++++")
#         if param.annotation != param.empty:
#             setattr(cls, name, TypeCheck(name, param.annotation))
#     return cls

class TypeAssert:
    def __init__(self, cls):
        sig = inspect.signature(cls)
        params = sig.parameters

        for name, param in params.items():
            # print(param.annotation, "----")
            # print(name,param,"+++++")
            if param.annotation != param.empty:
                setattr(cls, name, TypeCheck(name, param.annotation))
        self.cls = cls

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)

# @typeassert
@TypeAssert     # Person = TypeAssert(Person)
class Person:
    # name = TypeCheck('name',str)
    # age = TypeCheck('age',int)
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p1 = Person("Nana", 29)
    # print(p1.__dict__)
    print(p1.name)
    print(p1.age)
    # print(inspect.signature(Person).parameters.items())
