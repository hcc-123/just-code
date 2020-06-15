'''
class My:
    def __get__(self, instance, owner):
        print('getting', self, instance, owner)
    def __set__(self, instance, value):
        print('setting', self, instance, value)
    def __delete__(self, instance):
        print('deleting', self, instance)

class T:
    x = My()

t = T()
t.x = 'x-man'
t.x
del t.x
'''
class Mp:
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self,instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = Mp(getX, setX, delX)

c = C()

