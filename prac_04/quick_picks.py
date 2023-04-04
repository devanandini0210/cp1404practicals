import random

quick_picks = []

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    pick = []
    for j in range(6):
        temp = random.randint(1, 45)
        while temp in pick:
            temp = random.randint(1, 45)
        pick.append(temp)
    pick.sort()
    quick_picks.append(pick)

for pick in quick_picks:
    for num in pick:
        print(num, end="  ")
    print()
