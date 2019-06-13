#!/usr/bin/env python
'''
杨辉三角-对称解法
'''

triangle = [[1]]
n = 3
for i in range(1, n):
    pre = triangle[-1]
    cur = [1]
    for j in range(len(triangle)-1):        # 计算中间值
        cur.append(pre[j] + pre[j + 1])

    if not len(cur) % 2:    # 当前行为奇数行
        pass
    else:                   # 当前行为偶数行
        for y in range(1, len(cur)):
            cur.append(cur-[y])

    triangle.append(cur)
print(triangle)


#       1,      2,         3,            4,               5                     6                         7                             8                                 9
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]





