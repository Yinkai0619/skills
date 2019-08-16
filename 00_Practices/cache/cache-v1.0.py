#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/14 14:11
'''


from functools import wraps
import inspect
import time
import datetime

def logger(fn):
    '''
    计算被装饰函数的运行时长（单位：秒）

    :param fn:
    :return:
    '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)
        return ret
    return wrapper

def cache(duration=5):      # duration为缓存条目过期时长
    def _cache(fn):
        local_cache = {}    # 缓存字典，将所有实参组合为一个有序tuple作为dict的key，函数运行结果为value。对不同函数名是不同的cache。
        @wraps(fn)
        def wrapper(*args, **kwargs):   # 接收各种参数
            def _clear_expire():
                '''
                清除过期缓存
                :return:
                '''
                expire_keys = []
                for k, (_, stamp) in local_cache.items():
                    if datetime.datetime.now().timestamp() - stamp > duration:
                        expire_keys.append(k)
                for k in expire_keys:
                    expire_keys.pop(k)

            def _make_key(args, kwargs):
                # 参数处理，构建key
                sig = inspect.signature(fn)
                params = sig.parameters
                params_dict = {}
                # print('args: {}\nkwagrs: {}\n'.format(args, kwargs))
                # print('item: {}\nkeys: {}\nvalues: {}\n'.format(params.items(), params.keys(), params.values()))
                params_dict.update(zip(params.keys(), args))  # 处理位置传参
                params_dict.update(kwargs)  # 处理关键字传参
                for k, v in params.items():  # 处理默认参数传参
                    if k not in params_dict:
                        # print('\n', v.name, v.default, v.annotation, v.kind, '\n')
                        params_dict[k] = v.default
                # print(params, '\n', params_dict)
                key = tuple(sorted(params_dict.items()))
                # print(key)
                return key

            _clear_expire()
            key = _make_key(args, kwargs)
            if key not in local_cache.keys():
                local_cache[key] = fn(*args, **kwargs), datetime.datetime.now().timestamp()
            return local_cache[key][0]
        return wrapper
    return _cache

@logger     # 装饰器执行过程：由低向上
@cache(10)
def add(x, y, z=6):
    time.sleep(1)
    return x + y + z

print(add(4, 5))
print(add(4, y=5))
print(add(4, 5, 6))
print(add(y=5, x=4))
print(add(x=4, y=5))

