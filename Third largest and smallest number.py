#To find the third largest/smallest number in a list.

L=[]
A=int(input("How many numbers you want to enter: "))
for i in range(A):
     num=int(input("Enter the number:"))
     L.append(num)

#to arrange in descending order
L.sort( reverse=True) 
print("The third largest number is:",L[2])     

# to arrange in ascending order 
L.sort(reverse=False)     
print("The third smallest number is:",L[2]) 
