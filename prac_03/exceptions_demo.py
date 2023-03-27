"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: ValueError occurs when the values provided for the numerator and denominator are not of integer type

2. When will a ZeroDivisionError occur?
Answer: ZeroDivisionError occurs when the value provided for the denominator is zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes. Updated code below.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
