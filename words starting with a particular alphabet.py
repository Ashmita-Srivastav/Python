#To print the words starting with a particular alphabet in a user entered string.


A=str(input("Enter the string:"))
B=str(input("Enter the alphabet: "))
C=A.lower()
D=B.lower()
E=C.split(" ")
found=False
for i in E: 
    if i[0]==D:
      print(i)
      found=True
if(found==False):
     print("There is no such word") 
