#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/16 15:17
'''

from functools import partial

# 自定义函数可以有任意参数，可变参数、keyword-only除外
def cmds_dispacher():
    # 构建全局字典
    cmd_tbl = {}

    # 注册函数
    def reg(cmd, *args, **kwargs):
        def _reg(fn):
            if cmd in cmd_tbl.keys():
                print('{} already existed.'.format(cmd))
                return
            func = partial(fn, *args, **kwargs)
            cmd_tbl[cmd] = func
            return func
        return _reg

    # 缺省函数
    def default_func():
        print('Unknown command')

    # 调度器
    def dispatcher():
        while True:
            cmd = input('Please input cmd: ').strip()
            if cmd == '' or cmd == 'quit':
                print('Byebye.')
                return
            cmd_tbl.get(cmd, default_func)()

    return reg, dispatcher

if __name__ == '__main__':
    reg, run = cmds_dispacher()

    @reg('fo11', z=200, y=300, x=100)
    @reg('fo1', z=300, y=300, x=300)     # fool1 = reg('fo1', z=200, y=300, x=100)(foo1) = _reg(foo1) = foo1
    def foo1(x,y,z):
        print('foo1 function. Args: ', x, y, z)

    @reg('fo2', 300, b=400)
    def foo2(a, b=100):
        print('foo2 function. Args: ',  a, b)

    run()

