#!/usr/bin/env python
'''
杨辉三角-使用两行打印杨辉三角
'''


n = 6
oldline = []
for i in range(1, n+1):
    newline = [1] * i
    for j in range(2, i):
        newline[j - 1] = oldline[i-j-1] + oldline[i - j]

    oldline = newline
    print(newline)
