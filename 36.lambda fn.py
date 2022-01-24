a=int(input("Enter the side of a square:"))
area1=lambda a:a*a
x=area1(a)
print("Area of square=",x)
l=int(input("Enter the length of the rectangle:"))
w=int(input("Enter the breadth of the rectangle:"))
area2=lambda l,w:l*w
y=area2(l,w)
print("Area of rectangle=",y)
b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle:"))
area3=lambda b,h:0.5*b*h
z=area3(b,h)
print("Area of the triangle:",z)
