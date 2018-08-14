import random
OUTPUT_FILE = "capitalist_conrad_output.txt"
STARTING_PRICE = 10

day_count = 0
current_price = STARTING_PRICE
out_file = open(OUTPUT_FILE, 'w')
print("Starting price: ${0:.2f}".format(STARTING_PRICE), file=out_file)
while (current_price >0.01) and (current_price < 1000):
    if random.uniform(0, 100) <= 50:
        change_percentage = random.uniform(1, 1.1)
    else:
        change_percentage = random.uniform(1, 0.95)
    day_count += 1
    current_price *= change_percentage
    print("On day {0} price is: ${1:.2f}".format(day_count,current_price), file=out_file)
out_file.close()