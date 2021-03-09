import os
import logging

os.system("clear")

logging.basicConfig(format="%(name)s %(asctime)s %(message)s", level=logging.INFO)

root = logging.getLogger()
root.setLevel(logging.ERROR)
print("root: ", root.handle)

h0 = logging.StreamHandler()
h0.setLevel(logging.WARNING)
root.addHandler(h0)

print("root handlers: ", root.handlers)

for h in root.handlers:
    print("root handler = {}, formatter = {}".format(h, h.formatter))

print(root.getEffectiveLevel())
logging.info("test root info~~~~~~~~~~")