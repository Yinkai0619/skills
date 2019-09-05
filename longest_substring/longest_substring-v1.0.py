#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/12 16:38
'''

def findit1(str1: str, str2: str) -> str:
    if len(str1) > len(str2):   # 当参与比较的字符串长度不一致时，保证str2为较长的字符串
        str1, str2 = str2, str1

    length1 = len(str1)
    length2 = len(str2)

    matrix = list([0] * length1 for _ in range(length2))
    xmax = 0
    xindex = 0

    for i, x in enumerate(str2):
        for j, y in enumerate(str1):
            if x == y:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1

                if matrix[i][j] > xmax:
                    xmax = matrix[i][j]
                    xindex = j

    start = xindex + 1 - xmax
    end = xindex + 1
    print(str1,'\t',str2)
    print('matrix: {}\nxmax: {}\txindex: {}\tstart: {}\tend: {}\n'.format(matrix, xmax, xindex, start, end))
    return str1[start:end]


def findit2(str1: str, str2: str) -> str:
    if len(str1) > len(str2):  # 当参与比较的字符串长度不一致时，保证: str2为较长的字符串
        str1, str2 = str2, str1

    length = len(str1)
    for sublen in range(length, 0, -1): # 对较短字符串进行切片，确定尾边界
        for start in range(0, length - sublen + 1): # 确定首边界
            substr = str1[start:start + sublen]
            print(substr)

            # if str2.find(substr) > -1:  # 如果在长字符串中找到被切隔的子串
            #     return substr

def findit(str):
    length = len(str)
    for end in range(length, 0 ,-1):
        for start in range(0, length - end + 1):
            ret = str[start:end]
            print(ret)

s1 = 'abcdefg'
s2 = 'defabcd'

# s1 = 'abcd'
# s2 = 'abc'

print(findit2(s1, s2))
# findit(s1)
