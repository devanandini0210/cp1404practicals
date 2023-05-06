from Guitar import Guitar


def main():
    guitars = []

    in_file = open(' guitars.csv', 'r')
    in_file.readline()

    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], (parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    name = input("Enter Guitar name: ")
    while name != "":
        year = int(input("Enter the year it was made: "))
        cost = float(input("Enter the cost of the guitar: "))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Enter Guitar name: ")

    f = open("guitars.csv", "w")
    for guitar in guitars:
        f.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    f.close()


main()
