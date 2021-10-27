#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/17 下午3:58
'''

'''
核心算法：
    1. 在base63编码表查找给定的字符，找到后返回对应的索引值（int类型）；
    2. 索引值不会大于6bit。索引值左移指定位数（6 × [0, 1, 2, 3]），4 × 6bit变3 × 8bit；
    3. 二进制移位后，按位相加，得出24bit bytes；
    4. 24bit分割成3个bytes，再根据ASCII表转换成str。
    
Example：
    解码“a”时，二进制移位:
a -> YQ==
    Y: 24 -> 0001 1000
    Q: 16 -> 0001 0000

==QY
    00000000 00000000 00000000  # 24bit空间
        0001 0000               # b'Q'的索引值左移6 * 2位
    011000                      # b'Y'的索引值左移6 * 3位
'''

import base64_encode

alphatab = base64_encode.get_alphabet()
alphabet = dict(zip(alphatab, range(64)))


def base64_decode(s: bytes):
    if isinstance(s, str):
        s = s.encode()
    elif isinstance(s, bytes):
        pass
    else:
        return '{} type error!'.format(s)

    target = bytearray()
    length = len(s)
    if length % 4:      # base64编码后的字符串一定是4的倍数，否则，不是有效的base64编码，直接退出
        return
    step = 4
    for offset in range(0, length, step):
        block = s[offset:offset + step]     # 每次取4个base64编码
        temp = 0
        # for i, c in enumerate(reversed(block)):     # 为方便计算，反响取值， a -> '==QY'
        #     index = alphabet.find(c)
        #     if index > -1:   # 在base64编码表中找到了编号后的字符
        #         temp += index << 6 * i  # temp: int, 24bit, 3byte
        for i in range(step):
            c = block[-1 - i]
            index = alphabet.get(c)
            if index:
                temp += index << (6 * i)
        target.extend(temp.to_bytes(3, 'big'))
    # return bytes(target.rstrip(b'\x00'))
    return (target.rstrip(b'\x00')).decode()

if __name__ == '__main__':

    import base64
    encodes = base64.b64encode('abc中国'.encode())
    decodes = base64_decode(encodes)
    print(decodes)
