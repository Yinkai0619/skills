#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/17 16:43
'''

import base64

def get_alphabet(encodeing : bool = True):
    if encodeing:
        return ''.join([chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)] + [str(x) for x in range(10)] + ['+', '/']).encode()
    else:
        return ''.join([chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)] + [str(x) for x in range(10)] + ['+', '/'])


def base64_encode(src) -> bytearray:
    target = bytearray()
    if isinstance(src, str):
        src = bytearray(src.encode())
    elif isinstance(src, bytes):
        pass
    else:
        return '{} type error!'.format(src)

    length = len(src)
    r = 0   # 补齐3*8需要的byte个数
    for offset in range(0, length, 3):
        tripe = src[offset:offset + 3]
        if offset + 3 > length: # 是否为最后一次取数
            r = 3 - len(tripe)  #需要补充的byte个数
            tripe = tripe + b'\x00' * r     # 以ASCII中的0作为补充，以凑成3 × 8bit

        val = int.from_bytes(tripe, 'big')  # bytearray -> int

        for i in range(18, -1, -6): # 将24个bit转换成4段 X 6bit作为索引，并用索引分别查base64表取出对应的字符追加至目标中
            index = val >> i if i == 18 else val >> i & 0x3f

            target.append(alphabet[index])

        if r:   # 如果每次的取值有补充则使用‘=’替换之
            target[-r:] = b'=' * r

    return bytes(target)


alphabet = get_alphabet()

str_list = ['a', 'ab', 'abc', 'abcd', '`', 'Yinkai', 'Python', 'Li银凯']

# print(alphabet)
# print(len(alphabet))
for x in str_list:
    print(x)
    print(base64_encode(x))
    print(base64.b64encode(x.encode()))
    print()
# x='Yinkai'
# print(base64.b64encode(x.encode()))
# print(base64_encode(x))
