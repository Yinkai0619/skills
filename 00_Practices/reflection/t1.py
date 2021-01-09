
def addName(cls):
    cls.NAME = 'Yinkai'
    return cls

@addName    # addName(Point) => Point     
class Point:
    z = 6
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

"""     def show(self):
        print(self.x, self.y) """

class AMixin: pass

class PointMixin(AMixin, Point): pass


print(Point.__dict__)


p1 = Point(4, 5)
# p1.x = 10
# print(p1.x)

# print(Point.__dict__)
# print(p1.__dict__)
# print(Point.show)
# print(dir(p1))
""" for p in dir(p1):
    print(type(p), p)
    print(getattr(p1, p))
    print() """

# p = 'y'
# if hasattr(p1, p):
#     print(getattr(p1, p, None))

# print(getattr(p1, 'a', 'A'))

# setattr(p1, 'b', 1000)
# print(p1.__dict__)
# print(getattr(p1, '__dict__', None))

# setattr(Point, 'show', lambda self: print(self.x, self.y))
# print(Point.__dict__)
# getattr(p1, 'show')()
# p1.show()
# print(getattr(Point, 'show'))()
# setattr(p1, 'show1', lambda self: print(self, '~~~~~~~~~~~~'))
# p1.show2 = lambda self: print('show222222222')
# print(Point.__dict__)
# print(p1.__dict__)

# p1.show1(p1)
# p1.show2(p1)