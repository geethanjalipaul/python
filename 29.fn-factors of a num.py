a=int(input("Enter a number:"))
def factors(a):
    print("Factors are:")
    for i in range(1,a+1):
        if(a%i==0):
            print(i)
factors(a)
    
