#To find largest and smallest number from a list of numbers

list= []
A=int(input("How many numbers you want to enter?: "))
for i in range(A):
    num=int(input("Enter the number: "))
    list.append(num)

    
print("The largest number is:",max(list))
print("The smallest number is:",min(list))
