#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/9/7 下午4:43
'''

'''
打印一个完全二叉树，如下：

              1                 
      2               3         
  4       5       6       7     
8   9   10 

'''

import math


def print_tree1(array):
    '''
    居中对齐方案, 逐个打印array中的元素
    :param array:
    :return:
    '''
    unit_width = len(str(array[-1]))  # 取最大元素的宽度作为单位宽度
    length = len(array)
    depth = math.ceil(math.log2(length + 1))  # 二叉树的深度（二叉树性质4）：具有n个结点的完全二叉树的深度为: math.ceil(math.log2(n))+1
    index = 0
    width = 2 ** depth - 1  # 满二叉树的宽度（作为第一行的宽度数居中打印元素）。
                            # 从上往下用投影的方法观察満二叉树时，各栅格（结点位置）互不重叠，且栅格数量等于满二叉树的结点总数。
                            # 满二叉树的结点数量为（二叉树性质2）: 2 ** depth(二叉树的深度) - 1

    for i in range(depth):  # 二叉树的行
        for j in range(2 ** i):  # 计数：j来控制为每行元素的个数。0:1; 1:0,1; 2:0,1,2,3; 3:0,1,2,3,4,5,6,7
            print('{:^{}}'.format(array[index], width * unit_width), end=' ' * unit_width)  # 居中打印元素，最后补充一个单位数空格
            index += 1
            if index >= length:
                break
        width = width // 2
        print()


def print_tree2(array):
    '''
    投影栅格实现, 跳过array[0]中的元素
    :param array:
    :return:
    '''
    '''
    计算空格单位数量。此处以深度为4的满二叉树为示例说明：
    行  i  前空格       元素间空格
    1   3  7=2*3-1     0 2*4+1
    2   2  3=2*2-1     7=2*3+1
    3   1  1=2*1-1     3=2*1+1
    4   0  0=2*0-1     1=2*0+1 
    '''
    unit_width = len(str(max(array)))
    length = len(array)
    print('Length : ', length)
    index = 1   # 因为使用时前面补0了,不然应该是math.ceil(math.log2(len(array)+1))
    depth = math.ceil(math.log2(length))    # 二叉树的深度（二叉树性质4）：具有n个结点的完全二叉树的深度为: math.ceil(math.log2(n))+1，因为接收的参数中已经添加一个占位元素，所以无需再加1
    print('Depth : ', depth )
    sep = '-' * unit_width
    print('Sep: ', sep)

    for i in range(depth - 1, -1, -1):  # 二叉树层数（迭代上方注释中的i）
        pre = 2 ** i - 1    # 前空格数量
        print(sep * pre, end='')  # 打印前空格
        offset = 2 ** (depth - i - 1)
        line = array[index: index + offset]  # 取元素
        index += offset
        interval_space = sep * (2 * pre + 1)
        print(interval_space.join(map(str, line)))


if __name__ == '__main__':
    # print_tree1([x + 1 for x in range(10)])
    # print_tree1([30, 40, 50, 60, 70, 80, 90, 91, 93, 95, 97, 99, 100, 101, 102])
    print_tree2([0, 30, 40, 50, 60, 70, 80, 90, 91, 93, 95, 97, 99, 100, 101, 102])
    # print_tree2([0, 30, 40, 50, 60, 70, 80, 90, 91, 93, 95, 97, 99, 10, 10, 10])
