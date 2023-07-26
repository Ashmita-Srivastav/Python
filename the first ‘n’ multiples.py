#To print the first ‘n’ multiples of a given number.

A = int(input("Enter the desired number: "))

n = int(input("Enter the desired multiples of entered number: "))

for i in range(1,n+1):
      print(A,"*",i,"=",A*i)
