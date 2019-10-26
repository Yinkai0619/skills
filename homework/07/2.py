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

text='foo = 23 + 42 * 10'

def serializing(text: str = text) -> list:
    tokens = list()
    name_regex = re.compile('^[a-z]+', re.S)
    num_regex = re.compile('\d+', re.S)

    for num in num_regex.findall(text):
        tokens.append(('NUM', num))

    return tokens

print(serializing())

