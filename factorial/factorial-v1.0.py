#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/6 下午2:20
'''

def fac(n=5):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(fac())