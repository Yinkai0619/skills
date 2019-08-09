#!/usr/bin/env python


# 扁平化字典
# {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}} -> {'a.b': 1, 'a.c': 2, 'd.e': 3, 'd.f.g': 4}

source_list = [{'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}, {'a': {'b': 1, 'c': 2}}]
source = source_list[0]

def flatmap1(src:dict):
    target = {}
    def flat_map(src: dict, prefix = ''):   # {'a': {'b': 1, 'c': 2}}
        for k, v in src.items():
            if isinstance(v, dict):
                prefix = prefix + k + '.'
                flat_map(v, prefix)  #{'b': 1, 'c': 2}   a.
                prefix = ''
            else:
                target[prefix + k] = v
    flat_map(src)
    return target


def flatmap2(src:dict): # {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}
    target = {}
    def flat_map(src: dict, prefix = ''):
        for k, v in src.items():    # {'a': {'b': 1, 'c': 2}}
            if isinstance(v, dict):
                prefix = prefix + k + '.'
                flat_map(v, prefix)  # 1   a.b
                prefix = ''
            else:
                target[prefix + k] = v
        return target
    return flat_map(src)

print(flatmap2(source)) # flat_map(src)
