def check_neon(number):
    temp=number
    temp=temp**2
    sum=0
    while(temp>0):
        last=temp%10
        sum=sum+last
        temp=temp//10
    if(sum==number):
        return True
    else:
        return False
n=int(input("Enter the number:"))
if(check_neon(n)):
    print(n,"is a neon number")
else:
    print(n,"is not a neon number")
