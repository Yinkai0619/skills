import logging

FORMAT="%(process)d %(processName)s %(thread)s %(message)s"
# FORMAT="%(asctime)s %(message)s\t%(school)10s"
logging.basicConfig(level=logging.WARNING, format=FORMAT,
                    datefmt="%Y%m%d %H:%M:%S")

# logging.info('info test')
# logging.debug('debug test')
# d = {'school': 'BJOU'}
# logging.info('info test: %s', 'abc1', extra=d)

log1 = logging.getLogger(__name__)
log2 = logging.getLogger(__name__ + '.child')

log1.info('log1 test')
log2.info('log2 test')
log1.warning('log1_test')
log2.warning('log2_test')

print(log1.name)
print(log2.name)

print(log1.level)
print(log2.level)

print(log1.getEffectiveLevel())
print(log2.getEffectiveLevel())

log2.setLevel(28)

print(log1.getEffectiveLevel())
print(log2.getEffectiveLevel())

log3 = logging.getLogger(__name__+'.child'+'.child')
print(log3.name, log3.parent, log3.getEffectiveLevel())


# print(log1.name)
# print(log1.parent)
# print(log1.level)
# print(log1.__dict__)

