#!/usr/bin/env python
'''
杨辉三角-基本解法
'''

triangle = [[1]]
n = 10
for i in range(1, n):
    pre = triangle[-1]
    cur = [1]
    for j in range(len(triangle)-1):
        cur.append(pre[j] + pre[j + 1])
    cur.append(1)
    triangle.append(cur)
print(triangle)


#       1,      2,         3,            4,               5
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]





