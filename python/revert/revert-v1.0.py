#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/6 下午9:09
'''

# 将一个数逆序放入列表中,例如1234 => [4,3,2,1]

def revert1(n):
    n_list = []

    while n != 1:
        n, m = divmod(n, 10)
        n_list.append(m)
    else:
        n_list.append(n)

    return n_list

def revert2(n):
    sn = str(n)
    length = len(sn)
    n_list = [0] * length
    for i in range(length): # 0 1 2 3
        n_list[i] = int(sn[-i - 1])
    return n_list

# 递归取字符
def revert3(n):
    date = str(n)
    length = len(date) - 1
    def proc(x=length):
        if x == -1: return []
        return [int(date[x])] + proc(x - 1)
    return proc()

# 递归切片
def revert4(n):
    data = str(n)
    def proc(x, target=[]):
        if x:
            target.append(int(x[-1]))
            proc(x[:-1])
        return target
    return proc(data)

# 使用数字整除取模递归：
def revert5(n, target=None):
    if not target:
        target = []
    x, y = divmod(n, 10)
    target.append(y)

    if x == 0:
        return target
    return revert5(x, target)


print(revert5(1234))
