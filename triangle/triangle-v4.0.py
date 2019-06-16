#!/usr/bin/env python
'''
杨辉三角-优化空间复杂度(用一个列表，接合对称法)
'''

n = 5
row = [1] * n
for i in range(n):
    offset = n - 1
    z = row[1]
    for j in range(1, i // 2 + 1):
        val = z + row[j]
        row[j] = val
        if i != 2 * j:
            row[-j-offset] = val
            # row[-j-z] = val
    print(row[:i+1])


# Undone!