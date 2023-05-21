from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 5), SilverServiceTaxi("Hummer", 100, 2)]

    menu = "q)uit, c)hoose taxi, d)rive"
    print("Let's Drive!")
    choice = input(f"{menu}\n").upper()
    taxi_choice = -1
    bill = 0.0

    while choice != "Q":

        if choice == "C":
            try:
                print("Taxis available:")
                printTaxis(taxis)
                taxi_choice = int(input("Choose Taxi : "))
                if 0 > taxi_choice or taxi_choice >= len(taxis):
                    print("Invalid Taxi Choice")
            except ValueError:
                print("Invalid taxi choice")
            print(f"Bill to Date: ${bill}")
        elif choice == "D":

            if taxi_choice != -1:
                distance = int(input("Drive how far? "))
                taxis[taxi_choice].drive(distance)
                fare = taxis[taxi_choice].get_fare()
                print(f"Your {taxis[taxi_choice].name} trip cost you ${fare}")
                bill += fare
                print(f"Bill to Date: ${bill}")
            else:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to Date: ${bill}")
        else:
            print("Invalid Option")

        choice = input(f"{menu}\n").upper()
    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    printTaxis(taxis)


def printTaxis(taxis):

    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
