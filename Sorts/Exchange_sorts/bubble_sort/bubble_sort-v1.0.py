#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/6/20 15:27
'''
import random

m_list = [
    [1, 9, 8, 5, 6, 7, 4, 3, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
]
# c_list = [random.randrange(21) for _ in range(10)]
c_list = m_list[1]
print("Initial:\t", c_list, "\n========================================")
count_swap = 0
count = 0
for i in range(len(c_list) - 1):
    for j in range(len(c_list) - 1):
        count += 1
        if c_list[j] > c_list[j + 1]:
            c_list[j], c_list[j + 1] = c_list[j + 1], c_list[j]
            count_swap += 1
print("Result:\t\t", c_list)
print("Count: {}\tSwap: {}".format(count, count_swap))
