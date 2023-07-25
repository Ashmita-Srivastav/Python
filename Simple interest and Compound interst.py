# Simple and Compound Interest

A=str(input("Enter what you want to find[Simple interest(SI)/Compound interst(CI)]: "))

if A==("SI"):
 principal = float(input("Enter Principle amount:Rs "))
 time = float(input("Enter time(in years): "))
 rate = float(input("Enter rate: "))
 SI = (principal*time*rate)/100
 print("Simple interest is: ",SI)

else:
 principal = float(input("Enter Principle amount:Rs "))
 time = float(input("Enter time(in years): "))
 rate = float(input("Enter rate: "))
 CI= principal * ( ((1+rate)/100)**time)
 print("Compound interest is:",CI)
