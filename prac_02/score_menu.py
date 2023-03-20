"""
CP1404 - Practical 2
Program Name:Score
Author: Devanandini Chakravarti
Date:20.03.2023
"""

menu = """(G)et a valid score 
(P)rint result
(S)how stars 
(Q)uit"""


def main():
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            print_stars(int(score))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")


def get_score():
    score = 0.0
    c = 0

    while c == 0:
        score = float(input("Enter score: "))
        if score < 0 or 100 < score:
            print("Invalid score")
        else:
            c+-0
            break
    return score


def get_result(score):
    if score > 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score < 50:
        result = "Bad"
    return result


def print_stars(score):
    for i in range(1, score + 1, 1):
        print("*", end="")
    print()


main()
