#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/2/27 下午10:10
'''

class Node:
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return '<{} <-- {} --> {}>'.format(
            self.prev.item if self.prev else 'None',
            self.item,
            self.next.item if self.next else 'None')

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []     # 用列表辅助随机查询，元素与链表元素保持一致。因为要维护两个数据结构，且需要保持一致，整体性能取决于慢的一个(如list.insert())，所以实际应用中不应该使用。

    def __len__(self):
        return len(self.items)

    def append(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
            # self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            # self.tail = node
        self.tail = node

        self.items.append(node)
        return self

    def get(self, index, reverse=False):
        current = self.head if not reverse else self.tail
        count = 0
        while count < index:
            current = current.next if not reverse else current.prev
            # print(count, current)
            count += 1
        return current

    def insert(self, index, value):
        if index < 0:       # 不支持负索引
            raise IndexError('Negative index error {}'.format(index))

        current = None
        # 遍历链表，当链表为空或index超界时直接在尾部追加
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:
            self.append(value)
            return

        prev = current.prev
        node = Node(value)  # 待插入节点对象

        if index == 0: # 当插入点在开始处时
            # node.next = current
            # current.prev = node
            self.head = node
        else:   # 当插入点在中间时
            # node.next = current
            # current.prev = node
            node.prev = prev
            prev.next = node
        node.next = current
        current.prev = node

        self.items.insert(index, node)

    def pop(self):
        if self.tail == None:   # 链表为空时
            raise   Exception('Empty linked list.')

        node = self.tail
        item = node.item
        prev = node.prev

        if prev == None:    # 链表中只有一个node
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev
        self.items.pop()
        return item

    def remove(self, index):
        if index < 0:       # 不支持负索引
            raise IndexError('Negative index error {}'.format(index))

        # 全空链表
        if self.head is None:
            raise Exception('Empty linked list.')

        current = None
        # 遍历链表
        for i, node in enumerate(self.iternodes()):
            if i == index:  # 已找到并定位要移除的node
                current = node  # current指向当前node
                break
        else:   # 索引超界
            raise IndexError('Wrong index.')

        prev = current.prev
        next = current.next

        # 移除定位到的node，分四种情况
        if prev is None and next is None:     # 链表只有一个node
            self.head = None
            self.tail = None
        elif prev is None:                  # 链表中有多个node，且待移除node处于头部
            self.head = next
            next.prev = None
        elif next is None:                  # 链表中有多个node，且待移除node处于尾部
            self.tail = prev
            prev.next = None
        else:                               # 链表中有多个node，且待移除node处于中间
            prev.next = next
            next.prev = prev

        self.items.pop(index)

    def iternodes(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def __iter__(self):
        return iter(self.items)
        # yield from self.items
        # yield from self.iternodes()
        # return self.iternodes()

    def __getitem__(self, index):
        return self.items(index)

    def __setitem__(self, index, value):
        node = self.items[index]
        node.item = value


ll = LinkedList()
ll.append('a')
ll.append('b').append('c').append('d')
ll.insert(0,'head')
ll.insert(100,'tail')
ll.insert(2,'mid')
# for x in ll.iternodes(reverse=False):
#     print(x)
print(list(ll.iternodes()))
# ll.pop()
ll.remove(0)
print(list(ll.iternodes()))
