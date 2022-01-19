n=int(input("Enter a number:"))
def digit(s):
    sum=l=0
    while(s>0):
        l=s%10
        sum=sum+l
        s=s//10
    print("sum of digits=",sum)
digit(n)
        
