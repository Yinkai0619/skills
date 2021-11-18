import os
os.system("clear")

class A:
    def b(self):
        print("~~~~~~~~~~")
    def __init__(self) -> None:
        self.b = 3000

    @classmethod
    def c(cls):
        print(cls)

a = A()
# a.b()

a.c = 4000
print(A.__dict__)
print(a.__dict__)
print('-'*30)
print(a.b)
