print("please enter 5 numbers")
numbers = []
total = 0
for i in range(5):
    user_num = int(input("Numbers: "))
    numbers.append(user_num)
smallest = numbers[0] # so that the int number is in the list
largest = numbers[0]
for i, number in enumerate(numbers):
    smallest = min(smallest,number)
    largest = max(largest,number)
    total += number
average = total / 5
print(numbers)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(smallest))
print("The largest number is {}".format(largest))
print("The average number is {}".format(average))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
input_name = input("Please enter your username")
access_granted = False
for name in usernames:
    if name == input_name:
        access_granted = True
if access_granted:
    print("Access Granted")
else:
    print("Access Denied")
