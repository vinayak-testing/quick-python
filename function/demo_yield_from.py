"""yield from similar to yield with the exception that it delegates yield to sub generator"""


def sub_gen(x):
    for i in range(0,100, 2):
        yield i


def gen(y):
    yield from sub_gen(y)


for q in gen(6):
    print(q)