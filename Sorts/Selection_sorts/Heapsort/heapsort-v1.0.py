#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/9/12 10:11
'''

import math
import random
import print_tree


'''
核心算法：
    对于堆排序的核心算法就是堆结点的调整
    1. 度数为2的结点A，如果它的左右孩子结点的最大值比它大，则将这个最大值和该结点交换；
    2. 度数为1的结点A，如果它的左孩子的值大于它，则交换；
    3. 如果结点A被交换到新的位置，还需要和其孩子结点重复上面的过程。
'''

# 构建待排序元素：
# origin = [x * 10 for x in range(1, 10)]
# random.shuffle(origin)
# origin.insert(0, 0)
origin = [0, 10, 20, 90, 80, 50, 60, 40, 30, 70]    # 为了能和编码对应，增加一个无用的0在首位
print(origin)
print_tree.print_tree(origin, True)

total = len(origin) - 1

def heap_adjust(n, i, array: list):
    '''
    调整当前结点（核心算法）
    :param n:
    :param i:
    :param array:
    :return:
    '''