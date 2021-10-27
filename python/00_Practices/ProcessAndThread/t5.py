#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2021/1/3 下午5:12
'''

import threading

X = "abc"
ctx = threading.local()
ctx.x = 123

print(ctx, type(ctx), ctx.x)


def worker():
    print(X)
    print(ctx)
    print(ctx.x)
    print("working")


worker()
# threading.Thread(target=worker).start()
