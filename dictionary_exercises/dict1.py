#!/usr/bin/env python


# 输入一个数，输出每位数字及重复的次数

num = '655350'
print(num)

def count1(num):
    counter = {}
    for i in num:
        count = 0
        for j in range(len(num)):
            if i == num[j]: count += 1
        counter[i] = count
    return counter


def count2(num):
    counter = {}
    for c in num:
        if c not in counter.keys():
            counter[c] = 1
        else:
            counter[c] += 1
    return counter

def count3(num):
    counter = {}
    for c in num:
        counter[c] = counter.get(c,0) + 1
    return counter
        
def count4(num):
    counter = dict()
    for c in num:
        counter[c] = counter.setdefault(c,0) + 1
    return counter


print(count1(num))
print(count2(num))
print(count3(num))
print(count4(num))
