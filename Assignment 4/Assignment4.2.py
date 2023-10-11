def computepay(hours,rate):        
        hours = float(hours)
        rate = float(rate)

        if hours <= 40:
            pay = hours * rate
        else:
            pay = (40 * rate) + ((hours - 40) * (1.5 * rate))

        return pay
        
try:
    hours = input("Enter hours: ")
    rate = input("Enter rate: ")
    salary = computepay(hours,rate)
    print("Pay :",salary)
except:
     print("Error, please enter numeric input")