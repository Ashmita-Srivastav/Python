#GST


A=float(input("Enter the Original Price of the product:Rs "))
B=float(input("Enter the Selling Price of the product:Rs "))



if(A<B):
 GST=B-A
 print("The GST/Income tax on the product is:Rs ",GST)
 per=(GST/A)*100
 print("The Percentage of GST is: ",per,"%")

 
else:
    print("-------Selling price can not be less than or equal to original price please recheck the values---")


print=input("Press enter to exit")
quit()
    
                     
