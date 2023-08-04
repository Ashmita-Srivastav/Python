I=str(input("Enter the product purchased(Clothing,Shoes,Grocery,Electronic item,Toys)="))
price=float(input("Enter Price of the product: "))
dp=float(input("Enter discount % : "))
discount=price*dp/100
sp=price-discount
print("Cost Price: ",price)
print("Discount:",discount,"%")
print("Selling Price:",sp)
print("***********************Thank You for shopping with us***************************")

