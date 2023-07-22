#Area and Perimeter



S=str(input("Enter the Shape(triangle, rectangle, square, circle):"))
if S==("triangle"):
   L1=float(input("Enter the length of first side:"))
   L2=float(input("Enter the length of second side:"))
   L3=float(input("Enter the length of third side:"))
   P= L1+L2+L3
   print("The perimeter of triangle is:",P,"units")
   s= P/2
   B= (s*(s-L1)*(s-L2)*(s-L3))
   A= B**0.5
   print("The area of triangle is:",A,"units")

elif S==("rectangle"):
   L=float(input("Enter the length of rectangle:"))
   B=float(input("Enter the breadth of rectangle:"))
   P= 2*(L+B)
   print("The perimeter of Rectangle is:",P,"units")
   A= L*B
   print("The area of Rectangle is:",A,"units")


elif S==("square"):
   L=float(input("Enter the length of side of square:"))
   P= 4*L
   print("The perimeter of Square is:",P,"units")
   A= L**2
   print("The area of Square is:",A,"units")

elif S==("circle"):
   R=float(input("Enter the Radius of circle:"))
   P= 2*3.14*R
   print("The circumference of circle is:",P,"units")
   A= 3.14*R**2
   print("The area of circle is:",A,"units")   
