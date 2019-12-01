#!/usr/bin/env python3

import random

class RandomGen:
    def __init__(self, start=1, stop=100, patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch

    def generate(self):
        return [random.randint(self.start, self.stop) for _ in range(self.patch)]


class RandomGen:
    @classmethod
    def generate1(self, start=1, stop=100, patch=10):
        return [random.randint(start, stop) for _ in range(patch)]

    @staticmethod
    def generate2(start=1, stop=100, patch=10):
        return [random.randint(start, stop) for _ in range(patch)]


class RandomGen:
    def __init__(self, start=1, stop=100, patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield random.randint(self.start, self.stop)

    def generate(self, count=10):
        patch = self.patch if count <= 0 else count
        return [next(self._gen) for _ in range(patch)]


class RandomGen:
    def __init__(self, start=1, stop=100, patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield [random.randint(self.start, self.stop) for _ in range(self.patch)]

    def generate(self, count=10):
        if count > 0:
            self.patch = count
        return next(self._gen)

class Coordinate:
    def __init__(self, count=20):
        self.count = count
        self._codi = self._coordinate()

    def _coordinate(self):
        while True:
            yield tuple(RandomGen().generate(2))

    def generate(self, num=10):
        if num > 0:
            self.count = num
        return [next(self._codi) for _ in range(self.count)]

# print(*Coordinate().generate(4))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        pass

rg = RandomGen()
points = [Point(x,y) for x,y in zip(rg.generate(10), rg.generate(10))]
print(points)
