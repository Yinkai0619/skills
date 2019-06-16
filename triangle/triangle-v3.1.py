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

# i
#    1
#    1 1
# 2: 1 2 1   -2
# 3: 1 3 3 1    -1 -3
# 4: 1 4 6 4 1    -2 -4
# 5: 1 5 10 10 5 1    -1 -3 -5
# 6: 1 6 15 20 15 6 1    -2 -4 -6




