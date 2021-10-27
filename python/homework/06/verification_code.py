#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/4 下午5:12
'''

'''
随机生成100个验证码，每个验证码由6个元素构成:
1 要求使用random模块
2 验证码由字母和数字构成
3 要求验证码中的每个元素为一种颜色
提示 颜色可以用数字来表示:一般都是3个 (0, 255)之间的数字来构成的
demo:
Z (19, 157, 229)
2 (239, 10, 145)
Z (145, 142, 244)
M (231, 58, 7)
T (202, 19, 72)
F (182, 136, 237)
要求生成 png 或者jpg 格式的图片，关于如何生成图片 请搜索下python PIL生成图片
'''

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 验证码生成器
def verification_code_generator():
    code = []
    def random_num():
        return chr(random.randint(48, 57))

    def random_char():
        return chr(random.randint(65, 90))

    n = random.randint(1, 5)    # 字母和数字的数量随机匹配
    for i in range(n):
        code.append(random_char())
    for i in range(6 - n):
        code.append(random_num())
    random.shuffle(code)        # 随机打乱验证顺序
    return ''.join(code)

# 随机颜色
def random_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 定义验证码字体
font = ImageFont.truetype('arial.ttf', 36)

# 定义验证码大小
width = 60 * 6
height = 60


for _ in range(5):  # 验证码数量
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for x in range(width):  # 使用随机颜色填充验证码背景
        for y in range(height):
            draw.point((x, y), fill=random_color())

    code = verification_code_generator()
    print(code)
    length = len(code)

    for i in range(length):     # 对验证号每位字符随机着色
        draw.text((60 * i + 20, 10), code[i], fill=random_color(), font=font)

    image.save('verification_codes/code_{}.jpg'.format(code), 'jpeg')
    # image.show()
    image.close()
