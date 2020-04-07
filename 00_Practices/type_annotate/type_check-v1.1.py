#!/usr/bin/env python

class TypeCheck:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __get__(self, instance, owner):
        if instance is not None:
            return instance.__dict__[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError()
        instance.__dict__[self.name] = value


class Person:
    name = TypeCheck('name', str)
    age = TypeCheck('age', int)
    def __init__(self, name:str, age:int):
#        params = ((name, str), (age, int))
#        if not self.checkdata(params):
#            raise TypeError()
        self.name = name
        self.age = age
        print('{}: {}'.format(self.name, self.age))


#    def checkdata(self, params):
#        for k, v in params:
#            if not isinstance(k, v):
#                return False
#        return True


if __name__ == '__main__':
    p1 = Person('tom', 18)
    print(p1.__dict__)
