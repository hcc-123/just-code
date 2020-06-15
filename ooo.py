class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.o_r = 0

    def g_d_n(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def r_o(self):
        print('This car has ' + str(self.o_r) + ' miles on it.')

    def u_o(self, mileage):
        if mileage >= self.o_r:
            self.o_r = mileage
        else:
            print('You cannot roll back an odometre!')

    def i_o(self, miles):
        self.o_r += miles
class B():
    def __init__(self, b_s = 70):
        self.b_s = b_s

    def d_b(self):
        print('This car has a ' + str(self.b_s) + '-KWh battery.')

    def g_r(self):
        if self.b_s == 70:
            range = 240
        elif self.b_s == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

class E(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.b = B()
'''
tesla = E('tesla', 'model s', 2016)
print(tesla.g_d_n())
tesla.b.d_b()
tesla.b.g_r()
'''
