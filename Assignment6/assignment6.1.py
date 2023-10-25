program = input("Enter the name of the file: ")
try:
    file = open(program)
except:
    print("The file does not exist : ",program)
else:
    for line in file:
        line = line.upper().rstrip()
        print(line)
    file.close()