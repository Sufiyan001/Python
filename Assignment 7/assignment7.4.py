numbers = []
while True:
    enter = input("Please enter an integer: ")
    if enter == "done":
        break
    try:
        number = int(enter)
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print(f"{numbers}, average = {average:.2f}")
    except:
        print("Invalid input. Please enter an integer or 'done' to exit.")
print("---------- Bye !! --------------")