"""
CP1404 - Practical 2
Program Name:Temperatures
Author: Devanandini Chakravarti
Date:20.03.2023
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))  # taking the input from user in Fahrenheit
            celsius = convert_to_celsius(fahrenheit)  # converting value from Fahrenheit to Celsius
            print(f"Result: {celsius:.2f} C")  # printing the results in Celsius
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()