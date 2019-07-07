'''
猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。
第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
到第十天早上想吃时，只剩下一个桃子了。求第一天共摘多少个桃子。
'''


def peach1(days=10):
    if days == 1:
        return 1
    return (peach(days - 1) + 1) * 2

def peach2(days=1):
    if days == 10:
        return 1
    return (peach2(days + 1) + 1) * 2

print(peach2())
