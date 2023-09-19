Second = int(input("Enter seconds : "))
sec1 = Second%60
sec2 = Second//60
min1 = sec2%60
min2 = sec2//60
hour= min2%60
print(Second," seconds is",hour," hours,",min1," minites, ",sec1," seconds")
