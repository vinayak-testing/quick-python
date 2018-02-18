mv = 'module variable: mv'
"""cs module: Class scope demonstration module"""


def mf():
    return 'module function can be used like a class method' \
           'in other languages: mf()'


class SC:
    scv = 'superclass class variable: self.scv'
    __pscv = 'private superclass class variable : no access'

    def __init__(self):
        self.siv = 'superclass instance variable: self.siv (but for access use SC.siv ) superclass instance variable: ' \
              'self.siv (but for access use SC.siv ) '
        self.__psiv = 'private superclass instance variable: no access'

    def sm(self):
        return "superclass method: sm()"

    def __spm(self):
        return "superclass private method: no access"


class C(SC):
    cv = 'class variable: self.cv (but use C.cv for assignment)'
    __pcv = 'private class variable: self.__pcv(but use C.__pcv for assignment)'

    def __init__(self):
        super().__init__()
        self.iv = 'instance variable: self.iv'
        self.__piv = 'private instance variable: self.__piv'

    def m2(self):
        return 'method: self.m2()'

    def __pm(self):
        return 'private method:sefl.__pm()'

    def m(self, p='parameter:p'):
        lv = 'local variable: lv'
        print('Access local, global and built-in namespaces directly')
        print('local namespace:', list(locals().keys()))
        print(p)  # parameter

        print(lv)   # instance variable
        print('global namespace:', list(globals().keys()))
        print(mv)
        print(mf())

        print("Access instance, class and superclass namespace using 'self'")
        print("Instance namespace:", dir(self))
        print(self.iv)
        print(self.__piv)
        print(self.siv)

        print('class namespace:', dir(self.__class__))
        print(self.cv)
        print(self.m2())
        print(self.__pcv)
        print(self.__pm())

        print("Superclass namespace:", dir(SC))
        print(self.sm())
        print(self.scv)


c = C()
c.m()
















