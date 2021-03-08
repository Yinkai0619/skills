import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s\t\t%(message)s", datefmt="%Y/%m/%d %H:%M:%S")
root = logging.getLogger()

log1 = logging.getLogger("s")
log1.setLevel(logging.INFO)
log1.propagate=False
log1.info("line1")

# handler = logging.FileHandler("/tmp/log1.txt", 'a')
# log1.addHandler(handler)
# log1.setLevel(logging.CRITICAL)
#
# log1.info("line2")
# print(log1.handlers)

# log2 = logging.getLogger("s.s1")
# print(log2.getEffectiveLevel)
# log2.setLevel(logging.CRITICAL)
# print(log2.getEffectiveLevel)
# log2.warning("log2 warning")
