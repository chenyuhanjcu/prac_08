"""
CP1404/CP5632 Practical
Silver Service Taxi Test
By Chenyuhan Shen
11/01/2021
"""

from silver_service_taxi import SilverServiceTaxi

#1.
hummer = SilverServiceTaxi("Hummer", 100, 2)

#2.
hummer.drive(18)

#3.
print(hummer)
print(hummer.get_fare())

#4.
hummer.start_fare()
hummer.drive(100)

#5.
print(hummer)
print(hummer.get_fare())
