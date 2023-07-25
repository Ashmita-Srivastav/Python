#Calculate profit and loss
CP = float(input(" Please Enter the Cost Price of the Product:Rs "))
SP = float(input(" Please Enter the Sales Price of the product: "))
 
if( CP>SP):
    Loss=CP-SP
    print("Total Loss Amount =Rs ",Loss)
    L= (Loss / CP)*100
    print("Loss percentage= ",L,"%")
elif(SP>CP):
    Profit = SP - CP
    print("Total Profit = RS ",Profit)
    P= (Profit / SP)*100
    print("Profit percentage= ",P,"%")
    print("--------------------------Congratulations-------------------------")
else:
    print("No Profit No Loss!!!")
