import os
import logging

os.system("clear")

logging.basicConfig(format="%(name)s %(asctime)s %(message)s", level=logging.INFO)  # 定义缺省logger的level和缺省handler的formater

root = logging.getLogger()  # 实例化一个logger对象，在实例时缺省添加一个级别为NOSET的handler
# print(root.getEffectiveLevel(),"~~~~~~")
# root.setLevel(logging.ERROR)    # 设置logger level
# print(root.getEffectiveLevel(),"~~~~~~")
print("root: ", root.handlers)

h0 = logging.StreamHandler()
h0.setLevel(logging.WARNING)    # 设置handler的level 
root.addHandler(h0)     # root logger中增加一个handler

print("root handlers: ", root.handlers)     # 打印root logger的所有handler

for h in root.handlers:
    print("root handler = {}, formatter = {}".format(h, h.formatter))   # 遍历root logger中的所有handler的信息

print(root.getEffectiveLevel())
logging.warning("test root info~~~~~~~~~~")

print("=" * 50)

log1 = logging.getLogger('s')
log1.setLevel(logging.ERROR)
fmt1 = logging.Formatter("log1: %(name)s %(lineno)d %(message)s")
h1 = logging.FileHandler("/tmp/log1.txt",'a')
h1.setLevel(logging.WARNING)    # 定义log1 handler的level
h1.setFormatter(fmt1)
log1.addHandler(h1)
print("log1 handlers: ", log1.handlers)


log2 = logging.getLogger("s.s1")
log2.setLevel(logging.CRITICAL)
fmt2 = logging.Formatter("log2: %(name)s %(lineno)d %(message)s")   # 定义h2的显示格式
h2 = logging.FileHandler("/tmp/log1.txt")
h2.setLevel(logging.WARNING)    # 定义log2 handler的level
h2.setFormatter(fmt2)   # 绑定格式
f2 = logging.Filter('s')    # 过滤器，白名单，放行名为 s.s1 s.s2 的消息
h2.addFilter(f2)    # 在log2的h2 handler上添加一个名为f2的过滤器
log2.addHandler(h2)
# log2.propagate=False
print("log2 handlers: ", log2.handlers)


log3 = logging.getLogger("s.s1.s2")
log3.setLevel(logging.INFO)
print(log3.getEffectiveLevel(), "-----")    # 20 -----
print("log3 handlers: ", log3.handlers)     # log3 handlers:  []  没有添加handler，所以为空
log3.propagate = True   # 自己的handler处理完成后，消息向上传递给父级logger的handler，即log2的所有handler。此如如果不指定，则缺省为true
log3.warning('log3 info。')     # 该条信息的级别大于等于自己logger的级别，所以能过自己(log3)的logger，由于自己没有handler，所以不会由自己的handler输出消息。由于propagate为True，所以消息会向上传递；
                                 # 信息传递给log2的所有handler（不会考虑log2的logger level），且该消息的level大于等于log2 handler的level，所以会通过log2输出。log2的propagate为True（若不设定，默认为True），消息会再次上传递；
                                 # log1的handler级别与该消息相等，消息会传递给log1的所有handler，再次进行输出。
