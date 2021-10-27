#!/usr/bin/env python

import bisect

origin = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51]
origin = sorted(origin)

for i, x in enumerate(origin):
    print(i, x)

l = bisect.bisect(origin, 40)
print(l)

l = bisect.bisect_left(origin, 40)
print(l)

l = bisect.bisect_right(origin, 40)
print(l)

print(origin)

bisect.insort(origin, 40)
print(origin)