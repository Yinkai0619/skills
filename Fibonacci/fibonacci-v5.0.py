
import functools

@functools.lru_cache()
def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


# for i in range(1, 11):
#     print(fib(i))

print(fib(150))
