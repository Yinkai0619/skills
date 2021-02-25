#!/usr/bin/env python

num = 12233344444
'''
输入一个数字：
1.判断其位数；
2.输出每位数字出现的次数；
3.从高到低依次输出。
'''
nl = len(str(num))
print("Bit: {}".format(nl))

snum = str(num)
searched = []
for i in snum:
    if i in searched:
        continue
    count = snum.count(i)
    print("{}:{}".format(i, count))
    searched.append(i)


print('From high to low: ','\t'.join(snum[::-1]))
