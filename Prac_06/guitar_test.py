from Prac_06.guitar import Guitar

my_gibson = Guitar("Gibson L-5 CES",1922,16035.40)
my_fender = Guitar("Example Fender",1996,1500.40)

print("Testing")
print(my_gibson)
print(my_fender)

print("Gibson L-5 CES get_age() - Expected 96. Got {}".format(my_gibson.get_age()))
print("Example Fender get_age() - Expected 22. Got {}".format(my_fender.get_age()))
print("Gibson L-5 CES is_vintage - Expected True. Got {}".format(my_gibson.is_vintage()))
print("Example Fender is_vintage - Expected False. Got {}".format(my_fender.is_vintage()))