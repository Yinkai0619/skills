#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/17 16:43
'''

import base64

def get_alphabet(encodeing : bool = False):
    if encodeing:
        return ''.join([chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)] + ['+', '/']).encode()
    else:
        return ''.join([chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)] + ['+', '/'])

alphabet = get_alphabet(True)

str_list = ['a', '`', 'ab', 'abc', 'abcd', 'Yinkai', 'Python', 'Li银凯']

def base64_encode(src: str):
    ret = bytearray()
    if isinstance(src, str):
        _src = src.encode()
    else:
        return

    length = len(_src)

    r = 0
    for offset in range(0, length, 3):  #
        triple = _src[offset:offset + 3]    # 取三位字符
        if offset + 3 > length:
            r = 3 - len(triple)
            triple += b'\x00' * r

        # print(triple, r)
        b = int.from_bytes(triple, 'big')
        # print(b, hex(b))
        for i in range(18, -1, -6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F
            ret.append(alphabet[index])

    if r:
        ret[-r:] = b'=' * r
    return bytes(ret)

# print(alphabet)

for x in str_list:
    # print(x)
    # print(base64.b64encode(x.encode()))
    print(base64_encode(x))
    print()