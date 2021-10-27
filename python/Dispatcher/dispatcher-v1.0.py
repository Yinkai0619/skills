#!/usr/bin/env python

'''
Author: Li Yinkai
Email: yinkai.li@foxmail.com
Blog: https://blog.51cto.com/yinkai

Date: 2019/8/16 15:17
'''

def cmds_dispacher(default_fn=lambda : print('Unknown command.')):
    commands = {}

    def reg(cmd):
        def _reg(fn):
            if cmd in commands.keys():
                print('{} already existed.'.format(cmd))
                return
            commands[cmd] = fn
            return fn
        return _reg

    # def default_fn():
    #     print('Unknown command.')

    def dispatcher():
        while True:
            cmd = input('>>>').strip()
            if cmd == '' or cmd == 'quit':
                print('Byebye.')
                break
            commands.get(cmd, default_fn)()

    return reg, dispatcher

reg, run = cmds_dispacher()

@reg('fo1')     # fool1 = reg('fo1')(foo1) = _reg(foo1) = foo1
def foo1():
    print('foo1 function.')

@reg('fo1')
def foo2():
    print('foo2 function.')

if __name__ == '__main__':
    run()

