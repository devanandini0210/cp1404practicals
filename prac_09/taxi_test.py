from prac_09.taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Prius 1", 100)
    my_taxi.drive(40)
    printDetails(my_taxi.name, my_taxi.fuel, my_taxi.price_per_km, my_taxi.get_fare(), my_taxi.current_fare_distance)
    my_taxi.start_fare()
    my_taxi.drive(100)
    printDetails(my_taxi.name, my_taxi.fuel, my_taxi.price_per_km, my_taxi.get_fare(), my_taxi.current_fare_distance)


def printDetails(name, fuel_units, price, fare, current_fare_distance):
    print(f"Name: {name}")
    print(f"Fuel Units: {fuel_units}")
    print(f"Price per km: {price}")
    print(f"Current Fare Distance: {current_fare_distance}")
    print(f"Fare: {fare}")
    print("")


main()
