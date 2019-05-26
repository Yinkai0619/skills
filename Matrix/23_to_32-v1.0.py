#!/usr/bin/env python

matrix = [[1,2,3],[4,5,6]]
res = []

print(matrix)
for row in matrix: #[1,2,3]
    for i,col in enumerate(row):
        if len(res) < i + 1:  
            res.append([])
        res[i].append(col)
print(res)
