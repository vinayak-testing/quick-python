"""yield from similar to yield with the exception that it delegates yeild to sub generator"""


def subgen(x):
    for i in range(0,100, 2):
        yield i


def gen(y):
    yield  from subgen(y)


for q in gen(6):
    print(q)