'''
用装饰器方式实现打印功能
'''

class Document:
    def __init__(self, content):
        self.content = content
    
    def print(self):
        raise NotImplementedError

class Word(Document):pass
class Pdf(Document):pass
class Txt(Document):pass

#######################################################################

def printable(cls):
    def _print(self):
        print('{}: {}'.format(cls.__name__, self.content))
    cls.print = _print
    return cls    

@printable      # PrintableWord = printable(PrintWord)
class PrintableWord(Word):
    pass
    # def print(self):
    #     print('Word: ', self.content)

@printable
class PrintablePdf(Pdf):
    pass
    # def print(self):
    #     print('Pdf: ', self.content)

class PrintableTxt(Txt):pass
PrintableTxt.print = lambda self: print('{}: {}'.format(type(self).__name__, self.content))

#######################################################################

pt = PrintableTxt('test txt')
pt.print()

pw = PrintableWord('test word')
pw.print()
# print(PrintableWord.__dict__)
# print(PrintableWord.mro())

pp = PrintablePdf('test pdf')
pp.print()
# print(type(pp).__dict__)