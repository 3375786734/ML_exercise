class t(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def p(self):
        print(self.__a)
        print(self.__b)
c = t(1,2)
c.p()
