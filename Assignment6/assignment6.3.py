program = input("Enter the file name: ")
total = 0
count = 0
try:
    file = open(program,"r")
except:
    print("File can not be opened: ",program)
else:
    lines = file.readlines()
    for line in lines:
        if line.startswith("X-DSPAM-Confidence:"):
            split = line.split(":")
            if len(split) == 2:
                number = float(split[1])
                total =total + number
                count =count + 1
    print("Avarage Spam Confidence: ", (total/count))
file.close()