#To Find Average Marks and Grade marks


E = int(input("Enter the marks for English:"))
M = int(input("Enter the marks for Maths:"))
P = int(input("Enter the marks for Physics:"))
C = int(input("Enter the marks for Chemistry:"))
I = int(input("Enter the marks for IP:"))
A = int(input("Enter the marks for AI:"))

if(E>35 and M>35 and P>35 and C>35 and I>35 and A>35):
 print("***************Congratulations you Passed in all the subjects************************")


 Mean=(E+M+P+C+I+A)/6
 print("Average marks:",Mean)
 
 print("**********************************************************************")
 T= E+M+P+C+I+A
 Percentage= (T/600)*100
 print("You Got",Percentage,"%")

 if(Percentage>=90):
    print("Congratulations, Your grade is A1")
 elif(Percentage>=80):
    print("Congratulations, Your grade is A2")  
 elif(Percentage>=70):
     print("Congratulations, Your grade is B1")  
 elif(Percentage>=60):
    print("Congratulations, Your grade is B2")  
 elif(Percentage>=50):
     print("Congratulations, Your grade is C1")  
 elif(Percentage>=40):
    print("Congratulations, Your grade is C2")  
 elif(Percentage<40):
    print("Your grade is D")


else:#if conditions is not matching
    Mean=E+M+P+C+I+A/6
    print("**********************************************************************")
    print("Average marks:",Mean)
  
    Percentage= (Mean/600)*100
    print("You Got",Percentage,"%")
    print("------------------------------------------------------------------------")
    print("You have failed in below subjects")
    if(E<35):
     print("You Failed in English=",E)
    else:
        print("You passed in English")
    if(M<35):
       print("You failed in Maths=",M)
    else:
        print("You passed in Maths")
    if(P<35):
     print("You failed in Physics=",P)
    else:
        print("You passed in Physics")
    if(C<35):
     print("You failed in Chemistry=",C)
    else:
        print("You passed in Chemistry")
    if(I<35):
     print("You failed in IP=",I)
    else:
        print("You passed in IP")
    if(A<35):
        print("You failed in AI=",A)
    else:
        print("You passed in AI")
    
