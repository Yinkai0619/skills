import os

os.system('clear')

class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        print('a1 add~~~~~~`')
        print('self:', self)
        print('other: ', other)
        if hasattr(other, 'x'):
            return self.x + int(other.x)
        else:
            try:
                x = int(other)
            except:
                x = 0
            return self.x + other
        # try:
        #     other = int(other.x)
        # except:
        #     other = 0
        # return self.x + other

    def __iadd__(self, other):
        print('a2 iadd~~~~~~`')
        print('self:', self)
        print('other: ', other)
        return type(self)(self + other)

    def __radd__(self, other):
        print('a3 radd~~~~~~`')
        print('self:', self)
        print('other: ', other)
        # try:
        #     x = int(other.x)
        # except:
        #     x = 0
        # return self.x + x
        return self + other

    def __repr__(self):
        return '{}'.format(self.x)

class B:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if isinstance(other, type(self)):
            print('b1 add~~~~~~`')
            print('self:', self)
            print('other: ', other)
            return self.x + other.x
        else:
            return NotImplemented

    def __repr__(self):
        return '{}'.format(self.x)
    
a = A(4)
b = B(5)
c = A(6)
# c += a
# print(a+b)  # a.__add__(b)
# print('===========================================')
# print(b+a)  # b.__add__(a)
# print(a + '1')    # a.__add__(1)
print(1 + a)