string = input("please Enter string: ")

number = 0
upper_case = 0
lower_case = 0
other = 0

for char in string:
    if char.isdigit():
        number += 1
    elif char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1
    else:
        other += 1

print("uppercase letters:", upper_case)
print("lowercase letters:", lower_case)
print("numbers:", number)
print("other characters:", other)