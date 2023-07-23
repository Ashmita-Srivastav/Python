#To calculate EMI for Amount, Period and Interest


P = float(input("Enter the Principal or Loan Amount:Rs "))
r = float(input("Enter the Interest Rate Per Month(in percentage):"))
n = float(input("Enter the tenure in number of months:"))
R = (r/12)/100
print(R)
EMI = (P * R * (1 + R)**n)/((1 + R)**n - 1)
print("The EMI for entered value is:",EMI)                

                
