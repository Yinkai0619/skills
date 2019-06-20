#!/usr/bin/env python
'''
杨辉三角-对称解法
'''

triangle = [[1], [1, 1]]
n = 6
for i in range(2, n):
    pre = triangle[-1]
    cur = [1] * (i + 1)

    for j in range(i // 2):
        val = pre[j] + pre[j + 1]
        cur[j + 1] = val
        if i != 2j:
            cur[-j-2] = val

    triangle.append(cur)

print(triangle)






