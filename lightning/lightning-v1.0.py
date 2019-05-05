#!/usr/bin/env python

for i in range(-3,4):
    if i < 0:
        n = 4 + i
        print('{:>4}'.format('*' * n))
    elif i == 0:
        print('{:^}'.format('*' * 7))
    else:
        n = 4 - i
        print('{}{:<4}'.format(' ' * 3,'*' * n)) 
