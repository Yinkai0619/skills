try:
    # ret = 1 * 0
    ret = 1 / 0
except ArithmeticError as e:
    print(e)    # 捕获到异常时输出
else:   
    print("OK.")    # 没有异常时输出
finally:
    print("finally.")   # 无论是否发生异常，都会输出
