#To find Sale price 

I=str(input("Enter the product purchased(Clothing,Shoes,Grocery,Electronic item,Toys)="))
#Cost Price
M1=30000
M2=10000
M3=20000
M4=50000
M5=15000
if I==("Clothing"):
 print("The Cost Price of Clothing is:Rs",M1)
 D=20
 print("Discount is:",D,"%")
 discount=M1*D/100
 Sp=M1-discount
 print("You have to pay:RS",Sp)

elif I==("Shoes"):
  print("The Cost Price of Shoes is:Rs",M2)
  D=10
  print("Discount is:",D,"%")
  discount=M2*D/100
  Sp=M2-discount
  print("You have to pay:RS",Sp)


elif I==("Grocery"):
 print("The Cost Price of Grocery is:Rs",M3)
 D=12
 print("Discount is:",D,"%")
 discount=M3*D/100
 Sp=M3-discount
 print("You have to pay:RS",Sp)


elif I==("Electronic item"):
  print("The Cost Price of Electronic item is:Rs",M4)
  D=50
  print("Discount is:",D,"%")
  discount=M4*D/100
  Sp=M4-discount
  print("You have to pay:RS",Sp)


elif I==("Toys"):
  print("The Cost Price of Toys is:Rs",M5)
  D=6
  print("Discount is:",D,"%")
  discount=M5*D/100
  Sp=M5-discount
  print("You have to pay:RS",Sp)

print("**************************THANK YOU FOR SHOPPING WITH US************************")
 
