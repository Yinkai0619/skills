class A:
    x = 100
    def show(self):
        pass

def __init__(self):
    self.y = 2000

def show(self):
    print(self.y)

XClass = type('X', (object,), {'x':100, 'show':show, "__init__":__init__})

XClass().show()
print((type(XClass)))
print(XClass.__dict__)
print(XClass.__mro__)
print(XClass.mro())
print(XClass.__name__)
print(XClass.X)
