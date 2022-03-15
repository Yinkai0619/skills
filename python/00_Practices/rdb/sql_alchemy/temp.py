import random
import base64

from random import choice
import string

#生成随机密码
 
#python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters
 
# def GenPassword(length=8,chars=string.ascii_letters+string.digits):
#     return ''.join([choice(chars) for i in range(length)])
 
# if __name__=="__main__":
#     #生成10个随机密码    
#     for i in range(10):
#         #密码的长度为8
#         print(GenPassword(8))

# chars=string.ascii_letters+string.digits
# length=8
# print(string.ascii_letters)
# print(string.digits)
# print(chars)
# # print([choice(chars) for i in range(length)])
# cs=[choice(chars) for i in range(length)]
# print(cs)
# print(''.join(cs))

# pass = ''.join(string.ascii_letters+string.digits)
# print('')

# class PW:
#     def get_password(length=8, chars=string.ascii_letters+string.digits):
#         return ''.join([random.choice(chars) for i in range(length)])



# python2 不兼容，python3正常
import datetime,random, time
def randomtimes(start, end, frmt="%Y-%m-%d"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    date = random.random() * (etime - stime) + stime
    return date.strftime("%Y-%m-%d")

if __name__ == "__main__":
    # randomtimes('1980-01-01','1995-12-31',10)
    print(randomtimes('1980-01-01','1995-12-31'))


# dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
# print(dt.strftime("%Y-%m-%d %H:%M:%S"))
# print("{0:%Y}/{0:%m}/{0:%d} {0:%H}::{0:%M}::{0:%S}".format(dt))

# y = datetime.timedelta(days=365)
# print(y)

# st = datetime.datetime.now()
# ds = random.randint()
# print(ds)
# # td = st - datetime.timedelta(days=365*random()*10)
# print(st, type(st))
# # print(td, type(st))