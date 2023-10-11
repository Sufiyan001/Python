def Grade(n):
        if n < 0 or n > 100:
            print("Error, please enter numeric input between 0 and 100")
        elif n >= 90:
            return "Your grade is A"
        elif n >= 80:
            return "Your grade is B"
        elif n >= 70:
            return "Your grade is C"
        elif n >= 60:
            return "Your grade is D"
        else: 
            return "Your grade is F"

try:
    mark = float(input("Please enter your score: "))
    grade = Grade(mark)  
except ValueError:
    print("Error, please enter numeric input between 0 and 100.")
else:
    print(grade)