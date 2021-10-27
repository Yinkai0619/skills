import logging

FORMAT = "%(process)d %(processName)s %(thread)s %(message)s"
logging.basicConfig(level=logging.ERROR, format=FORMAT)
root = logging.getLogger()

log1 = logging.getLogger("s1")
log1.setLevel(logging.INFO)

print(log1.getEffectiveLevel(), log1.handlers, log1.parent)
log1.propagate = False
log1.info('log1 test')

# log2 = logging.getLogger("s1.s2")
# log2.warning("log2 warning")
# log2.error("log2 warning")
# print(log2.getEffectiveLevel(), log2.handlers)
# print(root.getEffectiveLevel(), log1.getEffectiveLevel(), log2.getEffectiveLevel())

logging.info()

logging.basicConfig(filemode=)