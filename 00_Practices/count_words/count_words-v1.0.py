#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/19 14:38
'''
# import copy

target = {}
with open('sample.txt', 'r', encoding='utf-8', newline='\r\n') as f:
    line_num = 0
    for line in f:
        # print(line)
        words = line.split()
        # print(words)
        for word in words:
            target[word] = target.setdefault(word, 1) + 1

# print(target['the'])
print(target)

max_value = 0
top_words = {}
for k, v in target.items():
    if v > 0:

    print(k,v)





