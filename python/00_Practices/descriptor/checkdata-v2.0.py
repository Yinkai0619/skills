import os

os.system("clear")

class CheckType():
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
    
    def __get__(self, instance, owner):
        # print(instance, type(instance), "------------")
        if instance is not None:
            return instance.__dict__[self.name]
        return self

    def __set__(self, instance, value):     # instance是Person的实例
        if not isinstance(value, self.type):
            raise TypeError()
        # setattr(instance, self.name, value)
        instance.__dict__[self.name] = value
        # print(instance, type(instance), "~~~~~~~~~~~~~~~")


class Person:
    name = CheckType("name", str)
    age = CheckType("age", int)
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age


p1 = Person("Nana", 30)
print(p1.__dict__)
print(p1.name)
print(p1.age)