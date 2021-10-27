#!/usr/bin/env python

from collections import defaultdict
import re

'''
对sample文件进行不区分大小写的单词统计
要求用户可以排除一些单词的统计,例如a、the、of等不应该出现在具有实际意义的统计中,应当忽略
要求,全部代码使用函数封装、调用完成
'''


# 使用RE库
regex = re.compile('[^\w-]+', re.M)

def make_key(line: str):
    for word in regex.split(line):
        if len(word):
            yield word

def word_count(filename, encoding='utf8', ignore=set()):
    d = defaultdict(lambda: 0)
    with open(filename, encoding=encoding) as f:
        for line in f:
            for word in map(str.lower, make_key(line)):
                if word not in ignore:
                    d[word] += 1
    return d

def top(d:dict, n=10):
    for i, (k, v) in enumerate(sorted(d.items(), key=lambda item: item[1], reverse=True)):
        if i > n:
            break
        print(k,v)

top(word_count('sample.txt', ignore={'a', 'of', 'the', '\n'}))
