numbers = [3, 1, 4, 1, 5, 9, 2]
'''numbers[0]
Value: 3

numbers[-1]
Value: 2

numbers[3]
Value: 1

numbers[:-1]
Value: [3, 1, 4, 1, 5, 9]

numbers[3:4]
Value: [1]

5 in numbers
Value: True

7 in numbers
Value: False

"3" in numbers
Value: False

numbers + [6, 5, 3]
Value: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
'''
# 1
numbers[0] = "ten"
# 2
numbers[len(numbers) - 1] = 1
# 3
print(numbers[1:len(numbers) - 1])
# 4
print(9 in numbers)
