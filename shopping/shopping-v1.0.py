#!/usr/bin/env python3

class color:
    RED = 0
    BLUE = 1
    GREEN = 2
    GOLDEN = 3
    BLACK = 4
    OTHER = 1000

class Item:
    def __init__(self, id, mark, type, price, **kwargs):
        self.id = id
        self.price = price
        self.type = type
        self.mark = mark
        # self.__spec = kwargs
        self.__dict__.update(kwargs)
        
    # def __repr__(self):
    #     return '<Item: {} {}>'.format(self.mark, self.color)


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item:Item):
        self.items.append(item)

    def get_all_items(self):
        return self.items

cart = Cart()
item1 = Item(1, 'Audi', 'c001', '20', color=color.RED, weight=2)
item2 = Item(2, 'Hero', 'p001', '2', color=color.GREEN)
# print(item.__dict__)
# print(item.color)
# print(item)
cart.add_item(item1)
cart.add_item(item2)

print(cart.get_all_items())
print(item1.__dict__,'\n', item2.__dict__)