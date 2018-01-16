"""Generators are special kind of functions you can use to create your own iterables"""


def four():
    x = 0;
    while x < 4:
        print("in generator value of x =", x)
        yield x
        x += 1


for i in four():
    print(i)
