#/usr/bin/env python

import random
import string

'''
生成100个ID；
    ID格式：0001.rmfbgzkojl
    前部分为4位数的整数，后半部分为10为随机字母，中间用“.”分割。
'''

[ "{:0>4d}.{}".format(x,''.join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)]))  for x in range(1,101)]

[ "{:0>4d}.{}".format(x,''.join(random.choices(bytes(range(97,123)).decode(),k=10))) for x in range(1,101)]

