#!/usr/bin/env python

def show(num=12, direction=True):
    tail = ' '.join([str(j) for j in range(num, 0, -1)])
    width = len(tail)

    if direction:
        for i in range(1, num):
            print("{:>{}}".format(' '.join([str(j) for j in range(i, 0, -1)]), width))
        print(tail)
    else:
        print(tail)
        for i in range(width):
            if tail[i] == ' ':
                print(' ' * i, tail[i + 1:])


show(11, True)
