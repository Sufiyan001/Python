try:
    print("Enter Hours : ")
    Hour = int(input())
    print("Enter Rate : ")
    Rate = float(input())
    if Hour>40:
        salary = 40*Rate+(Hour-40)*(1.5*Rate)
    else:
        salary = Hour*Rate
    print("Pay : ",salary)  
except:
    print("Error,Please enter the numaric input")