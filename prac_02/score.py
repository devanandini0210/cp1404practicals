"""
CP1404 - Practical 2
Program Name:Score
Author: Devanandini Chakravarti
Date:20.03.2023
"""


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)


def get_result(score):
    result = ""
    if score < 0 or 100 < score:
        result = "Invalid score"
    else:
        if score > 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        elif score < 50:
            result = "Bad"
    return result


main()
