l1=[0,3,9,50]
l2=[73,4,7,10]
print(l1)
print(l2)
c=0
if(len(l1)==len(l2)):
    print("lists are of equal length")
else:
    print("lists are of different length")
if(sum(l1)==sum(l2)):
    print("sum of both lists are equal")
else:
    print("sum of both lists are not equal")
for i in l1:
    for j in l2:
        if i==j:
            c=c+1
            print(i)
if c==0:
    print("common elements doesnot exist")
else:
    print("common elements exist")
