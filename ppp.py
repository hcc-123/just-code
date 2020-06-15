class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temp:
    cel = Celsius()
    fah = Fahrenheit()

'''
class A(object):
    run = True

class D(A):
    fly = False
    def ddd(self, age):
        self.age = age
    def sound(self):
        return 'wang wang~'

d = D()
print(d.sound())
'''
t = Temp()
t.fah = 760
print(t.cel)