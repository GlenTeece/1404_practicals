MAX_LENGTH = 3
print("Please enter a valid password")
print("Your password must be " +str(MAX_LENGTH)+" Characters long")
password = input(">>>")
while len(password) < MAX_LENGTH:
    print("Invalid password!")
    password = input(">>> ")
for i in range(len(password)):
    print("*",end="")


