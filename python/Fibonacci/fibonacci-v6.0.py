#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/3/1 下午10:14
'''



class Fib:
    def __init__(self):
        self.items = [0, 1, 1]

    def __call__(self, index):
        if index >= len(self.items):
            for i in range(len(self), index + 1):
                self.items.append(self.items[i - 1] + self.items[i - 2])
        return self.items[index]

    def __getitem__(self, index):
        return self(index)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)


fib = Fib()
# print(fib(10))
# print(fib.items)
# print(fib[10])
# print(len(fib))
fib(10)
for i in fib:
    print(i)
