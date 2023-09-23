try:
    print("Enter Score: ")
    Number = int(input())
    if Number >=0 and Number <=100:
        if Number>=90:
            Grade = "A"
        elif Number>=80:
            Grade = "B"
        elif Number>=70:
            Grade = "C"
        elif Number>=60:
            Grade = "D"
        else:
            Grade = "F"
        print("Grade is ",Grade)
    else:
        print("Error,please enter numeric input between 0 and 100")
except:
    print("Error,please enter numeric input between 0 and 100")