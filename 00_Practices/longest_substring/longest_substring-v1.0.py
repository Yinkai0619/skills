#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/12 16:38
'''

def findit(str1: str, str2: str) -> str:
    length1 = len(str1)
    length2 = len(str2)

    matrix = list([0] * length1 for _ in range(length2))
    # matrix = list([[0] * length1] * length2)
    # print(matrix)
    xmax = 0
    xindex = 0
    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            if x == y:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1

                if matrix[i][j] > xmax:
                    xmax = matrix[i][j]
                    xindex = j
            else:
                pass
    start = xindex + 1 - xmax
    end = xindex + 1
    print('matrix: {}\nxmax: {}\txindex: {}\tstart: {}\tend: {}\n'.format(matrix, xmax, xindex, start, end))
    return str2[start:end]

s1 = 'abcdefg'
s2 = 'defgabc'

# s1 = 'abc'
# s2 = 'bc'



print(findit(s1, s2))
