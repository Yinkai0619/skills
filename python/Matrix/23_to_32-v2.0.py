#!/usr/bin/env python

matrix = [[1,2,3],[4,5,6]]
res = [[0 for _ in range(2)] for _ in range(3)]

print(matrix)
for i in range(len(res)): # 0,1,2
    for j in range(len(res[0])):
        res[i][j] = matrix[j][i]

print(res)
