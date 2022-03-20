import os

os.system('clear')

class A:
    x = 100
    def __init__(self) -> None:
        self.y = 2000
    def show(self):
        print(self.y)

###########################################################################################


def __init__(self):
    self.y = 2000

def show(self):
    print(self.y)

XClass = type('X',(object,), {'x':100,'show':show, '__init__':__init__})
print(type(XClass))
print(XClass)
print(XClass.mro())
print(XClass.__dict__)
print(XClass.show)
print(XClass.show(XClass()))
XClass().show()