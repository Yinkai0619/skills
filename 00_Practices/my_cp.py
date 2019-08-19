#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/19 16:40
'''


filename1 = 'sample.txt'
filename2 = 'sample2.txt'

# length = 16 * 1024
# with open(filename1, 'br') as f1:
#     with open(filename2, mode='bw') as f2:
#         for line in f1:
#             buf = f1.read(length)
#             if not buf:
#                 break
#             f2.write(buf)
def copy(src, dst, buffer=16*1024):
    with open(src, 'br') as sf:
        with open(dst, 'bw') as df:
            df.write(sf.read(buffer))

copy(filename1, filename2)


