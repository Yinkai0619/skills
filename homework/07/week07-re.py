#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/10/26 下午12:01
'''

'''
2.使用正则序列化。
    text = 'foo = 23 + 42 * 10' 
    将字符串像下面这样转换为序列对：
     tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'), ('NUM', '42'), 
                ('TIMES', '*'), ('NUM', '10')] 
'''
import re

def serializing(text: str) -> list:
    tokens = list()
    num_regex = re.compile('\d+', re.S)
    regex = re.compile('(?P<NAME>^[a-z]+).+(?P<EQ>=).+(?P<PLUS>\+).+(?P<TIMES>\*)', re.S)
    for value in regex.finditer(text):
        for v in value.groupdict().items():
            tokens.append(v)

    for num in num_regex.findall(text):
        tokens.append(('NUM', num))

    return tokens

if __name__ == '__main__':
    text='foo = 23 + 42 * 10'
    print(serializing(text))

