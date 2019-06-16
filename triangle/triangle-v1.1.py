#!/usr/bin/env python

#!/usr/bin/env python

'''
杨辉三角基本解法
'''


triangle = [[1]]
n = 6
for i in range(1,n):
    pre = triangle[i-1]
    cur = [1]
    for j in range(i-1):  # 计算中间值
        cur.append(pre[j] + pre[j + 1])
    cur.append(1)
    triangle.append(cur)
print(triangle)
