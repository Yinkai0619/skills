#!/usr/bin/env python3

class Temperature:
    def __init__(self, t, unit='c'):
        self._f = None
        self._k = None
        self._c = None

        if unit == 'k':
            self._k = t
            self._c = self.k2c(t)
        elif unit == 'f':
            self._f = t
            self._c = self.f2c(t)
        else:
            self._c = t

    @property
    def c(self):    # 摄氏度
        return self._c

    @property
    def k(self):    # 华氏温度
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k

    @property
    def f(self):    # 开氏温度
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @classmethod
    def c2f(cls, c):
        return 9 * c / 5 + 32

    @classmethod
    def f2c(cls, f):
        return 5 * ( f - 32 ) / 9

    @classmethod
    def c2k(cls, c):
        return c + 273.15

    @classmethod
    def k2c(cls, k):
        return k - 273.15

    @classmethod
    def k2f(cls, k):
        return cls.c2f(cls.k2c(k))

    @classmethod
    def f2k(cls, f):
        return cls.c2k(cls.f2c(f))

if __name__ == "__main__":

    temp = Temperature(30)
    print(temp.c, temp.f, temp.k)

    print(Temperature.c2f(30))