"""scopetest: our scope test module"""
from builtins import print

v = 6


def f(x):
    """f: scope test function"""
    print("globals", list(globals().keys()))
    print("Entry Locals: ", locals())
    y = x
    w = v
    print("Exit Locals: ", list(locals().keys()))

