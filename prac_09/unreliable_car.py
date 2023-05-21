import random

from prac_09.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.distance = 0

    def __str__(self):
        return f"{super().__str__()}, Reliability : {self.reliability}, Distance Travelled: {self.distance}"

    def drive(self, distance):
        number = random.randint(0, 100)
        if number < self.reliability:
            distance_driven = super().drive(distance)
            self.distance = distance_driven
            return distance_driven
        else:
            return 0
