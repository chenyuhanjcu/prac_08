"""
CP1404/CP5632 Practical
Taxi Test
By Chenyuhan Shen
11/01/2021
"""

from taxi import Taxi

#1.
prius = Taxi("Prius", 100)

#2.
prius.drive(40)

#3.
print(prius)
print(prius.get_fare())

#4.
prius.start_fare()
prius.drive(100)

#5.
print(prius)
print(prius.get_fare())
