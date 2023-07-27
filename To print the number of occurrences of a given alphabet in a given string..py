#To print the number of occurrences of a given alphabet in a given string.


A=str(input("Enter the string: "))
B=str(input("Enter the alphabet: "))
C=A.lower()
D=B.lower()
s=0
for i in C:
    if (i==D):
      s= s+1
print("the occurance of",B,"in the entered string is:",s)
    
