def foo(word:str):
    for w in word:
        yield w

def bar(word:str):
    yield from word

s = "Nana."
# f = foo(s)
f = bar(s)
for _ in range(len(s)):
    print(next(f))


