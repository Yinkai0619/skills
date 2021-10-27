#!/usr/bin/env python3

import random

class RandomGen:
    def __init__(self, start=1, stop=100, patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch

    def generate(self):
        return [random.randint(self.start, self.stop) for _ in range(self.patch)]

rg = RandomGen(patch=20)
print(rg.generate())

class RandomGen:
    @classmethod
    def generate1(self, start=1, stop=100, patch=10):
        return [random.randint(start, stop) for _ in range(patch)]

    @staticmethod
    def generate2(start=1, stop=100, patch=10):
        return [random.randint(start, stop) for _ in range(patch)]

print(RandomGen.generate2(50, patch=5))


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

rg = RandomGen()
print(rg.generate())


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

print(RandomGen().generate(15))
