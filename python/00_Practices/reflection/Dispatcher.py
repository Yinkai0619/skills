class Dispatcher:
    def __init__(self) -> None:
        pass

    def reg(self, name, fn):
        setattr(self, name, fn)

    def run(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit':
                break

            getattr(self, cmd, lambda self: print("Unknown Cmd: {}".format(cmd)))()



if __name__ == "__main__":
    dis = Dispatcher()
    dis.reg('ls', lambda : print('ls'))

    dis.run()