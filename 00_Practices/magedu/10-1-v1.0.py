from pathlib import Path
import argparse
import datetime
import stat

def listdir(path='.',all=False, detail=False,human=False):
    '''
        def convert_mode(mode:int):
        modelist = ['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
        modestr = bin(mode)[-9:]
        ret = ""
        for i, c in enumerate(modestr):
        if c == '1':
        ret += modelist[i]
        else:
        ret += '-'
        return ret

        def convert_type(file:Path):
        ret = ""
        if file.is_symlink():
        ret = 's'
        elif file.is_fifo():
        ret = 'p'
        elif file.is_dir():
        ret = 'd'
        elif file.is_socket():
        ret = 's'
        else:
        ret = '-'
        return ret
        '''

    def _get_human(size:int):
        units = " KMGTP"
        depth = 0

        while size >= 1024:
            size = size / 1024
            depth += 1

        return "{:.1f}{}".format(size,units[depth])

    def _showdir(path='.',all=False, detail=False,human=False):
        p = Path(path)
        for file in p.iterdir():
            if not all and str(file.name).startswith('.'):
                continue

            if detail:
                st = file.stat()

                size = st.st_size
                if human:
                    size = str(_get_human(st.st_size))

                yield (stat.filemode(st.st_mode), st.st_nlink, file.owner(),file.group(), size,
                       datetime.datetime.fromtimestamp(st.st_atime).strftime( '%Y-%m-%d %H:%M:%S' ), file.name)
            else:
                yield (file.name,)
    yield from sorted(_showdir(args.path,args.all,args.l,args.h), key=lambda x: x[len(x)-1])

parser = argparse.ArgumentParser(prog='ls',add_help=False,description='List all files.')
parser.add_argument('path',nargs='?',default='.',help='Path Help.')
parser.add_argument('-l',action='store_true')
parser.add_argument('-h',action='store_true',help='List the help')
parser.add_argument('-a', '--all',action='store_true',help='All files')

if __name__ == '__main__':
    args = parser.parse_args()
    # parser.print_help()
    print('args = ',args)

    for st in listdir(args.path, args.all, args.l, args.h):
        print(st)

