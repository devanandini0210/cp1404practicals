# 1
name = input("Enter name:")
name_file = open('name.txt', 'w')
print(name, file=name_file)
name_file.close()

# 2
input_file = open("name.txt", "r")
print("Your name is " + input_file.readline())

# 3
number_file = open('numbers.txt', 'r')
total = int(number_file.readline()) + int(number_file.readline())
print(total)

# 4
numbers_file = open("numbers.txt", 'r')
numbers = numbers_file.readlines()
total_sum = 0
for i, number in enumerate(numbers, 1):
    total_sum = total_sum + int(number)
print(total_sum)
