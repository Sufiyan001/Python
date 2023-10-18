while True:
    string = input("Please enter string: ")

    if string.lower() == 'done':
        break

    special_characters = [',', '.', ':', '!', '?']
    for char in special_characters:
        string = string.replace(char, '')

    string = string.upper()

    print(string)
print("--Bye!!")