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

# 调整单棵子树
def heap_adjust(n, i, array: list):
    '''
    调整单棵子树（核心算法）

    调整的结点的起点在n//2，保证所有调整的结点都有孩子结点
    :param n: 待比较数个数
    :param i: 待比较（子）树的根结点的索引，也就是叶子结点的父结点
    :param array: 待排序数据
    :return: None
    '''
    while 2 * i <= n:   # 判断当前结点是否还有左孩子结点
        # 根据二叉树性质5，孩子结点判断：2i为左孩子，2i+1为右孩子
        lchild_index = 2 * i
        # 先假定左孩子为最大值
        max_child_index = lchild_index  # n=2i
        # 左右孩子值进行比较，当右孩子值大于左孩子值时，将最大值的索引标记为右孩子值的索引：
        if n > lchild_index and array[lchild_index + 1] > array[lchild_index]:  # 如果存在右孩子，且右孩子的值大于左孩子值，则最大值索引指向右孩子。n>2i时说明还有右孩子。
            max_child_index = lchild_index + 1  # n=2i+1

        # 与子树的根结点比较
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index # 被交换后，需要判断是否还需要调整
        else:
            break

        # print_tree.print_tree(array)
        # print('-'*50)

# 构建大顶堆（也称为大根堆）
def max_heap(total, array: list):
    '''
    构建大顶堆

    起点的选择: 从最下层最右边叶子结点的父结点开始
    :param total: 待排序元素个数:
    :param array: 待排序元素
    :return: 排序后的数据
    '''
    for i in range(total // 2, 0, -1):  # 按照二叉树性质5编号的结点,从起点开始找编号逐个递减的结点,直到编号1
        heap_adjust(total, i, array)
    return array

# 排序
def sort(total, array: list):
    '''
    思路:
        1. 每次都要让堆顶的元素和最后一个结点交换,然后排除最后一个元素,形成一个新的被破坏的堆。
        2. 让它重新调整,调整后,堆顶一定是最大的元素。
        3. 再次重复第1、2步直至剩余一个元素
    :param total:
    :param array:
    :return:
    '''
    while total > 1:
        array[1], array[total] = array[total], array[1] # 堆顶和最后一个结点互换
        total -= 1
        if total == 2 and array[total] >= array[total-1]:   # 当剩余2个元素，如果最后一个结点比堆顶大，则不再调整
            break
        heap_adjust(total, 1, array)
    return array

if __name__ == '__main__':
    # 构建待排序元素：
    # origin = [x * 10 for x in range(1, 10)]
    # random.shuffle(origin)
    # origin.insert(0, 0)
    origin = [0, 20, 10, 40, 70, 50, 60, 90, 30, 80]    # 为了能和二叉树编码一致，增加一个无用的占位值0在首位
    print(origin)
    print_tree.print_tree(origin, True)
    print('='*50)

    total = len(origin) - 1 # 初始待排序元素个数，即n

    print_tree.print_tree(sort(total, max_heap(total, origin)))
    print(origin)
