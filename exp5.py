l1=[1,5,10,7]
l2=[3,2,11,7,4]
print(l1)
print(l2)
l3=l1+l2
l3.sort()
print(l3)
print("no.of times 7 occurred is",l3.count(7))
print("sum of elements of list is:",sum(l1))
print("sum of elements in list is:",sum(l2))
if(l1==l2):
    print("the sum is equal")
else:
    print("The sum is not equal")
    
