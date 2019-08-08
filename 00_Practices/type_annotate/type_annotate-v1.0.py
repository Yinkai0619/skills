#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/7/26 下午8:54
'''

import inspect


def check(fn):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)  # 拿到签名
        # print(sig)

        params = sig.parameters
        print(params)

        values = list(params.values())
        flag = True
        for i, x in enumerate(args):
            param: Parameter = values[i]
            if param.annotation != inspect._empty and not isinstance(x, param.annotation):
                print(x, ': invalid type!')
                flag = False
                break
            else:
                print(param.name, ': OK!')
        # for i, (k, param) in enumerate(params.items()):
        #     print(i, k, param)
        #     print(type(param))
        #     print(param.name, param.default, param.annotation, param.kind)

        for k, v in kwargs.items():
            param: Parameter = params[k]
            if param.annotation != param.empty and not isinstance(v, param.annotation):
                print(x, ': invalid type!!')
                flag = False
                break
            else:
                print(k, ': OK!!')

        if not flag:
            raise TypeError('Filed!!!')
        ret = fn(*args, **kwargs)
        return ret

    return wrapper


@check  # add = check(add)(x, y) = wrapper(x, y)
def add(x, y: str) -> str:
    return x + y


# print(add(4, 5))
print(add('4', '5'))
# print(add(y='4', x='5'))
# print(add(y=4, x=5))
