#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/19 14:38
'''
from collections import defaultdict


# 分割字符串算法1
def make_key1(src: str, chars=set(r',."[]{}!@#$%^&*()_+=/\|`~;: ')):
    '''
    1. 将待处理的字符串中的特殊字符转换成空格；
    2. 使用空字符连接字符串后再进行分隔。
    :param src:
    :param chars: 特殊字符集合
    :return:
    '''
    src = src.lower()  # 不区分大小写
    target = list()
    for c in src:
        target.append(' ') if c in chars else target.append(c)
    return ''.join(target).split()


# 分割字符串算法2
def make_key2(src: str, chars=set(r',."[]{}!@#$%^&*()_+=/\|`~;: ')):
    '''
    将待处理的字符串用特殊字符进行切片，并返回
    :param src:
    :param chars: 特殊字符集合
    :return:
    '''
    # target = []
    # src = src.lower()
    length = len(src)
    start = 0
    for i, c in enumerate(src):
        if c in chars:
            if i != start:
                # target.append(src[start:i].lower())
                yield src[start:i]
            start = i + 1
    else:
        if start < length:
            # target.append(src[start:].lower())
            yield src[start:]
    # return target

def topn(n:int, filename):
    d = dict()
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            for word in map(str.lower, make_key2(line)):
                d[word] = d.get(word, 0) + 1
    count = 0
    for word in sorted(d.items(), key=lambda k: k[1], reverse=True):    # 依据字典中值（key=lambda k: k[1]）的顺序进行逆序排序
        if count >= n: break
        count += 1
        yield word
    # order_words = sorted(d.items(), key=lambda k: k[1], reverse=True)
    # return order_words[:n]


filename = 'sample.txt'
# print(topn(10, filename='sample.txt'))
for word in topn(10, filename='sample.txt'):
    print(word)
