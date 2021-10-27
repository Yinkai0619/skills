#!/usr/bin/env python

n = 9
for i in range(-(n//2),(n//2)+1):
    if i < 0:
        rn = -i * 2 + 1
        sn = (n - rn) // 2
        print(' ' * sn + '*' * rn + ' ' * sn )
    elif i == 0:
        sn = n//2
        rn = n - sn * 2
        print(' ' * sn + '*' * rn + ' ' * sn )
    else:
        rn += 2
        sn = (n - rn) // 2
        print(' ' * sn + '*' * rn + ' ' * sn )
