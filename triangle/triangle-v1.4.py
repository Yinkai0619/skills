#!/usr/bin/env python
'''
杨辉三角-优化空间复杂度
'''

n = 6
triangle = []
for i in range(n):
    row = [1]
    triangle.append(row)
    if not i: continue
    for j in range(i-1):
        row.append(triangle[i-1][j] + triangle[i-1][j + 1])
    row.append(1)

    # print(triangle)
print('\n'.join(map(str, triangle)))

