x=int(input("Enter the no:"))
print("factors of",x,"are")
count=0
for n in range(1,x+1):
    if x%n==0:
        print(n)
        count=count+1
if count==2:
    print(x,"is a prime number")
else:

    print(x,"is not a prime number")
