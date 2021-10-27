#!/usr/bin/env python
'''
杨辉三角补0法
'''

triangle = [[1],[1,1]]
n = 6
for i in range(2,n):
    pre = triangle[i-1] + [0]
    cur = []
    for j in range(i+1):    # 计算当前行
        cur.append(pre[j-1] + pre[j])
    triangle.append(cur)
print(triangle)
