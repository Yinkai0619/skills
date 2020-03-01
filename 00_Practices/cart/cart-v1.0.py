#!/usr/bin/env python

class Cart:
    def __init__(self):
        self.__items = []

    def additem(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __iter__(self):
        #return iter(self.__items)
        yield from self.__items

    def __getitem__(self, index):
        print('Index: {}'.format(index))
        return self.__items[index]

    def __setitem__(self, index, value):
        self.__items[index] = value

    def __add__(self, other):
        self.__items.append(other)
        return self

cart = Cart()
cart.additem(1)
cart.additem(2)
cart.additem('abc')

cart[1] = 'b'

cart + 'd' + 'e'

print(list(cart))

print('Len: ',len(cart))

#print(type(cart))
#for x in cart:
#    print(x)

#print(cart[2])
#print(1 in cart)
