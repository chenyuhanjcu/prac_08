"""
CP1404/CP5632 Practical
Taxi simulator
By Chenyuhan Shen
11/01/2021
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    """Simulating Program."""
    print("Let's drive!")
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            bill_to_date += drive_taxi(current_taxi, taxis)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        choice = input(MENU).lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Let user choose one taxi from taxis."""
    print("Taxi available:")
    display_taxis(taxis)
    chosen_taxi = int(input("Choose taxi: "))
    try:
        chosen_taxi = taxis[chosen_taxi]
    except IndexError:
        print("Invalid taxi choice")
    return chosen_taxi


def drive_taxi(current_taxi):
    """Drive taxi."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        trip_cost = 0
    else:
        current_taxi.start_fare()
        drive_distance = float(input("Drive how far? "))
        current_taxi.drive(drive_distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


if __name__ == '__main__':
    main()