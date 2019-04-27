#!/usr/bin/env python

n = 9
for i in range(-(n//2),(n//2)+1):
    if i < 0:
        sn = -i
        rn = n - sn * 2
        print(' ' * sn + '*' * rn + ' ' * sn )
    elif i == 0:
        print('*' * n)
    else:
        rn = n - i * 2
        print(' ' * i + '*' * rn + ' ' * i )

