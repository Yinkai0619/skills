#!/usr/bin/env python

import inspect

class TypeCheck:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.data = {}

    def __get__(self, instance, owner):
        if instance is not None:
#            print(self.__dict__, '========')
            return self.data[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError()
        self.data[self.name] = value

def typeassert(cls):
    sig = inspect.signature(cls)
    params = sig.parameters
    #print(params)
    for name, param in params.items():
        if param.annotation != param.empty:
            setattr(cls, name, TypeCheck(name, param.annotation))
    return cls


class TypeAssert:
    def __init__(self, cls):
        sig = inspect.signature(cls)
        params = sig.parameters
        for name, param in params.items():
            if param.annotation != param.empty:
                setattr(cls, name, TypeCheck(name, param.annotation))
        self.cls = cls

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)

#@typeassert
@TypeAssert
class Person:
#    name = TypeCheck('name', str)
#    age = TypeCheck('age', int)
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        print('{}: {}'.format(self.name, self.age))



if __name__ == '__main__':
    p1 = Person('tom', 18)
    print(p1.__dict__)
