#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/12/1 下午4:56
'''

class Car:
    CARS = dict()
    def add(self, owner, mark, color, price, speed):
        self.owner = owner
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed
        Car.CARS[self.owner] = dict(owner=self.owner, mark=self.mark, color=self.color, price=self.price, speed=self.speed)

    def show(self):
        print(Car.CARS[self.owner])

    @classmethod
    def showall(cls):
        print(cls.CARS.items())

yinkai = Car()
baina = Car()
yinkai.add('yinkai', 'baojun', 'white', 100000, '220km/h')
baina.add('baina', 'BMW', 'black', 300000, '240km/h')
yinkai.show()
baina.show()
Car.showall()

