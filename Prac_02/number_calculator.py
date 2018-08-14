INPUT_FILE = "numbers.txt"
input_file = open(INPUT_FILE, 'r')
total_numbers = 0
for line in input_file:
    line_number = line
    total_numbers += int(line_number)
print(total_numbers)
input_file.close()