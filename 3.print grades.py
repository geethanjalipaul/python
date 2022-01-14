a=int(input("Enter the marks of ASE:"))
b=int(input("Enter the marks of ADS:"))
c=int(input("Enter the marks of MFC:"))
d=int(input("Enter the marks of DCA:"))
e=int(input("Enter the marks of P LAB:"))
total=a+b+c+d+e
avg=(total/5)
if(avg<80):
    print("A Grade")
elif(avg<60):
    print("B Grade")
elif(avg<40):
    print("C Grade")
else:
    print("Falied")
