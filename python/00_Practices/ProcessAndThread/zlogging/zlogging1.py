import logging

FORMAT1 = "&(name)s %(lineno)d %(levelno)s %(process)d %(processName)s %(thread)s %(message)s"
# FORMAT2 = "%(asctime)-15s\tName: %(name)s\tThread info: %(thread)d %(threadName)s %(message)s %(blog)s"
FORMAT2 = "%(asctime)-15s\tName: %(name)s\tThread info: %(thread)d %(threadName)s %(message)s"

logging.basicConfig(level=logging.INFO,
                    format=FORMAT2,
                    datefmt="%Y%m%d %H:%M:%S")  # , filename="/tmp/pylog.txt", filemode='w')

# site = {"blog": "blog.yinkai.me"}
# logging.info("info: {}".format("test"), extra=site)
# logging.debug("debug: %s", "test")
# logging.error("error test", "aaa")

# 创建新logger实例
root = logging.getLogger()  # 根logger
log1 = logging.getLogger()
log2 = logging.getLogger("l2")
log3 = logging.getLogger("l2.l21")
log4 = logging.getLogger(__name__)  # 未设置level

print("{ln} info: ID:{ID}\tName:{Name}\t\tLevel:{Level}\t\tParent:{Parent}".format(ln="root", ID=id(root), Name=root.name, Level=root.getEffectiveLevel(), Parent=root.parent))
print("{ln} info: ID:{ID}\tName:{Name}\t\tLevel:{Level}\t\tParent:{Parent}".format(ln="log1", ID=id(log1), Name=log1.name, Level=log1.getEffectiveLevel(), Parent=log1.parent))
print("{ln} info: ID:{ID}\tName:{Name}\t\tLevel:{Level}\t\tParent:{Parent}".format(ln="log2", ID=id(log2), Name=log2.name, Level=log2.getEffectiveLevel(), Parent=log2.parent))
print("{ln} info: ID:{ID}\tName:{Name}\t\tLevel:{Level}\t\tParent:{Parent}".format(ln="log3", ID=id(log3), Name=log3.name, Level=log3.getEffectiveLevel(), Parent=log3.parent))
print("{ln} info: ID:{ID}\tName:{Name}\t\tLevel:{Level}\t\tParent:{Parent}".format(ln="log4", ID=id(log4), Name=log4.name, Level=log4.getEffectiveLevel(), Parent=log4.parent))

log2.setLevel(logging.CRITICAL)
print(log2.level, "~~~~~~~~~~~~")
print(log2.getEffectiveLevel(), "``````````````````")
log2.error("log2.error---------------------")
# print(log1.__dict__)
# print(log2.__dict__)


print(log4.name, type(log4), log4.getEffectiveLevel())  # 打印logger信息，注意level
log4.info("hello1 from log4")  # 正常打印
log4.setLevel(28)  # 修改level为28

print(log4.name, type(log4), log4.getEffectiveLevel())  # 再次打印logger信息
log4.info("hello2 from log4")  # INFO的level为20，由于log4的level已经修改为28，该信息由于低于log4的有效level，所以该信息会被屏蔽
log4.warning("hello3 from log4")  # WARNING的level为30，高于log4的level（28)，所以该信息会被正常输出

print(root.name, root.getEffectiveLevel())
root.info("hello4 from root")  # 正常输出
