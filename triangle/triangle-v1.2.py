#!/usr/bin/env python

#!/usr/bin/env python

'''
杨辉三角基本解法
'''


triangle = []
n = 6
for i in range(n):          # 0, 1, 2, 3
    cur = [1]               # [ [1], [1,1], [1,2,1], [1,3,3,1] ]
    triangle.append(cur)
    for j in range(i-1):  # 计算中间值
        cur.append(triangle[i-1][j] + triangle[i-1][j + 1])
    if i > 0:
        cur.append(1)
print(triangle)
