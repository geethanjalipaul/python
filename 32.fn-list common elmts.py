l1=list(input("Enter the 1st list"))
l2=list(input("Enter the 2nd list"))
def fnlist(l1,l2):
    c=0
    for i in l1:
        for j in l2:
            if(i==j):
                return(True)
            else:
                return(False)
if(fnlist(l1,l2)):
   print("Common elements exist")
else:
    print("Common elements does not exist")
