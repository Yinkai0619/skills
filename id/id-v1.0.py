import random
import string

'''
生成100个ID；
    ID格式：0001.rmfbgzkojl
    前部分为4位数的整数，后半部分为10为随机字母，中间用“.”分割。
'''

# s1 = string.ascii_lowercase
s2 = list(string.ascii_lowercase)

# print(s2)

for x in range(1,101):
    random.shuffle(s2)
    s3 = ''
    for i in range(10):
        s3 += s2[i]
    print('{:0>4d}.{}'.format(x,s3))
