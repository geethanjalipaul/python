a=int(input("Enter the first number:"))
b=int(input("Enter  the second number:"))
def arithmetic_operation(a,b):
    s=a+b
    m=a*b
    d=a-b
    div=a/b
    return(s,m,d,div)
l=arithmetic_operation(a,b)
print("sum=",l[0])
print("product=",l[1])
print("difference=",l[2])
print("division=",l[3])
