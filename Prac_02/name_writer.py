OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
name = input("please enter your name: ")
print(name,file=out_file)
out_file.close()