INPUT_FILE = "name.txt"
input_file = open(INPUT_FILE, 'r')
name = input_file.read()
print("Your name is "+ name)
input_file.close()