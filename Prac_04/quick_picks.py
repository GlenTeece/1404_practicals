import random

MIN = 1
MAX = 45
NUM_PER_LINE = 6

lines = int(input("how many quick picks? "))
for line in range(lines):
    quick_pick = []
    for i in range(NUM_PER_LINE):
        num = random.randint(MIN, MAX)
        while num in quick_pick:  # DO IT AGAIN IF IT'S ALREADY IN THERE
            num = random.randint(MIN, MAX)
        quick_pick.append(num)
    quick_pick.sort()
    print(" ".join("{:2}".format(num) for num in quick_pick))  # Copied this line from solutions
