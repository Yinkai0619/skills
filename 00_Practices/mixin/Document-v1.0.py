'''
用继承方式实现打印功能
'''

class Document:
    def __init__(self, content):
        self.content = content
    
    def print(self):
        raise NotImplementedError

class Word(Document):pass
class Pdf(Document):pass

class PrintableWord(Word):
    def print(self):
        print('Word: ', self.content)

class PrintablePdf(Pdf):
    def print(self):
        print('Pdf: ', self.content)

pw = PrintableWord('test word')
pw.print()

pp = PrintablePdf('test pdf')
pp.print()