from prac_06.guitar import Guitar


def main():
    gisbon = Guitar("Gibson L-5 CES", "1922", 16035.40)
    another_guitar = Guitar("Another Guitar", "2013", 12345.67)

    guitars = [gisbon, another_guitar]
    # get_age()
    for guitar in guitars:
        print(f"{guitar.name} get_age() - Expected " + str(get_age(int(guitar.year))) + " Got " + str(guitar.get_age()))
    # is_vintage()
    for guitar in guitars:
        print(f"{guitar.name} is_vintage() - Expected " + str(is_vintage(int(guitar.year))) + " Got " + str(
            guitar.is_vintage()))


def get_age(year):
    return 2023 - year


def is_vintage(year):
    if get_age(year) >= 50:
        return True
    else:
        return False


main()
