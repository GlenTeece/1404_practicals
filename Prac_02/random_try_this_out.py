import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
Line 1 will print a random integer between 5 and 20, largest is 20, smallest is 5
Line 2 will print a random odd number between 3 and 10 (9), largest is 9, smallest is 3, 4 is impossible
Line 3 will print a random decimal float between 2.5 and 5.5, largest is 5.5 smallest is 2.5
"""