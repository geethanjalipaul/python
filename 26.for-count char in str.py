str=list(input("Enter the string"))
i=0
for i in str:
    if(i!=" "):
        c=0
        for j in range(0,len(str)):
            if(i==str[j]):
                c=c+1
                str[j]=' '
        print(i,"=",c)
