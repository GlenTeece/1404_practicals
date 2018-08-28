number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))
total_cost = 0
for i in range(number_of_items):
    item_price = float(input("Price of Item: "))
    total_cost += item_price
print("Total price for "+str(number_of_items)+" item/s is "+str(total_cost))

def item_combiner():
