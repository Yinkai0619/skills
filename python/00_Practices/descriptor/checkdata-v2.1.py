import os
import inspect


#
# os.system("clear")


class TypeCheck():
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        # self.data = {}

    def __get__(self, instance, owner):
        # print(instance, type(instance), "------------")
        if instance is not None:
            return instance.__dict__[self.name]
            # return self.data[self.name]
        return self

    def __set__(self, instance, value):  # instance是Person的实例
        if not isinstance(value, self.type):
            raise TypeError()
        # setattr(instance, self.name, value)
        instance.__dict__[self.name] = value
        # print(instance, type(instance), "~~~~~~~~~~~~~~~")
        # self.data[self.name] = value


def typeassert(cls):
    sig = inspect.signature(cls)
    params = sig.parameters
    print(params, type(params), "1111111111111111111")
    for name, param in params.items():
        print(param.annotation, type(param.annotation), "2222222222222222")
        if param.annotation != param.empty:
            setattr(cls, name, TypeCheck(name, param.annotation))
    return cls


class TypeAssert():
    def __init__(self, cls):
        sig = inspect.signature(cls)
        params = sig.parameters
        # print(params, type(params), "1111111111111111111")
        for name, param in params.items():
            # print(param.annotation, type(param.annotation), "2222222222222222")
            if param.annotation != param.empty:
                setattr(cls, name, TypeCheck(name, param.annotation))
        self.cls = cls

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)


# @typeassert     # Person == typeassert(Person)
@TypeAssert
class Person:
    # name = TypeCheck("name", str)
    # age = TypeCheck("age", int)
    # print(name.__dict__, "============")
    # print(age.__dict__, "============")

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


p1 = Person("Nana", 30)
print(p1.__dict__)
print(p1.name)
print(p1.age)
print('-' * 50)
print(inspect.signature(Person))
