from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Prius 1", 100, 2)
    silver_service_taxi.drive(18)
    printDetails(silver_service_taxi.name, silver_service_taxi.fuel, silver_service_taxi.price_per_km, silver_service_taxi.get_fare(), silver_service_taxi.current_fare_distance)
    silver_service_taxi.start_fare()


def printDetails(name, fuel_units, price, fare, current_fare_distance):
    print(f"Name: {name}")
    print(f"Fuel Units: {fuel_units}")
    print(f"Price per km: {price}")
    print(f"Current Fare Distance: {current_fare_distance}")
    print(f"Fare: {fare}")
    print("")


main()
