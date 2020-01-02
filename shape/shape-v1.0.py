import math
import json
import msgpack

class Shape:
    @property
    def area(self):
        raise NotImplementedError('Not Implemented.')

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

def serialize(m):
    def wrapper(cls):
        # if m.lower() == 'json':
        #     ser = json.dumps(cls.__dict__)
        # elif m.lower() == 'msgpack':
        #     ser = msgpack.dumps(cls.__dict__)
        # else:
        #     raise NotImplementedError
        # return ser
        print(cls.__dict__)
    return wrapper

@serialize(m='json')
class Rectangle(Shape):     # Rectangle = serialize(m='json')(Rectangle) = wrapper(Rectangle)
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius * self.radius

class SerializableMixin:
    def serialize(self, m='json'):
        if m.lower() == 'json':
            return json.dumps(self.__dict__)
        elif m.lower() == 'msgpack':
            return msgpack.dumps(self.__dict__)
        else:
            raise NotImplementedError

class SerializableCircleMixin(SerializableMixin, Circle):
    pass

# c = Circle(4)
# print(c.area)

# scm = SerializableCircleMixin(4)
# print(scm.area)
# print(scm.serialize())

ran = Rectangle(4,5)
# print(ran.area)