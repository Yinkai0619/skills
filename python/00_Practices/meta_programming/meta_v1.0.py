import os

os.system('clear')

class ModelMeta(type):      # 元类
    def __new__(cls, name, bases, attrs:dict):
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        return super().__new__(cls, name, bases, attrs)

class A(metaclass=ModelMeta):
    id = 100
    def __init__(self) -> None:
        self.x = 2000

print('~' * 30)

class B(A):
    X = 'x'

print('~' * 30)

C = ModelMeta('C_Class', (), {'y':2000})

print('~' * 30)

class D(ModelMeta): pass

print('~' * 30)

E = type('E_Class', (), {})

print('~' * 30)

print('-' * 30)
print(type(A))
print(type(B))
# print(B.mro())
print(type(C))
print(type(D))
print(type(E))