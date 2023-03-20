"""
CP1404 - Practical 2
Program Name:Password Stars
Author: Devanandini Chakravarti
Date:20.03.2023
"""


def main():
    password = get_password()
    length = len(password)
    print_asterisk(length)


def print_asterisk(length):
    for i in range(1, length + 1, 1):
        print("*", end="")
    print()


def get_password():
    pwd = ""
    c = 0
    while c == 0:
        pwd = input("Enter Password: ")
        length = len(pwd)
        if length <= 0:
            print("Enter valid password!")
        else:
            c += 1
    return pwd


main()
