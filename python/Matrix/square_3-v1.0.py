#!/usr/bin/env python

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i < j:
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]              
print(matrix)



'''
0.0  0.1  0.2
1.0  1.1  1.2
2.0  2.1  2.2
'''
