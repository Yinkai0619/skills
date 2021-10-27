#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/18 下午9:45
'''

# 自己实现sorted

import random

# nums = list(range(10))
# random.shuffle(nums)

nums = [2, 6, 5, 3, 0, 1, 4, 7, 9, 8]

# def compare(a, b):
#     return a > b

def sort(iterable, *, reverse=False, key = lambda x: int(x)):
    newlist = []
    for x in iterable:
        for i, y in enumerate(newlist):
            flag = key(x) > key(y) if reverse else key(x) < key(y)
            if flag:
                newlist.insert(i, x)
                break
        else:
            newlist.append(x)


    return newlist


print(nums)
new_nums = sort(nums)
print(new_nums)
