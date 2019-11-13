import random
import re

'''
获取200个激活码，格式：xxxxx-xxxxx-xxxxx-xxxxx
'''

def get_code1():
    chars = [str(n) for n in range(10)] + [chr(c) for c in range(65,91)]
    ret = list()
    for _ in range(4):
        ret.append(''.join(random.sample(chars, k=5)))
    yield '-'.join(ret)

def get_code2():
    chars = [str(n) for n in range(10)] + [chr(c) for c in range(65,91)]
    random.shuffle(chars)
    chars = ''.join(chars)
    regex = re.compile(r'.{5}', re.S)
    ret = regex.findall(chars)
    yield '-'.join(ret[:4])

if __name__ == '__main__':
    for _ in range(200):
        print(next(get_code1()))

