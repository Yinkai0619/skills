#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/6 下午2:20
'''

def fac(n=5):
    if n == 1:
        return 1
    return fac(n-1) * n

def fac1(n=5):
    return 1 if n == 1 else fac(n-1) * n

def fac2(n=3, fac=1):
    if n == 1:
        return fac
    fac = n * fac
    return fac2(n-1, fac)



print(fac2(5))

