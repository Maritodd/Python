from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, gas_tank, engine, wheels):
        super(Car, self).__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print('Швидкість машини ' + str(self.speed))
        super(Car, self).accelerate()

    def turn(self, side):
        print('Машина зупинилась')
        super(Car, self).turn(side)

    def brake(self):
        super(Car, self).brake()
        print('Машина зупинилась')
        print('-----------------')

    def get_wheels_count(self):
        super(Car, self).get_wheels_count()
