#!/usr/bin/env python

'''
字符串重复统计：
    1.字符表[a-z]
    2.随机挑选2个字母组成字符串，共挑选100个；
    3.降序输出所有不同的字符串及重复的次数。
'''

import string
import random

strs = string.ascii_lowercase

def string_print(strs=strs):
    alpha_dict = dict()
    for i in range(len(strs)):
        alpha_dict.setdefault(strs[i],i)
    return alpha_dict



print(string_print())
