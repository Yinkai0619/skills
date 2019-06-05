#!/usr/bin/env python

'''
数字重复统计：
    1.随机产生100个整数；
    2.数字范围[-1000,1000]；
    3.升序输出这些数字并打印其重复的次数。
'''

# import random
#
# def gen_num(n=100,m=1000):
#     result = list()
#     for _ in range(n):
#         result.append(random.randint(-m,m))
#     return result
#
# nums = gen_num()
#
# def count(ns=nums):
#     counter = {}
#     for c in ns:
#         counter[c] = counter.get(c,0) + 1
#     return sorted(counter.items())
#
#
#
# print(nums,'\n')
# print(count())

import random
nums = [random.randint(-1000,1000) for _ in range(100)]
nums.sort()

counter = {}

for i in nums:
    counter[i] = counter.get(i,0) + 1

print(nums)
print(counter)
