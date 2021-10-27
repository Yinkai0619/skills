#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/6/24 下午9:40
'''
# 一元选择排序，也称为简单选择排序

import random

lists = [
    [3, 5, 9, 1, 6, 8, 4, 7, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
]
sort_list = lists[0]
# random.shuffle(sort_list)
print(sort_list)

length = len(sort_list)

counter_swap = 0
counter_iter = 0
for i in range(length - 1):
    max_index = i
    for j in range(i + 1, length):
        counter_iter += 1
        if sort_list[max_index] < sort_list[j]:
            max_index = j
    if i != max_index:
        sort_list[i], sort_list[max_index] = sort_list[max_index], sort_list[i]
        counter_swap += 1

print(sort_list)
print('Swap: ', counter_swap, '\nIter: ', counter_iter)
