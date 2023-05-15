from prac_09.unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Prius 1", 100, 50)
    my_car.drive(40)
    printDetails(my_car.name, my_car.fuel, my_car.reliability, my_car.distance)
    my_car.drive(100)
    printDetails(my_car.name, my_car.fuel, my_car.reliability, my_car.distance)


def printDetails(name, fuel_units, reliability, distance):
    print(f"Name: {name}")
    print(f"Fuel Units: {fuel_units}")
    print(f"Reliability: {reliability}")
    print(f"Distance Travelled: {distance}")
    print("")


main()
