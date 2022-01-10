"""
CP1404/CP5632 Practical
Unreliable Car Class
By Chenyuhan Shen
11/01/2021
"""

from car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name="", fuel=0,  reliability=0):
        """Initialise a Car instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if random.randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            distance += 0
        return distance