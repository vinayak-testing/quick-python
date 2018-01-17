"""Variables in python can be local, global or non-local scoped"""


def fun():
    global a
    a = 1
    print(a)
    b = 2


a = 'one'
b = 'two'
fun()
print(a)
print(b)

"""Non local variable"""
g_var = 0
nl_var = 0
print("toplevel -> g_var:{0} nl_var:{1}".format(g_var, nl_var))


def test():
    nl_var = 2
    print("in test() -> g_var:{0} nl_var:{1}".format(g_var, nl_var))

    def inner_test():
        global g_var
        nonlocal nl_var
        g_var = 1
        nl_var = 4
        print("in inner_test() -> g_var:{0} nl_var:{1}".format(g_var, nl_var))

    inner_test()
    print("in test() -> g_var:{0} nl_var:{1}".format(g_var, nl_var))


test()
print("toplevel -> g_var:{0} nl_var:{1}".format(g_var, nl_var))
