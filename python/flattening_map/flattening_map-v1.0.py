#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/8 16:54
'''

# 扁平化字典
# {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}} -> {'a.b': 1, 'a.c': 2, 'd.e': 3, 'd.f.g': 4}

source_list = [{'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}, {'a': {'b': 1, 'c': 2}}]
source = source_list[0]

# recursion
def flat_map1(src: dict = source):
    target = {}

    def _flat_map(src: dict, prefix=''):
        for k, v in src.items():
            if isinstance(v, (list, tuple, set, dict)):
                _flat_map(v, prefix=prefix + k + '.')
            else:
                target[prefix + k] = v
        return target

    _flat_map(src)
    return target

def flat_map2(src: dict = source, target = None, prefix=''):
    if target == None:
        target = {}
    for k, v in src.items():
        if isinstance(v, (tuple, dict, set, list)):
            flat_map2(v, target, prefix=prefix + k + '.')
        else:
            target[prefix + k] = v
    return target


def flat_map3(src: dict):
    def _flat_map(src: dict, target = None, prefix=''):
        if target is None:
            target = {}
        for k, v in src.items():
            if isinstance(v, (tuple, dict, set, list)):
                _flat_map(v, target, prefix=prefix + k + '.')
            else:
                target[prefix + k] = v
        return target
    return _flat_map(src)


print(source)
print(flat_map3(source))
