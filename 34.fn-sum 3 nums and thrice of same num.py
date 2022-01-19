x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
z=int(input("Enter the 3rd number:"))
def thrice(a,b,c):
    s=a+b+c
    if a==b==c:
        return(3*s)
    else:
        return(s)
print("Sum=",thrice(x,y,z))
