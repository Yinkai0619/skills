#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/19 14:38
'''
from collections import defaultdict

filename = 'sample.txt'
count = 0
d = defaultdict(lambda :0)
with open(filename, mode='r', encoding='utf-8') as f:
    for line in f:
        count += 1
        # print(line)

        words = line.split()
        for word in words:
            d[word] += 1

        # if count == 5: break
# print(d)
# print(sorted(d.items(), key=lambda k: k[1], reverse=True))

# os.path.commonprefix(list)
for k in d.keys():
    if k.find('path') > -1:
        print(k)