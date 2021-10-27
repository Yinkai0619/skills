import logging

root = logging.getLogger()    # root logger
print(root.name, root.getEffectiveLevel(), type(root), root.parent, id(root))   # root 30 <class 'logging.RootLogger'> None 139760029805488，由此可见，root logger没有父，且默认级别为30（WARNING）

logger = logging.getLogger(__name__)    # 模块级logger
print(logger.name, logger.getEffectiveLevel(), type(logger), logger.parent, id(logger))   # __main__ 30 <class 'logging.Logger'> <RootLogger root (WARNING)> 140706290429760

loggerchild = logging.getLogger(__name__ + '.child')    # 模块logger的子logger
print(loggerchild.name, loggerchild.getEffectiveLevel(), type(loggerchild), loggerchild.parent, id(loggerchild))    # __main__.child 30 <class 'logging.Logger'> <Logger __main__ (WARNING)> 140706290429664


