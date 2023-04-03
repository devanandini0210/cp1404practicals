numbers = []
for i in range(0, 5):
    numbers.append(int(input("Number: ")))
max_number = max(numbers)
min_number = min(numbers)
average = sum(numbers) / len(numbers)
print("The first number is " + str(numbers[0]))
print("The last number is " + str(numbers[len(numbers) - 1]))
print(
    f"The smallest number is {min_number}\nThe largest number is {max_number}\nThe average of the numbers is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input("Enter username: ")
if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")