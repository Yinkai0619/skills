import os

os.system('clear')

class A:    # 描述器
    def __init__(self) -> None:
        self.a1 = 'a1'
        print('A.init')

    def __get__(self, instance, owner):
        print("A.__get__ {} {} {}".format(self, instance, owner))
        # print(type(self),'~~~~~~~~~~')
        return self

    def __set__(self, instance, value):
        print("A.__set__ {} {} {}".format(self, instance, value))
        self.data = value

class B:
    x = A()
    def __init__(self) -> None:
        print("B.init")
        # self.b = A()
        self.x = 'b.x'

print('-' * 30)
print(B.x)

print('=' * 30)
b = B()
b.x = 500
B.x = 600
print(b.x)
print(b.__dict__,"!!!!!!!!!!!!")
print(b.x.a1)
