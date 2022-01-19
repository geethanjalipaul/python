x=int(input("Enter the first limit"))
y=int(input("Enter the second limit"))
while(x<=y):
    counter=0
    for i in range(1,x+1):
        if x%i==0:
            counter=counter+1
    if counter==2:
            print(x)
    x=x+1
