# dictionary to store names of states and their capitals

s=dict()
n=int(input("Enter the number of states: "))
for i in range(n):
   state=str(input("Enter the name of the state: "))
   capital=str(input("Enter the name of the capital:"))
   s[state]=capital
print("Created dictionary of state and their capital is:",s)
   
name=str(input("Enter the name of the state"))
print(s[name])
