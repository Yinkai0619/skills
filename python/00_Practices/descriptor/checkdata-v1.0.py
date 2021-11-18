import os

os.system("clear")

class Person:
    def __init__(self, name:str, age:int) -> None:
        params = ((name, str), (age, int))
        if not self.checkdata(params):
            raise TypeError()
        print("ok==========")
        self.name = name
        self.age = age

    def checkdata(self, params):
        for k,v in params:
            if not isinstance(k, v):
                return False
        return True

p1 = Person("Nana", '30')
