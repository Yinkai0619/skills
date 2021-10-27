import os
from functools import total_ordering

os.system('clear')

# @total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __hash__(self):
    #     return hash((self.x, self.y))

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == self.y

    def __add__(self, other):
       return self.__class__(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        # self.x += other.x
        # self.y += other.y
        self.x, self.y = self.x + other.x, self.y + other.y
        return self
    # def __sub__(self, other):
    #     return self.__class__(self, self.x - other.x, self.y - self.y)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __repr__(self):
        return '<Point {}:{}>'.format(self.x, self.y)
    

# p1 = Point(1,2)
# p2 = Point(1,2)
p1 = Point(3,4)
p2 = Point(1,2)
p3 = Point(3,5)
# p3 = p1 + p2
# print(type(p3), p3.__dict__)

# p1 += p2
# print(type(p1), p1.__dict__)

# print('YES' if len({p1, p2}) == 1 else 'NO')

print(p1 == p2)
print(p1 != p2)
print(p1 == p3)
print('-'*30)
print(p1 > p3)
print(p1 < p3)
print(p1 >= p3)
print(p1 >= p3)

l = [p1, p2, p3]
print(sorted(l))