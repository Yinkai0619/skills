#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/12/1 下午4:56
'''

class Car:
    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed


class CarInfo:
    cars = list()

    @classmethod
    def add_car(cls, car:Car):
        cls.cars.append(car)

    @classmethod
    def get_all_car(cls):
        return cls.cars


ci = CarInfo()
# car = Car('baojun', 'white', 100000, '220km/h')
ci.add_car(Car('baojun', 'white', 100000, '220km/h'))
print(ci.get_all_car())


# yinkai = Car()
# baina = Car()
# yinkai.add('yinkai', 'baojun', 'white', 100000, '220km/h')
# baina.add('baina', 'BMW', 'black', 300000, '240km/h')
# yinkai.show()
# baina.show()
# Car.showall()
#
