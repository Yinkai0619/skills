#!/usr/bin/env python

'''
字符串重复统计：
    1.字符表[a-z]
    2.随机挑选2个字母组成字符串，共挑选100个；
    3.降序输出所有不同的字符串及重复的次数。
'''

# import string
import random

# strs = string.ascii_lowercase
#
# def gen_string(strs=strs):
#     alpha_dict = dict()
#     ds = {}
#     counter = {}
#     for i in range(len(strs)):
#         alpha_dict.setdefault(i,strs[i])
#
#     for j in range(100):
#         s1 = alpha_dict[random.randint(0,len(alpha_dict.items())-1)]
#         s2 = alpha_dict[random.randint(0,len(alpha_dict.items())-1)]
#         ds.setdefault(s1+s2,j)
#
#     for c in ds:
#         counter[c] = counter.get(c,0) + 1
#
#     print(ds)
#     print(*sorted(counter.items(),reverse=True))
#
# # print(gen_string())
# gen_string()
#使用ASCII码生成字母字符串
alpha = ''
for i in range(26):
    alpha += chr(97 + i)

words = [ (random.choice(alpha) + random.choice(alpha)) for _ in range(100)]

counter = {}
for word in words:
    counter[word] = counter.get(word,0) + 1


print(alpha)
print(words)
print(counter)
print(sorted(counter.items(),reverse=True))