#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2020/2/27 下午10:10
'''

class Note:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return '<{} --> {}>'.format(self.item, self.next.item if self.next else 'None')

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        note = Note(item)

        if self.head is None:
            self.head = note
            # self.tail = note
        else:
            self.tail.next = note
            # self.tail = note
        self.tail = note
        return self

    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next


ll = LinkedList()
ll.append('a')
ll.append('b').append('c')

# for x in ll.iternodes():
#     print(x)
print(list(ll.iternodes()))
