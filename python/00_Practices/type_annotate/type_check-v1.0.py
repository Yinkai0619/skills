#!/usr/bin/env python

class Person:
    def __init__(self, name:str, age:int):
        params = ((name, str), (age, int))
        if not self.checkdata(params):
            raise TypeError()
        self.name = name
        self.age = age
        print('{}: {}'.format(self.name, self.age))


    def checkdata(self, params):
        for k, v in params:
            if not isinstance(k, v):
                return False
        return True


if __name__ == '__main__':
    p1 = Person('tom', '18')
