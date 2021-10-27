#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/6/29 下午5:09
'''

'''
s = "Sorting1234" -> ginortS1324 ()
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面 
'''

# ASCII: 数字 < 大写字母 < 小写字母

def str_sort(string):
    upper_str_list = []
    lower_str_list = []
    int_list = []
    status = True
    for s in string:  # 分离大小写字符串与数字
        if ord(s) in range(48, 58):
            int_list.append(int(s))
        elif ord(s) in range(65, 91):
            upper_str_list.append(s)
        elif ord(s) in range(97, 123):
            lower_str_list.append(s)
        else:
            status = False
            break
    if status:
        result = ''.join(sorted(lower_str_list) + sorted(upper_str_list)  + sorted([str(i) for i in int_list if i % 2]) + sorted([str(i) for i in int_list if not i % 2]))
        result_info = 'OK.'
    else:
        result = None
        result_info = 'Invalid string!'

    return result, result_info

s = "Sorting1234"
sort_result, sort_status = str_sort(s)
print('Init string: {2}\nSorting status: {1}\nSorting result: {0}'.format(sort_result, sort_status, s))
