Sum = 0
count = 0
while True:
    Number = input("Enter a number : ")
    if Number == "done" or Number == "Done":
        break
    else:
        try:
            num = int(Number)
        except:
            print("invalid input. enter a number")
            continue
        Sum = Sum + num
        count = count + 1
print("Sum of input numbers : ",Sum)
print("number of input : ",count)
print("Average of input numbers : ",float(Sum/count))