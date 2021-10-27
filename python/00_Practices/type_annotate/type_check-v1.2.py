#!/usr/bin/env python

class TypeCheck:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.data = {}

    def __get__(self, instance, owner):
        if instance is not None:
            print(self.__dict__, '========')
            return self.data[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError()
        self.data[self.name] = value


class Person:
    name = TypeCheck('name', str)
    age = TypeCheck('age', int)
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        print('{}: {}'.format(self.name, self.age))



if __name__ == '__main__':
    p1 = Person('tom', 18)
    print(p1.__dict__)
