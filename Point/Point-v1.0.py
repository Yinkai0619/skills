import os

os.system('clear')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == self.y

p1 = Point(1,2)
p2 = Point(1,2)

print('YES' if len({p1, p2}) == 1 else 'NO')