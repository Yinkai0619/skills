#!/usr/bin/env python

'''
杨辉三角基本解法
'''


triangle = [[1],[1,1]]  # 定义前两行
n = 6
for i in range(2,n):  # 后四行
    pre = triangle[i-1]     # 前一行
    cur = [1]       # 当前行
    for j in range(i-1):  # 计算中间值
        cur.append(pre[j] + pre[j + 1])
    cur.append(1)
    triangle.append(cur)
print(triangle)
