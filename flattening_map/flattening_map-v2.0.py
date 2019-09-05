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


def flat_map1(src: dict):
    target = {}
    def _flat_map(src: dict = src, prefix: str = ''):
        for k, v in src.items():     # k = 'a', v = {'b': 1, 'c': 2}
            if isinstance(v, dict): #
                _flat_map(v, prefix + k + '.')
            else:
                target[prefix + k] = v
        return target
    return _flat_map()

def flat_map2(src: dict):
    target = {}
    def _flat_map(src: dict = src, prefix=''):  # {'b': 1, 'c': 2}, a.
        for k, v in src.items():    # k=b, v=1
            if isinstance(v, dict):
                _flat_map(v, prefix + k + '.')  # {'b': 1, 'c': 2}, a.
            else:
                target[prefix + k] = v  # a.b=1
    _flat_map()
    return target

print(flat_map2(source))





