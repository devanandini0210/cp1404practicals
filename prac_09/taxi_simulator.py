from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 5), SilverServiceTaxi("Hummer", 100, 2)]

    menu = "q)uit, c)hoose taxi, d)rive"
    print("Let's Drive!")
    choice = input(f"{menu}\n").upper()

    while choice != "Q":
        taxi_choice = -1
        bill = 0.0
        if choice == "C":
            try:
                printTaxisAvailable(taxis)
                taxi_choice = int(input("Choose Taxi : "))
                print(f"Bill to Date: ${bill}")
            except ValueError:
                print("Invalid taxi choice \n Bill to date: $0.00")





def printTaxisAvailable(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
main()