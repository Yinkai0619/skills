#!/usr/bin/env python

# 只计算一次，减少计算次数

def show(num=12, direction=True):
    tail = ' '.join([str(j) for j in range(num, 0, -1)])
    width = len(tail)
    if direction:
        for i in range(width, 0 ,-1):
            if tail[i - 1] == ' ':
                print(' ' * (i - 1), tail[i:])
        # for i in range(-1, -width-1,-1):
        #     if tail[i] == ' ':
        #         print(' ' * (width + i), tail[i + 1:])
        print(tail)
    else:
        print(tail)
        for i in range(width):
            if tail[i] == ' ':
                print(' ' * i, tail[i + 1:])


show(direction=True)
# show(direction=False)
