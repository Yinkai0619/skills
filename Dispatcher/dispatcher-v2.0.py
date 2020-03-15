#!/usr/bin/env python

class Dispatcher:
    def __init__(self):
        pass

    def reg(self, name, fn):
        if isinstance(name, str) and callable(fn):
             setattr(self, name, fn)
        else:
            raise ValueError('Invalid argument.')
            
    def run(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit' or cmd == '':
                break

            getattr(self, cmd, lambda self: print('Unknown command: {}'.format(cmd)))()


dis = Dispatcher()
dis.reg('ls', lambda : print('ls'))

dis.run()
