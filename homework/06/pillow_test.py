#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/3 15:09
'''

from PIL import Image

im = Image.open('test.jpg')

w, h = im.size

print(w,h)
