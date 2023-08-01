#Finding Density and Force


Mass = int(input("enter value of mass:"))
Length = int(input("enter value of Length:"))
Volume = Length**3
Density = Mass/Volume
print("the density of entered values is:",Density)
A= input("Do you want to find Force(Y/N):")
if A==("Y"):
    print("YES")
    print(input("press enter to proceed for finding Force"))
    Acceleration = float(input("enter the value of Acceleration:"))
    Force = Mass*Acceleration
    print("Force is:",Force)
    print=input("press enter to exit")
    quit()
else :
    print("THANK YOU")
    print=input("press enter to exit")
    quit()
